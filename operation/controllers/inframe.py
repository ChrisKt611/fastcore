from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from operation.models.usermodels import User

def topbar(req):
	username = req.COOKIES.get('username','')
	return render_to_response('topbar.html',{'username':username})

def targeturl(req):
    if req.method == 'GET':
        rawpage = req.path
        pagename = rawpage[7:-1]
    return render_to_response('pagecontent.html',{'pagename':pagename})
