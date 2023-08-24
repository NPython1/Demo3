from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from webscraper_app.models import Links


# Create your views here.
def home(request):
    if request.method == "POST":
        link_name=request.POST.get('pagename','')
        urls=requests.get(link_name)
        bsoup=BeautifulSoup(urls.text,'html.parser')

        for i in bsoup.find_all('a'):
            li_address=i.get('href')
            li_name=i.string
            Links.objects.create(address=li_address,stringn=li_name)
        return HttpResponseRedirect('/')

    else:
        data=Links.objects.all()

    return render(request,"home.html",{'data':data})



