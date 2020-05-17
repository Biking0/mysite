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
from django.db.models import Count
# from django.db import connections

import operator

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
                  {'page_obj': page_obj})  # 返回page_obj对象

    # print(result)
    # print(result[0].name)
    # # print(list(result))
    # # result=1
    # return render(request, 'tender_info.html', {'result': result})


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
    if 'search_input' in request.GET:
        search_input = request.GET['search_input']
        if not search_input:
            error = True
        elif len(search_input) > 20:
            error = True
        else:
            # books = tender_info.objects.filter(name__icontains=q)

            result = tender_info.objects.filter(name__icontains=search_input)
            current_page = request.GET.get('p')  # 使用get方法来获取翻页的页数
            paginator = Paginator(result, 10)  # Paginator生成一个对象，然后传入queryset,
            try:  # 以及每页显示的个数，这里每页显示十个
                page_obj = paginator.page(current_page)  # 根据get方法取到的数字显示页数
            except EmptyPage as e:  # 如果get方法获取了一个没有的页数则显示第一页
                page_obj = paginator.page(1)
            except PageNotAnInteger as e:  # 传入一个字符串也显示第一页
                page_obj = paginator.page(1)
            return render(request, 'search_results.html',
                          {'page_obj': page_obj, 'query': search_input})  # 返回page_obj对象

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


# 地区排名
def region_top(request):
    # result=tender_info.objects.filter(name='招标公告名称测试')
    # result = tender_info.objects.raw(sql)
    # result = tender_info.objects.filter(name__contains="郑州").values('name').annotate(count=Count('name')).values('name','count')

    region_list = [{'region': '郑州', 'count': 0},
                   {'region': '开封', 'count': 0},
                   {'region': '洛阳', 'count': 0},
                   {'region': '平顶山', 'count': 0},
                   {'region': '安阳', 'count': 0},
                   {'region': '鹤壁', 'count': 0},
                   {'region': '新乡', 'count': 0},
                   {'region': '焦作', 'count': 0},
                   {'region': '濮阳', 'count': 0},
                   {'region': '许昌', 'count': 0},
                   {'region': '漯河', 'count': 0},
                   {'region': '三门峡', 'count': 0},
                   {'region': '南阳', 'count': 0},
                   {'region': '商丘', 'count': 0},
                   {'region': '信阳', 'count': 0},
                   {'region': '周口', 'count': 0},
                   {'region': '驻马店', 'count': 0}]
    for i in region_list:
        count = tender_info.objects.filter(name__contains=i['region']).count()
        i['count'] = count

    print(region_list)

    result_sort = sorted(region_list, key=operator.itemgetter('count'), reverse=True)
    print(result_sort)
    # print(result)
    # print(result[0].name)
    # # print(list(result))
    # # result=1
    return render(request, 'region_top.html', {'result': result_sort})


# 公告浏览量排名
def view_top(request):
    # result=tender_info.objects.filter(name='招标公告名称测试')
    # result = tender_info.objects.raw(sql)
    # result = tender_info.objects.filter(name__contains="郑州").values('name').annotate(count=Count('name')).values('name','count')
    view_list = tender_info.objects.order_by("-view_cont")[:10]

    zz = tender_info.objects.filter(name__contains="郑州").count()
    ly = tender_info.objects.filter(name__contains="洛阳").count()
    ay = tender_info.objects.filter(name__contains="安阳").count()

    # result = tender_info.objects.values_list('msg_status').annotate(Count('id'))
    # cursor = connection.cursor()
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # print(ret)
    result = []
    zz_str = {'region': '郑州', 'count': zz}
    ay_str = {'region': '安阳', 'count': ay}
    ly_str = {'region': '洛阳', 'count': ly}

    result.append(zz_str)
    result.append(ay_str)
    result.append(ly_str)
    print(result)

    result_sort = sorted(result, key=operator.itemgetter('count'), reverse=True)
    print(result_sort)

    print(view_list)
    # print(result)
    # print(result[0].name)
    # # print(list(result))
    # # result=1
    return render(request, 'view_top.html', {'result': view_list})


# 行业排名
def industry_top(request):
    # result=tender_info.objects.filter(name='招标公告名称测试')
    # result = tender_info.objects.raw(sql)

    industry_list = [{'industry': '教育', 'search_str': '大学', 'count': 0},
                     {'industry': '银行', 'search_str': '银行', 'count': 0},
                     {'industry': '快递', 'search_str': '快递', 'count': 0},
                     {'industry': '能源', 'search_str': '煤', 'count': 0},
                     {'industry': '房地产', 'search_str': '房地产', 'count': 0},
                     {'industry': '交通', 'search_str': '交通运输', 'count': 0}]
    for i in industry_list:
        count = tender_info.objects.filter(name__contains=i['search_str']).count()
        i['count'] = count

    print(industry_list)

    result_sort = sorted(industry_list, key=operator.itemgetter('count'), reverse=True)
    print(result_sort)
    # print(result)
    # print(result[0].name)
    # # print(list(result))
    # # result=1
    return render(request, 'industry_top.html', {'result': result_sort})

# def control_spider():
