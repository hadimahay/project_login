
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import sendForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
# Create your views here.

def sinup(request):
    if request.method == 'POST':
        form = sendForm(request.POST)

        if form.is_valid():
            
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(username,email,password)


            return redirect('Sin:login')

    else:
        form = sendForm()
    
    return render(request,'sin/sinup.html')

@login_required( redirect_field_name =None, login_url='/')
def profile(request):
    return render(request,'sin/profile.html')

def home(request):
    return redirect('Sin:login')