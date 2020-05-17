# encoding=utf8
# 爬虫主函数
# by hyn
# 20200322


# 构造url，根据url获取书数据，调用简略解析，调用详细解析
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

# sys.path.append('D:/python_project/test_pwd/common')
sys.path.append('D:/project/github/tender_spider')

from tender_spider.tender_spider.url_pool import url_pool  as url_pool
import tender_spider.tender_spider.config as config
from tender_spider.tender_spider.get_data.test.get_data import get_data
import tender_spider.tender_spider.parser.test.sample_parser as sample_parser
import tender_spider.tender_spider.parser.test.content_parser as content_parser
import tender_spider.tender_spider.conn_db.test.save_data as save_data
import time


# 构造url，根据url获取书数据，调用简略解析，调用详细解析
def main():
    pro_totalpage = url_pool.pro_totalpage()
    city_totalpage = url_pool.city_totalpage()

    print('开始爬取，总页数：', pro_totalpage)

    # 自定义爬虫进度
    # spider_status = save_data.get_spider_status()
    for i in range(1, pro_totalpage):

        # 更新爬虫状态
        data = [i, pro_totalpage]
        save_data.update_spider_status(data)

        while True:
            # 判断爬虫状态
            spider_status = save_data.get_spider_status()
            if spider_status[0][1] == 1:
                print('停止爬取 sleep 10s')
                time.sleep(10)
            else:
                break

        url = config.pro_page_url + str(i)
        print('正在爬取省级公告，第', i, '页', url)
        response = get_data(url)
        sample_info_list = sample_parser.parser(response)

        # 解析详细信息
        for j in sample_info_list:
            # print('解析详细信息')
            # print(j)
            response_content = get_data(j[4])
            content_parser.parser(response_content)

    for i in range(1, pro_totalpage):
        url = config.pro_page_url + str(i)
        print('正在爬取市县区公告，第', i, '页', url)
        response = get_data(url)
        sample_info_list = sample_parser.parser(response)

        # 入库详细信息
        for j in sample_info_list:
            print('入库详细信息')
            print(j)
            response_content = get_data(j[4])
            content_parser.parser(response_content)
