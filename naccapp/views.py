import sqlite3 as sq, os
from django.shortcuts import render, redirect

# Create your views here.

global ColumnName, Filter


    
def dashboard(requests):
    connection = sq.connect("basketball.db")  # connect to your DB
    cursor = connection.cursor()
    data=cursor.execute('''SELECT * FROM s20_21 WHERE ID=1''')
    data = [ column[0] for column in data.description ]

   

    global ColumnName, Filter
    ColumnName = ''
    Filter = ''
    try:
        data.remove('ID')
    except:pass
    order_by = 'twins,twins'
    names = [data[i:i+3] for i in range(0, len(data), 3)]
    context = {'names':names}
    if requests.method == 'POST':
        Ddata = dict(requests.POST)
        print(Ddata)
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
                                Filter+=f"substr({i}, 0, instr({i}, '-')) = '{value[-1]}' and "
                            else:
                                # Filter+=f"substr({i}, instr({i}, '-')+1) = '{}' and "
                            # else:
                            #     Filter+=''

                                pass

                        # Filter+=f'{i} = "{value[-2]}-{value[-1]}" and ' if len(value) == 3 and value[-1] else ''



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
        selectquery = open(f"{os.getcwd()}/static/files/selectquery.txt",'r').read()
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