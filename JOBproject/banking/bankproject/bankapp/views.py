from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegionCreationForm

# Create your views here.
from .models import District, City, Region, Field


def demo(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/account/')
        else:
            messages.error(request, 'Login Failed! Invalid username and password')
            return redirect('/login/')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', )
        password = request.POST.get('password', )
        cpassword = request.POST.get('cfpassword', )
        if password == cpassword:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print("user created")
            return redirect('/login/')
        else:
            print('Invalid password')

    return render(request, 'register.html')


def account(request):
    form = RegionCreationForm()
    if request.method == "POST":
        form = RegionCreationForm(request.POST)
        if form.is_valid():
            form.save()

        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            if request.method == "POST":
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                field = Field(email=email, phone=phone)
                field.save()
            return redirect('/submit/', {'result': field})
        else:
            messages.error(request, 'Application Submission Failed! Invalid username')
        return redirect('/account/')

    return render(request, 'account.html', {'form': form})


def submit(request):
    obj={}
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        obj = Field.objects.filter(email=email, phone=phone)
    return render(request, 'message.html', {'result': obj})


# AJAX
def load_cities(request):
    district = request.GET.get('district')
    cities = City.objects.filter(district=district).all()
    return render(request, 'city.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
