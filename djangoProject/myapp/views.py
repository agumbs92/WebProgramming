from datetime import datetime

from django.shortcuts import render

# Create your views here.
def home(requests):
    cur_time = datetime.now()
    context = {'time': datetime.now()}
    return render(requests, 'myapp/homepage.html', context=context)