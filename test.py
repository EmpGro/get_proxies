import requests
import get_ip_list
from bs4 import BeautifulSoup
import time


def print_ip(proxies):
    """利用http://www.whatismyip.com.tw/显示访问的ip"""
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Proxy-Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    url = 'http://www.whatismyip.com.tw/'
    try:
        page = requests.get(url, headers=headers, proxies=proxies)
    except:
        print(str(proxies) + 'is wrong')
    else:
        soup = BeautifulSoup(page.text, 'lxml')
        my_ip = soup.find('b').text
        print(my_ip)


def main():
    url = 'http://www.data5u.com/free/type/https/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
    ip_list = get_ip_list.get_ip_list(url, headers)
    print(ip_list)
    for aip in ip_list:
        proxy = get_ip_list.get_proxy(aip)
        print_ip(proxy)


if __name__ == '__main__':
    main()


