from logging import exception
import bs4
import requests
import calendar
import sqlite3 as sq
from datetime import date, timedelta, datetime

class Scrapper:
    def __init__(self):
        # self.main_url = "https://www.basketball-reference.com/boxscores/?month=%s&day=%s&year=%s"
        # self.teams_url = "https://www.basketball-reference.com/teams/%s/%s_games.html"
        self.main_url = "https://www.sports-reference.com/cbb/boxscores/index.cgi?month=%s&day=%s&year=%s"
        self.teams_url = "https://www.sports-reference.com/cbb/schools/%s/2022-schedule.html"
        self.main_domain = "https://www.sports-reference.com"   
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        self.strdate = ''
        self.day, self.wday = '',''
 
    def main_page(self, m, d, y):
        self.strdate = f"{y}-{m}-{d}"
        print(self.main_url % (int(m), int(d), y))
        response = requests.get(self.main_url % (int(m), int(d), y),headers = self.headers)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        game_summaries = soup.findAll('div',{'class':'game_summary nohover'})

        for gsrow in game_summaries:
            # print(gsrow)
            try:
                teams = gsrow.find('table',{"class":"teams"})
                top, bottom = teams.findAll('a')[0].get('href').split('/')[3], teams.findAll('a')[-1].get('href').split('/')[3]
                boxscore_url = self.main_domain+teams.findAll('a')[1].get('href')

                tr, trd,  tgame_steak, twldet, tpts, tPGm = 0,[],[],0,0,0
                br, brd, bgame_steak, bwldet, bpts, bPGm = 0,[],[],0,0,0

                tr, trd,  tgame_steak, twldet, tpts, tPGm, tGL = self.teams_page(top, y)
                br, brd, bgame_steak, bwldet, bpts, bPGm, BGL = self.teams_page(bottom, y)

                if tGL == 'N':
                    tGL, BGL = 1, 1
                elif tGL == '@':
                    tGL, BGL = 0, 2
                else:
                    tGL, BGL = 2, 0


                t1, t2, b1, b2 = self.box_score(boxscore_url)

                fdate = f"{m}/{d}/{y[2:]}"
                
                tsteak = tgame_steak[0] if tgame_steak else 0
                bsteak = bgame_steak[0] if bgame_steak else 0
                
                t1w = twldet[:1].count('W')
                b1w = bwldet[:1].count('W')
                t2w = twldet[:2].count('W')
                b2w = bwldet[:2].count('W')
                t3w = twldet[:3].count('W')
                b3w = bwldet[:3].count('W')
                t4w = twldet[:4].count('W')
                b4w = bwldet[:4].count('W')
                t5w = twldet[:5].count('W')
                b5w = bwldet[:5].count('W')
                t6w = twldet[:6].count('W')
                b6w = bwldet[:6].count('W')
                t7w = twldet[:7].count('W')
                b7w = bwldet[:7].count('W')
                t8w = twldet[:8].count('W')
                b8w = bwldet[:8].count('W')
                t9w = twldet[:9].count('W')
                b9w = bwldet[:9].count('W')
                t10w = twldet[:10].count('W')
                b10w = bwldet[:10].count('W')
                t11w = twldet[:11].count('W')
                b11w = bwldet[:11].count('W')
                t12w = twldet[:12].count('W')
                b12w = bwldet[:12].count('W')
                t13w = twldet[:13].count('W')
                b13w = bwldet[:13].count('W')
                t14w = twldet[:14].count('W')
                b14w = bwldet[:14].count('W')
                t15w = twldet[:15].count('W')
                b15w = bwldet[:15].count('W')

                
                trd = trd if trd else 0
                brd = brd if brd else 0
                rdd = trd-brd 
                sd = int(tsteak) - int(bsteak)
                w8dd = int(t8w) - int(b8w)
                w8c = int(t8w) + int(b8w)

                # print(wday, fdate, top, tr, trd, rdd, tsteak, sd, t8w, w8dd, w8c)

                # if tPGm >= 15 and bPGm >= 15:
                con = sq.connect(r"C:\Users\Sankar Senthil\Documents\Daemon\DB_conv\new column\basketball.db")
                cursor = con.cursor()
                
                cursor.execute(
                    """
                    insert into S21_22(
                        Day ,
                        Date ,
                        Top_Team ,
                        Top_Site_Value ,
                        Top_boxscore_1 ,
                        Top_boxscore_2 ,
                        Top_Current_Game_Score ,
                        Bottom_Team ,
                        Bottom_Site_Value ,
                        Bottom_boxscore_1 ,
                        Bottom_boxscore_2 ,
                        Bottom_Current_Game_Score ,
                        Top_Record ,
                        Top_WIN$_Last_1_games,
                        Top_WIN$_Last_2_games,
                        Top_WIN$_Last_3_games,
                        Top_WIN$_Last_4_games,
                        Top_WIN$_Last_5_games,
                        Top_WIN$_Last_6_games,
                        Top_WIN$_Last_7_games,
                        Top_WIN$_Last_8_games,
                        Top_WIN$_Last_9_games,
                        Top_WIN$_Last_10_games,
                        Top_WIN$_Last_11_games,
                        Top_WIN$_Last_12_games,
                        Top_WIN$_Last_13_games,
                        Top_WIN$_Last_14_games,
                        Top_WIN$_Last_15_games,
                        Bottom_WIN$_Last_1_games,
                        Bottom_WIN$_Last_2_games,
                        Bottom_WIN$_Last_3_games,
                        Bottom_WIN$_Last_4_games,
                        Bottom_WIN$_Last_5_games,
                        Bottom_WIN$_Last_6_games,
                        Bottom_WIN$_Last_7_games,
                        Bottom_WIN$_Last_8_games,
                        Bottom_WIN$_Last_9_games,
                        Bottom_WIN$_Last_10_games,
                        Bottom_WIN$_Last_11_games,
                        Bottom_WIN$_Last_12_games,
                        Bottom_WIN$_Last_13_games,
                        Bottom_WIN$_Last_14_games,
                        Bottom_WIN$_Last_15_games,
                        Bottom_Record ,
                        Total_WIN$_Combined_Last_8_games_Between_Both_Teams ,
                        Record_Diffence_Differential ,
                        Streak_Differential ,
                        Top_Streak ,
                        Bottom_Streak ,
                        Wins_Last_8_games_differential ,
                        top_number_of_previous_games_played ,
                        Bottom_number_of_previous_games_played ,
                        Top_Record_Difference ,
                        Bottom_Record_Difference 
                    )values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)                        """,
                    (self.wday, fdate, top, tGL, t1, t2, tpts, bottom, BGL, b1, b2, bpts, tr, t1w, t2w, t3w, t4w, t5w, t6w, t7w, t8w, t9w, t10w, t11w, t12w, t13w, t14w, t15w, b1w, b2w, b3w, b4w, b5w, b6w, b7w, b8w, b9w, b10w, b11w, b12w, b13w, b14w, b15w, br, w8c, rdd,sd ,tsteak, bsteak, w8dd, tPGm,  bPGm, trd,  brd)
                )
                print("Worked - 1")
                con.commit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                con.close()
                print(self.wday, fdate, top, tGL, t1, t2, tpts, bottom, BGL, b1, b2, bpts, tr, t8w, b8w, br, w8c, rdd,sd ,tsteak, bsteak, w8dd, tPGm,  bPGm, trd,  brd)
            # else:pass
            except Exception:
                pass

    
    def box_score(self, boxscore_url):
        try:
            response = requests.get(boxscore_url,headers = self.headers)
            soup = bs4.BeautifulSoup(response.content, 'html.parser')
            all_line = soup.findAll('div',{"id":"all_line-score"})
            a = ''
            for i in all_line[0]:
                if '<!--' in str(i):
                    pass
                else:
                    a+=str(i)
            soup = bs4.BeautifulSoup(a, 'html.parser')

            t1, b1 = soup.findAll('td',{"data-stat":'1'})
            t2, b2 = soup.findAll('td',{"data-stat":'2'})

            return (t1.text, t2.text, b1.text, b2.text)
        except:
            return ("", "", "", "")


    def teams_page(self, team, year):
            date, wl, game_streak, wldet, Gsteak, rd = '', '0-0', '', [], [], 0
            teams_response = requests.get(self.teams_url % team)
            teams_soup = bs4.BeautifulSoup(teams_response.content, 'html.parser')
            tbody = teams_soup.findAll("tbody")
            tr = tbody[1].findAll('tr')

            for tdrow in tr:
                try:
                    try:
                        pts = tdrow.find('td',{'data-stat':'pts'}).text
                    except:
                        pts = ""
                    
                    game_location = tdrow.find('td',{'data-stat':'game_location'}).text
                    date = tdrow.find('td',{'data-stat':'date_game'})
                    date = str(date).split('=')[2].split(' ')[0][1:-1]
                    if date == self.day:
                        break
                    else:pass
                    wins = tdrow.find('td',{'data-stat':'wins'}).text
                    losses = tdrow.find('td',{'data-stat':'losses'}).text
                    game_streak = tdrow.find('td',{'data-stat':'game_streak'}).text
                    a = '-' if 'L' in game_streak else ''
                    wldet.append(game_streak.split(' ')[0])
                    Gsteak.append(f"{a}{game_streak.split(' ')[-1]}")
                    wl = f"{wins}-{losses}"
                    rd = int(wins)-int(losses)
                except Exception as e:
                    # print(e     )
                    pass
            # wl = wl[::-1][:8]
            PGm = len(wldet)
            Gsteak = Gsteak[::-1][:8]
            wldet = wldet[::-1]

            return (wl, rd, Gsteak, wldet, pts, PGm, game_location)

# if __name__ == "__main__":
    
    # start_date = date(2022, 3, 14) 
    # end_date =  datetime.now().date() + timedelta(days=2)   
    # delta = end_date - start_date   
    # scrap = Scrapper()
    # for i in range(delta.days + 1):
    #     day = start_date + timedelta(days=i)
    #     scrap.wday = calendar.day_name[day.weekday()][:3]
    #     scrap.day = str(day)
    #     y, m, d = scrap.day.split('-')
    #     scrap.main_page(m, d, y)
    #     print(day)
    #     print("*"*150)