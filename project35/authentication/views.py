from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .form import ServiceProviderSignUpForm, ServiceUserSignUpForm


# Create your views here.
# def serviceuser_register(request):
#     return render(request,'authentication/serviceuser_register.html')

# def serviceprovider_register(request):
#     return render(request,'authentication/serviceprovider_register.html')

class serviceuser_register(CreateView):
    model = User
    form_class = ServiceUserSignUpForm
    template_name = "authentication/serviceuser_register.html"

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/')


class serviceprovider_register(CreateView):
    model = User
    form_class = ServiceProviderSignUpForm
    template_name = "authentication/serviceprovider_register.html"

    def form_valid(self, form):
        user = form.save()
       # login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'authentication/login.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')




# def login(request):
#     return render(request,'authentication/login.html')