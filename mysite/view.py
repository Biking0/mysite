from django.template import Template, Context
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render

from books.models import tender_info

import datetime


def hello(request):
    return HttpResponse("Hello world11ddddddd22")


# def current_datetime(request):
#     #now = datetime.datetime.now()
#     #html = "It is now %s." % now
#
#     now = datetime.datetime.now()
#     t = Template("<html><body>It is now {{ current_date }}.<span>hello</span></body></html>")
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)

def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "It is now %s." % now

    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s. " % (offset, dt)
    num_list = ['1', '2', '3']
    return render(request, 'hours_ahead.html', {'next_time': dt, 'hour_offset': offset})


def test_for(request):
    num_list = ['1', '2', '3']
    return render(request, 'current_datetime.html', {'num_list': num_list})


def mypage(request):
    current_section = 'mypagetest'
    return render(request, 'mypage.html', {'current_section': current_section})

# 检索数据
def book_tender_info(request):
    # result=tender_info.objects.filter(name='招标公告名称测试')
    result=tender_info.objects.all()
    print(result)
    print(result[0].name)
    # print(list(result))
    # result=1
    return render(request, 'tender_info.html', {'result': result})


