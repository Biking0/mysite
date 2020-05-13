from django.template import Template, Context
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render
from django import forms
from books.models import tender_info

from django.shortcuts import render
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime
import time


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


# 展示数据
def book_tender_info(request):
    # result=tender_info.objects.filter(name='招标公告名称测试')
    result = tender_info.objects.all()
    print(result)
    print(result[0].name)
    # print(list(result))
    # result=1
    return render(request, 'tender_info.html', {'result': result})


# 展示数据，翻页
def book_tender_info_page(request):
    # result=tender_info.objects.filter(name='招标公告名称测试')
    result = tender_info.objects.all()
    current_page = request.GET.get('p')  # 使用get方法来获取翻页的页数
    paginator = Paginator(result, 10)  # Paginator生成一个对象，然后传入queryset,
    try:  # 以及每页显示的个数，这里每页显示十个
        page_obj = paginator.page(current_page)  # 根据get方法取到的数字显示页数
    except EmptyPage as e:  # 如果get方法获取了一个没有的页数则显示第一页
        page_obj = paginator.page(1)
    except PageNotAnInteger as e:  # 传入一个字符串也显示第一页
        page_obj = paginator.page(1)
    return render(request, 'tender_info_page.html',
                  {'page_obj': page_obj})    #返回page_obj对象



    print(result)
    print(result[0].name)
    # print(list(result))
    # result=1
    return render(request, 'tender_info.html', {'result': result})


# 打印访问信息
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


# 搜索书籍
def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = tender_info.objects.filter(name__icontains=q)
            return render(request, 'search_results.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html',
                  {'error': error})

    # if 'q' in request.GET and request.GET['q']:
    #     q = request.GET['q']
    #     books = tender_info.objects.filter(name__icontains=q)
    #     return render(request, 'search_results.html',
    #                   {'books': books, 'query': q})
    # else:
    #     return render(request, 'search_form.html',
    #                   {'error': True})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


def title(request):
    return render(request, 'title.html')
