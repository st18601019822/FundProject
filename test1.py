import re
import time
import datetime
if __name__ == '__main__':
    ele_json='http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183013248650036662357_1611125979803&fundCode=161725&pageIndex=1&pageSize=20&startDate=&endDate=&_=1611125979816'
    # url=ele_json.find('pageIndex')
    # t=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # ts=int(time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S")))
    # print(ts)
    t = time.time()
    s=str(int(round(t * 1000)))
    url=re.sub(r'&pageIndex=[0-9]',"&pageIndex="+"2",ele_json)
    print(url)
    url1=re.sub(r'endDate=&_=[0-9]+',"endDate=&_="+s,url)
    print(url1)
    # url1=ele_json.replace("")
    # print(ele_json[url:])
    # print(url)

# if __name__ == '__main__':
#     print(get_record())
#     print(type(get_record()))