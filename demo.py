import requests
from bs4 import BeautifulSoup

def main():
    headers = {
        #'cookies': cookies,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
    url = 'http://www.whatismyip.com.tw/'
    proxies = {'https': 'https://122.72.18.60:8620',}
    page = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(page.text, 'lxml')
    my_ip = soup.find('b').text
    print(my_ip)

if __name__ == '__main__':
	main()