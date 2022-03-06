import sqlite3 as sq, os
from django.shortcuts import render, redirect
from threading import Thread
from . import scrapy

# Create your views here.

global ColumnName, Filter


# Thread(target=scrapy.scraper_func).start()
    
def dashboard(requests):
    global ColumnName, Filter
    ColumnName = ''
    Filter = ''
    connection = sq.connect(r"C:\Users\Sankar Senthil\Documents\Daemon\ICONT\InCont\basketball.db")  # connect to your DB
    cursor = connection.cursor()
    data=cursor.execute('''SELECT * FROM s20_21 WHERE ID=1''')
    data = [ column[0] for column in data.description ]

    box = [
            'Day',
            'Date']

    box_1 = [
            'Top_Team',
            'Top_Site_Value',
            'Top_boxscore_1',
            'Top_boxscore_2',
            'Bottom_Team',
            'Bottom_Site_Value',
            'Bottom_boxscore_1',
            'Bottom_boxscore_2',
            'Top_Current_Game_Score',
            'Top_Record_Difference',
            'Top_Record',
            'top_number_of_previous_games_played',
            'Bottom_Current_Game_Score',
            'Bottom_Record_Difference',
            'Bottom_Record',
            'Bottom_number_of_previous_games_played',
            
            'Record_Diffence_Differential',
            'Wins_Last_8_games_differential']

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
    box_3 = [box_3[i:i+4] for i in range(0, len(box_3), 4)]
    context = {'names':names,'box_2':box_2,'box_3':box_3,"box":box}
    if requests.method == 'POST':
        Ddata = dict(requests.POST)
        for i in Ddata:
            value = Ddata[i]
            try:
                value.remove('')
            except:pass
            if i == 'Record':
                order_by = 'Top_Record' if value[0] == 'Top_Record' else 'Bottom_Record'
                order_by = "Cast(substr(@, 0,instr(@, '-'))AS DECIMAL), Cast(substr(@, 3,instr(@, '-')) AS DECIMAL)".replace('@',order_by)
            else:
                if len(value) and i != 'csrfmiddlewaretoken':
                    ColumnName+= f'{i},' 

                    value[-1] = value[-1].lower() if type(value[-1]) == str and i!='Date' else value[-1]
                    value[-1] = value[-1].capitalize() if i=='Day' else value[-1]

                    print(value)
                    if 'Top_Record' in value or 'Bottom_Record' in value :

                        if len(value) == 3 and value[-1]:
                            Filter+=f'{i} = "{value[-2]}-{value[-1]}" and '
                        else:
                            
                            if len(value) == 2:
                                if value[-1]:
                                    Filter+=f"substr({i}, 0, instr({i}, '-')) = '{value[-1]}' and "
                            else:
                                pass


                    elif i in ['Top_Streak','Bottom_Streak','Streak_Differential']:
                        try:
                            if int(value[-1]) > 0:
                                Filter += f'Cast({i} AS Decimal) > 0 and '
                            elif int(value[-1]) < 0:
                                Filter += f'Cast({i} AS Decimal) < 0 and '
                            else:
                                Filter += f'Cast({i} AS Decimal) = 0 and '
                        except:
                            Filter += ''
                            
                    else:
                        Filter+=f'{i} = "{value[-1]}" and ' if len(value) == 2 and value[-1] else ''

        ColumnName = ColumnName[:-1]

        Title = {}
        for i in ColumnName.split(',') :
            if '_' in i:
                # print((''.join(i[0].upper() for i in i.split('_')))
                Title[i] = ''.join(i[0].upper() for i in i.split('_'))
            else:
                Title[i] = i.upper()

        Filter = f" where {Filter[:-5]}" if Filter else ''
        print("Filter",Filter)
        selectquery = open(r"C:\Users\Sankar Senthil\Documents\Daemon\ICONT\InCont\static\files\selectquery.txt",'r').read()
        print(selectquery.replace('columns',ColumnName)+ Filter + " order by Cast(date AS Date) DESC;" )
        selectdata = cursor.execute(selectquery.replace('columns',ColumnName) + Filter + " order by substr(date,7)||substr(date,1,2)||substr(date,4,2) DESC;").fetchall()
       
        context = {"ColumnName":ColumnName.split(','),'selectdata':selectdata,'Title':Title}
        
        # print(ColumnName)

        # df = pd.DataFrame(context)
        # df.to_csv('f"{os.getcwd()}/static/files/')

        return render(requests, 'naccapp/result-page.html', context)
    return render(requests, 'naccapp/dash-board.html', context)

def result_page(requests,context):
    return render(requests, 'naccapp/result-page.html', context)