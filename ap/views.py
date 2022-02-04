from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import user,male,female

# Create your views here.
def home(request):
    return render(request,'form1.html')
def chk(request):
    
    if(request.method=='POST'):
        gender = request.POST['gender']
        mail=request.POST['email']
        ob_user=user()
        ob_user.f_name=request.POST['first_name']
        ob_user.l_name=request.POST['last_name']
        ob_user.password=request.POST['password']
        ob_user.gender=request.POST['gender']
        ob_user.email=request.POST['email']
        ob_user.phone=request.POST['phone']
        ob_user.save()
        if(gender=='Male'):
            response = render(request,'male.html')
            response.set_cookie(key='mail', value=mail)
            response.set_cookie(key='gender', value='male')
            return response
        else:
            response = render(request,'female.html')
            response.set_cookie(key='mail', value=mail)
            response.set_cookie(key='gender', value='female')
            return response
        
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
def fav(request):
    if(request.method=='POST'):
        if(request.COOKIES.get('gender')=='male'):
            ob_male=male()
            ob_male.email=request.COOKIES.get('mail')
            ob_male.favourite_game=request.POST['fg']
            ob_male.favourite_sports_person=request.POST['fsp']
            ob_male.save()
            return HttpResponse("added !!")
            

        elif(request.COOKIES.get('gender')=='female'):
            ob_female=female()
            ob_female.email=request.COOKIES.get('mail')
            ob_female.favourite_color=request.POST['fc']
            ob_female.favourite_beauty_brand=request.POST['fbb']
            ob_female.favourite_beauty_product=request.POST['fbp']
            ob_female.save()
            return HttpResponse("added !!")
            
        print("hiiii **************************************************"+request.COOKIES.get('mail'))
        fg=request.POST['fg']
        fsp=request.POST['fsp']
        return HttpResponse("Sorry page not found")
    
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
