import sqlite3 as sq, os
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from threading import Thread

import subprocess

# Create your views here.

global ColumnName, Filter

# Thread(target=scrapy.scraper_func,daemon=True).start()


def dashboard(requests):
    global ColumnName, Filter
    ColumnName = ''
    Filter = ''
    connection = sq.connect(r"C:\Users\Sankar Senthil\Documents\Daemon\ICONT\InCont\basketball.db")  # connect to your DB
    cursor = connection.cursor()
    data=cursor.execute('''SELECT * FROM s20_21 WHERE ID=1''')
    data = [ column[0] for column in data.description ]

    box = [
            
            'Top_Team',
            'Top_boxscore_1',
            'Top_boxscore_2',
            'Top_Pre_Game_Score',
            'Bottom_Team',
            'Bottom_boxscore_1',
            'Bottom_boxscore_2',
            'Bottom_Pre_Game_Score',
            'Top_Site_Value',
            'Bottom_Site_Value',
            'Day',
            'Date',
            ]

    box_1 = [
            
            'Top_Record',
            'Top_Record_Difference',
            'top_number_of_previous_games_played',
            'Record_Diffence_Differential',
            'Bottom_Record',
            'Bottom_Record_Difference',
            'Bottom_number_of_previous_games_played',
            'Wins_Last_8_games_differential',
            ]

    box_2 = ['Streak_Differential',
            'Top_Streak',
            'Bottom_Streak']
    box_3 = [
            'Top_WIN$_Last_1_games',
            'Top_WIN$_Last_2_games',
            'Top_WIN$_Last_3_games',
            'Top_WIN$_Last_4_games',
            'Bottom_WIN$_Last_1_games',
            'Bottom_WIN$_Last_2_games',
            'Bottom_WIN$_Last_3_games',
            'Bottom_WIN$_Last_4_games',
            'Top_WIN$_Last_5_games',
            'Top_WIN$_Last_6_games',
            'Top_WIN$_Last_7_games',
            'Top_WIN$_Last_8_games',
            'Bottom_WIN$_Last_5_games',
            'Bottom_WIN$_Last_6_games',
            'Bottom_WIN$_Last_7_games',
            'Bottom_WIN$_Last_8_games',
            'Top_WIN$_Last_9_games',
            'Top_WIN$_Last_10_games',
            'Top_WIN$_Last_11_games',
            'Top_WIN$_Last_12_games',
            'Bottom_WIN$_Last_9_games',
            'Bottom_WIN$_Last_10_games',
            'Bottom_WIN$_Last_11_games',
            'Bottom_WIN$_Last_12_games',
            'Top_WIN$_Last_13_games',
            'Top_WIN$_Last_14_games',
            'Top_WIN$_Last_15_games',
            'empty',
            'Bottom_WIN$_Last_13_games',
            'Bottom_WIN$_Last_14_games',
            'Bottom_WIN$_Last_15_games']

    # 'Total_WIN$_Combined_Last_8_games_Between_Both_Teams',
    try:
        box_1.remove('ID')
    except:pass
    order_by = 'twins,twins'
    names = [box_1[i:i+4] for i in range(0, len(box_1), 4)]
    box_4t = [box_3[i:i+4] for i in range(0, len(box_3), 4)]
    box_0 = [box[i:i+4] for i in range(0, len(box), 4)]
    context = {'names':names,'box_2':box_2,'box_4t':box_4t,"box":box_0}
    if requests.method == 'POST':
        Ddata = dict(requests.POST)
        #print(Ddata)
        data=cursor.execute('''SELECT * FROM s20_21 WHERE ID=1''')
        data = [ column[0] for column in data.description ]

        for i in data:
            col='-'
            if i in ['Top_Current_Game_Score','Bottom_Current_Game_Score'] or i in Ddata.keys() :
                if i in ['Top_Current_Game_Score','Bottom_Current_Game_Score']:
                    col = 'Top_Pre_Game_Score' if i == "Top_Current_Game_Score" else "Bottom_Pre_Game_Score"
                    value = Ddata[col]
                else:
                    value = Ddata[i]
                # print(value)
                try:
                    value.remove('')
                except:pass
                if i == 'Record':
                    order_by = 'Top_Record' if value[0] == 'Top_Record' else 'Bottom_Record'
                    order_by = "Cast(substr(@, 0,instr(@, '-'))AS DECIMAL), Cast(substr(@, 3,instr(@, '-')) AS DECIMAL)".replace('@',order_by)
                else:
                    #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',col)
                    #print(box)
                    if len(value) and i != 'csrfmiddlewaretoken' and i in value or col == value[0]:
                        if i in box_3:
                            #print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
                            if value[-1]=='-1':
                                ColumnName+= f"({i} - {i.split('_')[-2]})"
                            else:
                                ColumnName+= f'{i},' 

                        elif col in box:
                            #print("dsfhgjsdhhsdbfshj")
                            ColumnName+= f'{i} as {col},' 
                        else:
                            #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                            ColumnName+= f'{i},' 

                        value[-1] = value[-1].lower() if type(value[-1]) == str and i!='Date' else value[-1]
                        value[-1] = value[-1].capitalize() if i=='Day' else value[-1]
                        # #print(i)
                        # #print(box_3)
                        # #print(i in box_3)

                        if 'Top_Record' in value or 'Bottom_Record' in value :

                            if len(value) == 3 and value[-1]:
                                Filter+=f'{i} = "{value[-2]}-{value[-1]}" and '
                            else:
                                
                                if len(value) == 2:
                                    if value[-1]:
                                        Filter+=f"substr({i}, 0, instr({i}, '-')) = '{value[-1]}' and "
                                else:
                                    pass

                        elif i not in box :
                            #print("worked")
                            print("valuevaluevaluevaluevalue",value)
                            if len(value) == 3:
                                if value[-2] == "p":
                                    Filter += f'{i}> 0 and '
                                elif value[-2] == 'n':
                                    Filter += f"({i} - {i.split('_')[-2]}) < 0 and "
                                elif value[-2] == 'z':
                                    Filter += f"{i} = 0 and "
                                Filter+=f'{i} = "{value[-1]}" and ' if len(value) == 3 and value[-1] else ''
                            else:
                                Filter+=f'{i} = "{value[-1]}" and ' if len(value) == 2 and value[-1] else ''
                                
                        else:
                            Filter+=f'{i} = "{value[-1]}" and ' if len(value) == 2 and value[-1] else ''

            else:
                pass

        ColumnName = ColumnName[:-1]

        Title = {}
        for i in ColumnName.split(',') :
            if ' as ' in i:
                print("worked")
                i = i.split(' as ')[-1]
            if '_' in i:
                # #print((''.join(i[0].upper() for i in i.split('_')))
                Title[i] = ''.join(i[0].upper() for i in i.split('_'))
            else:
                Title[i] = i.upper()

        Filter = f" where {Filter[:-5]}" if Filter else ''
        #print("Filter",Filter)
        selectquery = open(r"C:\Users\Sankar Senthil\Documents\Daemon\ICONT\InCont\static\files\selectquery.txt",'r').read()
        print(selectquery.replace('columns',ColumnName) + Filter + " order by substr(date,7)||substr(date,1,2)||substr(date,4,2) DESC;" )
        selectdata = cursor.execute(selectquery.replace('columns',ColumnName) + Filter + " order by substr(date,7)||substr(date,1,2)||substr(date,4,2) DESC;").fetchall()

        context = {"ColumnName":ColumnName.split(','),'selectdata':selectdata,'Title':Title}

        return render(requests, 'naccapp/result-page.html', context)
    return render(requests, 'naccapp/dash-board.html', context)

def result_page(requests,context):
    return render(requests, 'naccapp/result-page.html', context)