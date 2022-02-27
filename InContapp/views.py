import json 
from django.shortcuts import render

# Create your views here.

class Incont:
    def indecont(requests):
        jsondata = json.load(open(r"static\files\DD.json",))
        return render(requests, 'InCon-home.html', jsondata)