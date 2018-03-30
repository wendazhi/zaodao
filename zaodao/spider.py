from zaodao.driver import Driver
from zaodao.saveData import Save
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from zaodao.config import *
import time


#初始化mongoDB对象
class Spider(object):

    def __init__(self):
        #初始化浏览器对象
        self.driver = Driver()
        self.save = Save()

    def get_index_url(self,page):
        baseUrl = BASE_URL
        url = {
            "keywords":KEYWORDS,
            "page":page
        }
        url = urlencode(url)
        return baseUrl+url

    def parse_html(self,html):
        items = pq(html)('#company_list .company_item').items()
        for item in items:
            company={
                'companyName':item.find('.company_name_text').text().replace('\n',''),
                'companyDomain':BASE_DOMAIN+item.attr('href'),
                'baseInfoCorporate':item.find('.base_info').children().eq(0).text()[5:],
                'baseInfoCapital':item.find('.base_info').children().eq(1).text()[5:],
                'baseInfoEstablish':item.find('.base_info').children().eq(2).text()[5:],
                'baseInfoTel':item.find('.contact_info').children().eq(0).text()[3:],
                'baseInfoEmail':item.find('.contact_info').children().eq(1).text()[3:],
                'baseInfoAddr':item.find('.contact_info').children().eq(2).text().replace('\n','')[3:],
            }
            yield company


if __name__ == "__main__":
    spider = Spider()
    for page in range(1,10):
        time.sleep(5)
        currentUrl = spider.get_index_url(page)
        # 当不传参时使用默认的本地地址, 用于测试
        pageSource = spider.driver.get_index_page(currentUrl)
        # pageSource = spider.driver.get_index_page(currentUrl)
        if pageSource:
            print('============================')
            try:
                # 获取导航页的基本信息
                for content in spider.parse_html(pageSource):
                    # 保存到文件中
                    spider.save.save_to_mongoDB(content)
                    spider.save.save_to_file(content)
            except Exception as e:
                print(e)
                spider.driver.drive_close()
    spider.driver.drive_close()