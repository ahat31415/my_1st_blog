from django.http import Http404, HttpResponse
import datetime
#from django.template import Template, Context
from django.template import *
from django.shortcuts import *#render
from django.template.loader import *  #get_template


#777 - 888 - 999


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    dic = {'current_date': now}
    t = get_template("current_datetime.html")
    html = t.render(dic)
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dic = {'hours': offset,
           'time': dt
           }
    return render(request, 'mytemplate.html', dic)


def experiments(request):
    t = Template("Привет, {{ name }}")
    something = t.render(Context({"name": "Джон"}))

    return HttpResponse(something)
