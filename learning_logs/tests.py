from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import index


class HomePageTest(TestCase):
    def testWhenOpenRootUrlThenShowHomePage(self):
        """测试url和view"""
        found = resolve('/')
        self.assertEqual(found.func, index)

    def testWhenOpenHomePageThenShowRightHtml(self):
        """测试template"""
        request = HttpRequest()
        response = index(request)
        self.assertEqual(render_to_string('learning_logs/index.html'), response.content.decode())





"""
读取文件全部内容为字符串，for循环遍历exist_sn_list判断sn有没有在文本字符串中，
有则输出此sn和文件名
1.看看能不能通过判断包含^FD^FS的字符串来确认此rawdata使用的sn不好
2.找几个比较通用的sn：通过看elements确定常用字段
  如果没有，看看能不能在uat做数据,要和corpmes1一致
3.点击view data后，增加最长时间限制，到时换sn，
  同一个label也可以多打几个sn，文件名加sn为后缀做区分

"""