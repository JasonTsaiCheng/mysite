#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.db import models

from models import UserInfo
#def index(request):
	#return render(request,'index.html')


def index(request):
    return render(request, 'index.html')

def orbis(request):
    return render(request, 'orbis.html')


def add(request):
    a = request.GET['a']
    return HttpResponse(a)

def show(request):
    if request.method == 'POST':
    	a_user = request.POST['a_user']
    	a_pwd = request.POST['a_pwd']
    	UserInfo.objects.create(user=a_user,pwd=a_pwd) #this is addMethod
    
    user_list = UserInfo.objects.all()
    return render(request,'show.html',{'user_list':user_list})

    
def doLogin(request):
      if request.method =='POST':
         username = request.POST.get('name')
         pwd = request.POST.get('password')
         if username =='lisi' and pwd == '12345':
              request.session['IS_LOGIN'] = True      # 设置session
              return redirect('index.html')
      else:
  
          return render(request,'orbis.html')


def datasave(request):
  tem_dic = json.loads(request.body)
  username = tem_dic["username"]
  password = tem_dic["password"]
  return HttpResponse(username)
  

def showjason(request):

  return render(request, 'jason.html')
# Create your views here.
