# This is a sample Python script.

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def print_hi():
    server = Server(r'D:\exchange_data\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    # 设置driver options
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

    driver = webdriver.Chrome(chrome_options=chrome_options)
    #
    url = 'https://www.baidu.com/'
    proxy.new_har('fund', options={'captureHeaders': True, 'captureContent': True})
    driver.get(url)

    result = proxy.har
    print(result)

    for entry in result['log']['entries']:
        _url = entry['request']['url']
        # 根据URL找到数据接口
        # if "lsjz?callback=" in _url:
        _response = entry['response']
        _content = _response['content']['text']
            # 获取接口返回内容
        print(_content)
    server.stop()
    # driver.quit()
