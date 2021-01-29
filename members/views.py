# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Members, product


#수정 했습니다,,이미지는 조금 안 맞을 수 있어서 내일 서버 돌리고 다시 수정 조금 해야할 것 같아요!

def index(request):
    mess={}
    mess['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        mess['login_color']='red'
        
    data = product.objects.all()
    page = request.GET.get('page',1)
    
    paginator = Paginator(data, 8)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    mess['lists']=lists
    mess['index']='ALL'
    mess['num']='37 items'
    return render(request, "project.html", mess)

#세부 index
def index_rice(request):
    mess={}
    mess['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        mess['login_color']='red'
    
    list_rice = product.objects.filter(type='rice')
    page = request.GET.get('page',1)
    
    paginator = Paginator(list_rice, 8)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    mess['lists']=lists
    mess['index']='샐러드/간편식'
    mess['num']='8 items'
    return render(request, "index.html", mess)

def index_meat(request):
    mess={}
    mess['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        mess['login_color']='red'
        
    list_meats=product.objects.filter(type='meat')
    page = request.GET.get('page',1)
    
    paginator = Paginator(list_meats, 8)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    mess['lists']=lists
    mess['index']='고기류'
    mess['num']='8 items'
    return render(request, "index.html", mess)

def index_snack(request):
    mess={}
    mess['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        mess['login_color']='red'
        
    list_snack=product.objects.filter(type='snack')
    page = request.GET.get('page',1)
    
    paginator = Paginator(list_snack, 8)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    mess['lists']=lists
    mess['index']='과자'
    mess['num']='8 items'
    return render(request, "index.html", mess)

def index_fruits(request):
    mess={}
    mess['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        mess['login_color']='red'
        
    list_fruits=product.objects.filter(type='fruits')
    page = request.GET.get('page',1)
    
    paginator = Paginator(list_fruits, 8)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    mess['lists']=lists
    mess['index']='과일류'
    mess['num']='8 items'
    return render(request, "index.html", mess)

def bot(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='음료'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)

def bak(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='베이커리'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)
def fish(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='어패류'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)
def egg(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='계란류'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)
def veg(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='채소류'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)
def rice2(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='즉석밥'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)
def freeze(request):
    list={}
    list['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        list['login_color']='red'
        
    list['index']='냉동식품'
    list['num']='차후 업데이트 예정입니다.'
    return render(request, "index.html", list)
def all(request):
    mess={}
    mess['login_color']='black'
    user_id = request.session.get('user') 
    
    if user_id:
        mess['login_color']='red'
        
    list = product.objects.all()
    page = request.GET.get('page',1)
    
    paginator = Paginator(list, 8)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    mess['lists']=lists
    mess['index']='ALL'
    mess['num']='37 items'
    return render(request, "index.html", mess)

# footer url
def shipment(req):
    list={}
    list['login_color']='black'
    user_id = req.session.get('user') 
    
    if user_id:
        list['login_color']='red'
    list['index'] ='배송조회'
    return render(req, "shipment.html", list)

def introduction(req):
    list={}
    list['login_color']='black'
    user_id = req.session.get('user') 
    
    if user_id:
        list['login_color']='red'
    list['index']='about us'
    return render(req, "introduction.html",list)

def foruser(req):
    list={}
    list['login_color']='black'
    user_id = req.session.get('user') 
    
    if user_id:
        list['login_color']='red'
    return render(req, "foruser.html", list)

def howto(req):
    list={}
    list['login_color']='black'
    user_id = req.session.get('user') 
    
    if user_id:
        list['login_color']='red'
    return render(req, "howto.html", list)

def guide(req):
    list={}
    list['login_color']='black'
    user_id = req.session.get('user') 
    
    if user_id:
        list['login_color']='red'
    return render(req, "guide.html", list)

#로그인

def login(req):
    if req.session.get('user'):
        del(req.session['user'])
        return redirect('/store')
    
    err = {}
    err['login_color'] = 'black'
    if req.method== 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        userid = req.POST.get('userid', None)
        userpassword = req.POST.get('userpassword', None)

        if not (userid and userpassword) :
            err['err'] = '입력이 안 된 사항이 있습니다.'
            return render(req, 'login.html', err)
        elif Members.objects.filter(userid = userid).exists():
            member = Members.objects.get(userid=userid)
            
            if userpassword == member.userpassword :
                req.session['user'] = member.userid
                err['login_color'] = 'red'
                return redirect('/store')
            else:
                err['err'] = "비밀번호가 잘못되었습니다."
                return render(req, "login.html", err)
        else:
            err['err']="다시입력해주세요."
            return render(req, "login.html", err)

    return render(req, "login.html", err)
    
#회원가입
def signup(req):
    err={}
    
    if req.method == 'POST':
        userid = req.POST['userid']
        userpassword = req.POST['userpassword']
        useremail = req.POST['useremail']
        pwck = req.POST['pwck']
        
        if not (userid and userpassword and useremail):
            err['err'] = '입력이 안 된 사항이 있습니다.'
            return render(req, 'signup.html', err)
        elif Members.objects.filter(userid = userid).exists():
            err['err3'] = '존재하는 아이디입니다.'
            return render(req, 'signup.html', err)
        else:
            if pwck != userpassword: 
                err['err2'] = '비밀번호가 일치하지 않습니다..'
                return render(req, 'signup.html', err)
            else :
                member = Members(
                    userid = userid,
                    userpassword = userpassword,
                    useremail = useremail
                )

                member.save()
                err['err'] = '등록 되었습니다.'
        
    return render(req, "signup.html", err)
