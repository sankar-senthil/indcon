import json , os
from django.shortcuts import render

# Create your views here.


class Incont:
    def indecont(requests):
        # print(os.getcwd().replace().remove('InCont'))
        
        jsondata = json.load(open(f"{os.getcwd()}/static/files/DD.json",))
        return render(requests, 'InCon-home.html', jsondata)