import requests
from bs4 import BeautifulSoup

import pymysql
import time
import config

def Main():
    
    time.sleep(900)
    
    while True:
        html = requests.get(config.parse_url).content
        soup = BeautifulSoup(html, "lxml")

        db = pymysql.connect(host = config.host, user = config.user, password = config.password, database = config.name)
        cur = db.cursor()
        
        all_block = soup.find_all("tr", class_="rates-table")
        for i in range(len(all_block)):
            if i == 0 or i == 1 or i == 18:
                block = all_block[i]
                
                title = block.find("td", class_="mobile-hide").find("a", class_="black-link").text

                price = block.find_all("td", class_="rates-val")[2].find("div", class_="rates-calc-block -big-sum").text
                price = price.replace("₽", "")
                price = price.replace(",", ".")
                price = round(float(price.replace(" ", "")))
                price = int(price)
                
                req = f"SELECT price FROM `rates` WHERE title = '{title}'"
                cur.execute(req)
                db.commit()
                
                last_rate = cur.fetchone()
                
                if last_rate is None:
                    req = f"INSERT INTO `rates`(title, price) VALUES ('{title.lower()}', {price})"
                    cur.execute(req)
                    db.commit()
                else:
                    if last_rate[0] != price:
                        req = f"UPDATE `rates` SET price = {price} WHERE title = '{title.lower()}'"          
                        cur.execute(req)
                        db.commit()
                        
        cur.close()
        db.close()
        
        print("OVER")
        time.sleep(3600)