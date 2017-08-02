#-*- coding:UTF-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def index(request):
	return render(request,"index.html")

#登录动作
def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)  #登录
			request.session['user'] = username #将session信息记录到浏览器
			response =  HttpResponseRedirect('/event_manage/')
			#response.set_cookie('user',username,3600)  #浏览器cookie	
			return response

		else:
			return render(request,'index.html',{'error':'username or password error!'})
			
#发布会管理
@login_required
def event_manage(request):
	#username = request.COOKIES.get('user','')   #读取浏览器cookie
	event_list = Event.objects.all()    #django读取数据库event表中的所有数据
	username = request.session.get('user','')    #读取浏览器session
	return render(request,"event_manage.html",{"user":username,"events":event_list})  #使用render方法，把username和even_list传给event_manage页面

#发布会名称搜索
@login_required
def search_name(request):
	username = request.session.get('user','')
	search_name = request.GET.get("name","") #使用GET方法接受搜索关键字 name属性的值
	event_list = Event.objects.filter(name__contains=search_name)  #传入查询条件然后用filter模糊查询去匹配数据库
	return render(request,"event_manage.html",{"user":username,"events":event_list})

#嘉宾管理
@login_required
def guest_manage(request):
	username = request.session.get('user','')
	guest_list = Guest.objects.all()   #取出所有Guest表的数据赋值给guest_list
	paginator = Paginator(guest_list,2)  #用Paginator方法将quest_list中的数据每页显示2条
	page = request.GET.get('page')       #通过GET请求得到当前要显示第几页的数据
	try:
		contacts = paginator.page(page)  #获取第page页的数据。如果当前没有页数，抛出异常，返回第一页的数据。如果超出最大页数范围，抛出异常，返回最后一页的数据。
	except PageNotAnInteger:
		#If page is not an integer,deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999),deliver last page of results
		contacts = paginator.page(paginator.num_pages)
	return render(request,"guest_manage.html", {"user": username, "guests": contacts})

#嘉宾名称搜索
@login_required
def search_p_name(request):
	username = request.session.get('user','')
	search_p_name = request.GET.get("realname","")
	guest_list = Guest.objects.filter(realname__contains=search_p_name)
	paginator = Paginator(guest_list,2)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request,"guest_manage.html",{"user":username,"guests":contacts})

#嘉宾电话搜索
@login_required
def search_phone(request):
	username = request.session.get('user','')
	search_phone = request.GET.get("phone","")
	guest_list = Guest.objects.filter(realname__contains=search_phone)
	paginator = Paginator(guest_list,2)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request,"guest_manage.html",{"user":username,"guests":contacts})

