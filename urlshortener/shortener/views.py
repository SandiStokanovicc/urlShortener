from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        newUrl = Url(link=url, short=uid);
        newUrl.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(short=pk)
    return redirect(url_details.link)