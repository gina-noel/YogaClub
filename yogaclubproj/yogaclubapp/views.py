from django.shortcuts import render, get_object_or_404
from .models import Schedule, Classes, Pricing, User
from django.urls import reverse_lazy
from .forms import ClassForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'yogaclubapp/index.html')

# all may not be a good idea if you have a lot! 
def schedule(request):
    schedule=Schedule.objects.all() 
    return render(request, 'yogaclubapp/schedule.html', {'schedule' : schedule})

def classes(request):
    classes_list=Classes.objects.all()
    return render(request, 'yogaclubapp/classes.html', {'classes_list':classes_list})
    
def classdetail(request, id):
    class_detail=get_object_or_404(Classes, pk=id)
    return render(request, 'yogaclubapp/classdetail.html', {'class_detail' : class_detail})

def pricing(request):
    pricing=Pricing.objects.all()
    return render(request, 'yogaclubapp/pricing.html', {'pricing':pricing})
    

@login_required  
def newClass(request):
     form=ClassForm
     if request.method=='POST':
          form=ClassForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ClassForm()
     else:
          form=ClassForm()
     return render(request, 'yogaclubapp/classes.html', {'form': form})
 

def loginmessage(request):
     return render(request, 'yogaclubapp/loginmessage.html')

def logoutmessage(request):
     return render(request, 'yogaclubapp/logoutmessage.html')