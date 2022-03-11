
import bs4
import requests
import time
import calendar
import sqlite3 as sq
from datetime import date, timedelta, datetime
from . import scrapy_excuetion as se

def scraper_func():
    while True:
        try:
            con = sq.connect(r"C:\Users\Sankar Senthil\Documents\Daemon\DB_conv\new column\basketball.db")
            cursor = con.cursor()
            try:
                id = cursor.execute("select id,date from s21_22  where top_boxscore_1 = '' order by id limit 1").fetchall()[0]
                print('id>>>',id)
                cursor.execute(f"delete from s21_22 where id>={id[0]} or date ='{id[1]}'")
                con.commit()
            except Exception:
                print("Exception>>>>",Exception)

            st_Date = cursor.execute("select Date from s21_22 order by id").fetchall()[-1][0].split('/')
            print("st_Date",st_Date)
            st_Date[0], st_Date[1] = st_Date[1], st_Date[0] 
            D = [int(i) for i in st_Date]

            start_date = date(D[-1]+2000, D[1], D[0]) 
            end_date =  datetime.now().date() + timedelta(days=2) 
            delta = end_date - start_date   
            scrap = se.Scrapper()
            for i in range(delta.days + 1):
                day = start_date + timedelta(days=i)
                scrap.wday = calendar.day_name[day.weekday()][:3]
                scrap.day = str(day)
                y, m, d = scrap.day.split('-')
                print(y, m, d)
                # scrap.main_page(int(m), int(d), int(y))
                scrap.main_page(m, d, y)
                
                print(day)
                print("*"*150)

        except Exception as e:
            print(e)
        finally:
            con.commit()
            con.close()
            time.sleep(10800)
            break

scraper_func()
        