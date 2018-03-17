from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from .form import TopicForm, EntryForm
from .models import Topic, Entry


def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """显示所有的主题"""
    topics_obj = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics_obj}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题的所有条目"""
    topic_obj = Topic.objects.get(id=topic_id)
    check_topic_owner(topic_obj.owner, request.user)
    entries = topic_obj.entry_set.order_by('date_added')
    context = {'topic': topic_obj, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_t = form.save(commit=False)
            new_t.owner = request.user
            new_t.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    return render(request, 'learning_logs/new_topic.html', {'form': form})


@login_required
def new_entry(request, topic_id):
    """在特定主题下添加新条目"""
    topic_obj = Topic.objects.get(id=topic_id)
    check_topic_owner(topic_obj.owner, request.user)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry_obj = form.save(commit=False)
            entry_obj.topic = topic_obj
            entry_obj.save()
            return HttpResponseRedirect(
                reverse('learning_logs:topic', args=[topic_id])
            )

    return render(request, 'learning_logs/new_entry.html',
                  {'topic': topic_obj, 'form': form})


@login_required
def edit_entry(request, entry_id):
    """修改特定条目，每个条目的id在全主题中也是唯一的"""
    entry_obj = Entry.objects.get(id=entry_id)
    topic_obj = entry_obj.topic
    check_topic_owner(topic_obj.owner, request.user)

    if request.method != 'POST':
        form = EntryForm(instance=entry_obj)
    else:
        form = EntryForm(instance=entry_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('learning_logs:topic', args=[topic_obj.id])
            )

    return render(request, 'learning_logs/edit_entry.html',
                  {'topic': topic_obj, 'entry': entry_obj, 'form': form}
                  )


def check_topic_owner(owner, current_user):
    """确认请求的主题属于当前用户"""
    if owner != current_user:
        raise Http404
