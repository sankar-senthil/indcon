
import bs4
import requests
import time
import calendar
import sqlite3 as sq
from datetime import date, timedelta, datetime
import scrapy_excuetion as se

def scraper_func():
    today = ''
    cttime = str(datetime.now()).split(' ')
    while True:
        if today != cttime[0] and cttime[-1].split(':')[0] == '09':
            today = cttime[0]
            cttime = str(datetime.now()).split(' ')
            print(today)
            print(cttime)
        else:pass

        try:
            con = sq.connect(r"C:\Users\Sankar Senthil\Documents\Daemon\DB_conv\basketball.db")
            cursor = con.cursor()
            try:
                cursor.execute("delete from s21_22 where top_boxscore_1 = ''")
                con.commit()
            except:
                pass

            st_Date = cursor.execute("select Date from s21_22 order by id").fetchall()[-1][0].split('/')
            st_Date[0], st_Date[1] = st_Date[1], st_Date[0] 
            D = [int(i) for i in st_Date]

            start_date = date(D[-1]+2000, D[1], D[0]) 
            print(start_date)
            end_date = date(2022, 3, 6)    
            delta = end_date - start_date   
            scrap = se.Scrapper()
            for i in range(delta.days + 1):
                day = start_date + timedelta(days=i)
                scrap.wday = calendar.day_name[day.weekday()][:3]
                scrap.day = str(day)
                y, m, d = scrap.day.split('-')
                scrap.main_page(m, d, y)
                print(day)
                print("*"*150)
        except Exception as e:
            print(e)
        finally:
            con.commit()
            con.close()
            time.sleep(2)