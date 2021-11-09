import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
import csv
from selenium.webdriver.chrome.options import Options
 
# main処理
def main():
 
    # メルカリのURL
    BASE_URL = 'https://www.mercari.com'
 
    #キーワード読み込み
    args = sys.argv
    KEYWORD = args[1]
    for i in range(2,len(args)):
        KEYWORD += '+' + args[i]
 
    URL_INI = BASE_URL + '/jp/search/?keyword=' + KEYWORD + '&status_trading_sold_out=1'
    url = URL_INI
 
    # 検索結果格納用配列
    result_array = [['item_name','item_price','url']]
 
    # 次ページ番号格納用
    next_page_num = 2
 
    while True:
 
        # スクレイピング実行
        try:
            # Chrome設定
            options = Options()
            options.add_argument('--headless')
 
            #対象URLにリクエスト
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            time.sleep(5)
 
            # 文字コードをUTF-8に変換し、html取得
            html = driver.page_source.encode('utf-8')
            soup = BeautifulSoup(html, "html.parser")
 
            # tagとclassを指定して要素を取り出す
            item_name = soup.find('div', class_='items-box-content clearfix').find_all('h3', class_='items-box-name font-2')
            item_price = soup.find('div', class_='items-box-content clearfix').find_all('div', class_='items-box-price font-5')
            item_url = soup.find('div', class_='items-box-content clearfix').find_all('a')
 
            pager = soup.find('ul', class_='pager').find_all('a')
 
            item_num = len(item_name)
 
            for i in range(0,item_num):
                result_array.append([item_name[i].text,
                                    int(item_price[i].text.replace('\','').replace(',','')),
                                    BASE_URL + item_url[i].get('href')])
 
            for x in pager:
                if x.text == str(next_page_num):
                    next_url = BASE_URL + x.get('href')
 
            if next_url == '':
                break
 
            next_page_num += 1
            url = next_url
            next_url = ''
 
            print('nextpagenum:'+str(next_page_num))
 
 
        except Exception as e:
            message = "[例外発生]"+os.path.basename(__file__)+"\n"+"type:{0}".format(type(e))+"\n"+"args:{0}".format(e.args)
            print(message)
 
        finally:
            # 起動したChromeを閉じる
            driver.close()
            driver.quit() 
 
 
    # csvファイルへ書き込み
    with open('mercari-soldvalue.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(result_array)
 
if __name__ == '__main__':
    main()