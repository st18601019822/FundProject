from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import time
import re
from urllib.request import Request, urlopen

# def get_url():
if __name__ == '__main__':
    server = Server(r'D:\exchange_data\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    # 设置driver options
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--disable-gpu')
    chrome_driver = r'D:\exchange_data\chromedriver.exe'
    #
    json_url=''
    url = 'http://fundf10.eastmoney.com/jjjz_161725.html'
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


    driver = webdriver.Chrome(executable_path=chrome_driver, options = chrome_options)
    # proxy.new_har('fund', options={'captureHeaders': True, 'captureContent': True})
    proxy.new_har(url)

    driver.get(url)

    result = proxy.har
    for entry in result['log']['entries']:
        # entry['request']['url']
        if "lsjz" in entry['request']['url']:
            json_url=entry['request']['url']
            for i in range(1,69):
                t = time.time()
                s = str(int(round(t * 1000)))
                url = re.sub(r'&pageIndex=[0-9]', "&pageIndex=" + str(i), json_url)
                url1 = re.sub(r'endDate=&_=[0-9]+', "endDate=&_=" + s, url)
                print(url1)
                request = Request(url1, headers=firefox_headers)
                html = urlopen(request)
                # 获取数据
                data = html.read()
                # 转换成字符串
                strs = str(data)
                # 获取接口返回内容

                # 构建请求
                print(strs)

# if __name__ == '__main__':
#     # print(requests.session().get(get_url()).text.replace("'", '"').replace('/ ', '/'))
#     print(get_url())