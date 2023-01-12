from django.shortcuts import render,HttpResponse,redirect
from libapp.models import Tickit
from django.db.models import Q
from libapp.forms import StudentForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from libapp.forms import UserForm
from django.contrib.auth import authenticate,login,logout
# from libapp.forms import UserForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')    

def borrow(request):
    userid=request.user.id
    if request.method == "POST":
        b=request.POST['btitle']
        c=request.POST['cat']
        # i=request.POST['isbn']
        a=request.POST['Aname']
        # at=request.POST['pactive']

        
        p=Tickit.objects.create(btitle=b,cat=c,Aname=a,is_deleted='1',uid=userid)
        # print(p)
        p.save()
        return redirect('/udash')

    else:

          return render(request,'borrow.html')

def udash(request):
    # rec=Tickit.objects.all()
    # print(rec)
    userid=request.user.id
    q1=Q(is_deleted=1)
    q2=Q(uid=userid)
    rec=Tickit.objects.filter(q1 & q2)
    
    content={}
    content['data']=rec
    return render(request,'udash.html',content)

def delete(request,rid): 
    # is_del
    # p.delete() 
    p=Tickit.objects.filter(id=rid)
    p.update(is_deleted='0')

    return redirect('/udash')  

def edit(request,rid):
    if request.method=='POST':
       ubtitle=request.POST['btitle']
       ucat=request.POST['cat']
    #    uisbn=request.POST['isbn']
       uaname=request.POST['Aname']

       p=Tickit.objects.filter(id=rid)
       p.update(btitle=ubtitle,cat=ucat,Aname=uaname)

       return redirect('/udash')
       

    else:
        p=Tickit.objects.get(id=rid) 
        content={}
        content['data']=p
        return render(request,'edit.html',content)   




def catfilter(request,catopt):
    q1=Q(cat=catopt)
    q2=Q(is_deleted=1)
    rec=Tickit.objects.filter(q1 & q2)
    content={}
    content['data']=rec

    return render(request,'udash.html',content)  

def authfilter(request,authopt):
    q1=Q(Aname=authopt)
    q2=Q(is_deleted=1)

    rec=Tickit.objects.filter(q1 & q2)
    content={}
    content['data']=rec

    return render(request,'udash.html',content) 


def djangoform(request):

    fm=StudentForm()
    content={}
    content['form']=fm
    return render(request, 'djangoform.html',content)    

def user_singUp(request):
    if request.method=='POST':
        # fm=UserCreationForm(request.POST)
        fm=UserForm(request.POST)
        if fm.is_valid():
            fm.save()

            return redirect('/Login')
        else:
            return HttpResponse("Failed to Create an User")    
    else:
        fm=UserForm()
        content={}
        content['form']=fm
        return render(request, 'singUp.html',content)    


def user_Login(request):

    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        # print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']

            u=authenticate(username=uname,password=upass)

            if u:
                login(request,u)
                return redirect("/udash")

            else:
                content={}
                content['data']="Invalid username and password"
                content['form']=fm
                return render()    
    else:
        fm=AuthenticationForm()
        content={}
        content['form']=fm
        
        return render(request,'Login.html',content)

def user_logout(request):

    logout(request)

    return redirect('/')        
    
