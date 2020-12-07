from django.shortcuts import render
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def button(request):
    return render(request,'home.html')

def output(request):

    lala = {
        'B5 100ml 기획' : 'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=%EB%9D%BC%EB%A1%9C%EC%8A%88%ED%8F%AC%EC%A0%9C+%EC%8B%9C%EC%B9%B4+%ED%94%8C%EB%9D%BC%EC%8A%A4%ED%8A%B8%EB%B0%A4+B5+100ml%EA%B8%B0%ED%9A%8D',
        '폼클렌징': 'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=%EC%95%84%ED%81%AC%EB%84%A4%EC%8A%A4+%EB%AA%A8%EC%9D%B4%EC%8A%A4%EC%B2%98+%ED%8F%BC+%ED%81%B4%EB%A0%8C%EC%A0%80',
        '토너':'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=%EC%96%B8%EC%84%BC%ED%8B%B0%EB%93%9C',
        '우루우루 40 * 4개입' : 'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=%EC%9A%B0%EB%A3%A8%EC%9A%B0%EB%A3%A8%2040%EB%A7%A4',
        'Aestura(내꺼)' : 'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=Aestura',
        '상하 크림' : 'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=%EB%B9%84%EC%9A%98%EB%93%9C+1%2B1+new',
        '우르오스' : 'https://m.lalavla.com/service/search/searchResult.html?searchKeyword=%EC%9A%B0%EB%A5%B4%EC%98%A4%EC%8A%A4+%EC%8A%A4%ED%82%A8+%EB%A1%9C%EC%85%98+%EC%A7%80%EB%B3%B5%ED%95%A9%EC%84%B1+200ml'
        }
    Chrome_options = webdriver.ChromeOptions()
    Chrome_options.add_argument('headless')
    Chrome_options.add_argument('--disable-gpu')
    data = []
    data += "랄라블라 "
    try:
        for key, val in lala.items():
            driver = webdriver.Chrome('/Users/yun/desktop/buttonpython/chromedriver',options=Chrome_options)
            url = val
            driver.get(url)
            time.sleep(0.2)

            try :
                content = driver.page_source.encode('utf-8').strip()
                soup = BeautifulSoup(content, "html.parser")
                price = soup.select("span.price")[0]
                Total = price.text.split('원')
                if(len(Total) == 2):
                    data += "|"+Total[0] +"원|  "
                else:
                    data += "|"+Total[1] +"원|  "
            except:
                data += "|판매 안함| "
    except:
            data += "오류! "
    driver.quit()
    olive = {
        'B5 100ml 기획' :'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=B5%20100ml%20%EA%B8%B0%ED%9A%8D&giftYn=N',
        '폼클렌징': 'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=%EC%95%84%ED%81%AC%EB%84%A4%EC%8A%A4%20%EB%8D%94%EB%A7%88%EB%A6%B4%EB%A6%AC%ED%94%84%20%EB%AA%A8%EC%9D%B4%EC%8A%A4%EC%B2%98%20%ED%8F%BC%ED%81%B4%EB%A0%8C%EC%A0%80%20125ml&giftYn=N',
        '토너':'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=%EC%96%B8%EC%84%BC%ED%8B%B0%EB%93%9C%20%ED%86%A0%EB%84%88&giftYn=N',
        '우루우루 40 * 4개입' : 'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=%EC%9A%B0%EB%A3%A8%EC%9A%B0%EB%A3%A8%2040%EB%A7%A4&giftYn=N',
        'Aestura(내꺼)' : 'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?onlyOneBrand=&query=%EC%97%90%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%84%ED%86%A0%EB%B2%A0%EB%A6%AC%EC%96%B4365%20%ED%81%AC%EB%A6%BC%2080ml&giftYn=N',
        '상하 크림' : 'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=%EB%B9%84%EC%9A%98%EB%93%9C%20%EC%88%98%EB%B6%84%ED%81%AC%EB%A6%BC%201%2B1&giftYn=N',
        '우르오스' : 'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=%EC%9A%B0%EB%A5%B4%EC%98%A4%EC%8A%A4&giftYn=N'
}

    Chrome_options = webdriver.ChromeOptions()
    Chrome_options.add_argument('headless')
    Chrome_options.add_argument('--disable-gpu')

    data += "/올리브영 "

    try:
        for key, val in olive.items():
            driver = webdriver.Chrome('/Users/yun/desktop/buttonpython/chromedriver', options=Chrome_options)
            url = val
            driver.get(url)
            time.sleep(0.2)

            try:
                content = driver.page_source.encode('utf-8').strip()
                soup = BeautifulSoup(content, "html.parser")
                divs = soup.select("p.prd_price")[0]
                price = divs.select(".tx_num")
                data += "|" + price[1].text +"원|  "
            except:
                data += "|" + price[0].text +"원|  "
    except:
        data += "오류! "
    driver.quit()

    LOHB = {
    'B5 100ml' : 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%8B%9C%EC%B9%B4%20%ED%94%8C%EB%9D%BC%EC%8A%A4%ED%8A%B8%20%EB%B0%A4B5%20100ml&mallId=7',
    '폼클렌징' : 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EB%8D%94%EB%A7%88%20%EB%A6%B4%EB%A6%AC%ED%94%84%20%EB%AA%A8%EC%9D%B4%EC%8A%A4%EC%B2%98%20%ED%8F%BC%ED%81%B4%EB%A0%8C%EC%A0%80%20125ml&mallId=7',
    '토너':'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%96%B8%EC%84%BC%ED%8B%B0%EB%93%9C%20%EC%9C%84%EC%B9%98%ED%95%98%EC%A0%A4%20%ED%86%A0%EB%84%88%20355ml&mallId=7',
    '우루우루 40매' : 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%9A%B0%EB%A3%A8%EC%9A%B0%EB%A3%A8%2040%EB%A7%A4&mallId=7',
    'Aestura(내꺼)' : 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=Aestura&mallId=7',
    '상하 크림' : 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%97%94%EC%A0%A4%20%EC%95%84%EC%BF%A0%EC%95%84%ED%81%AC%EB%A6%BC%201%2B1&mallId=7',
    '우르오스' : 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%98%AC%EC%9D%B8%EC%9B%90%20%EC%8A%A4%ED%82%A8%20%EB%A1%9C%EC%85%98%20200ml&mallId=7'
    }

    Chrome_options = webdriver.ChromeOptions()
    Chrome_options.add_argument('headless')
    Chrome_options.add_argument('--disable-gpu')

    try:
        data += "/LOHB "
        for key, val in LOHB.items():
            driver = webdriver.Chrome('/Users/yun/desktop/buttonpython/chromedriver',options=Chrome_options)
            url = val
            driver.get(url)
            time.sleep(0.2)

            try :
                content = driver.page_source.encode('utf-8').strip()
                soup = BeautifulSoup(content,"html.parser")
                price = soup.select("span.srchCurrentPrice")
                data += "|"+ price[0].text + "| "
            except:
                data += "|판매 안함| "
    except:
        data+= "오류!"
    driver.quit()
    data = "".join(data)
    data = data.split("/")

    return render(request, 'home.html',{'data':data})
