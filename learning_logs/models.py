from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # 使用django自带的User类，并在Topic创建外键指向User
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """学到的关于某个主题的具体知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """设置变格的复数形式"""
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        return self.text[:50] + "..."
