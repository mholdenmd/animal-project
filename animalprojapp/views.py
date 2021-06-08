from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")
# --------------------------------------------
# def index(request):
# 	return render(request, "index.html")
# --------------------------------------------


def index(request):
    return render(request, "loginreg.html")
# --------------------------------------------


def register(request):   # REGISTER NEW USER FUNCTION #
    error = User.objects.registrationvalidator(request.POST)
    print("*****", error)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")
    print(request.POST["firstname"])
    print("******")
    print(request.POST["lastname"])
    print("******")
    print(request.POST["email"])
    print("******")
    newuser = User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'], password=request.POST['password'], birthday=request.POST
                                  ['birthday'])
    request.session['loggedinuserid'] = newuser.id
    return redirect("/success")
# ------------------------------------------------


def success(request):  # SUCCESSFUL LOGIN FUNCTION / PAGE #
    context = {
        'loggedinuser': User.objects.get(id=request.session['loggedinuserid']),
        'pets': Pet.objects.all()
    }

    return render(request, "success.html", context)
# -----------------------------------------------


def login(request):  # LOGIN FUNCTION #
    print("*****test*****")
    print(request.POST)
    error = User.objects.loginvalidator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")
    matchingemail = User.objects.filter(email=request.POST['email'])
    request.session['loggedinuserid'] = matchingemail[0].id
    print("****", error)
    return redirect("/success")
# -----------------------------------------------


def logout(request):   # LOGOUT FUNCTION #
    request.session.clear()
    return redirect("/")
# -----------------------------------------------


def addpet(request):  # ADDS A PET #
    Pet.objects.create(
        name=request.POST['name'],
        breed=request.POST['breed'], age=request.POST['age'],
        foodtype=request.POST['foodtype'], sex=request.POST['sex'],
        description=request.POST['description'],
        owner=User.objects.get(id=request.session['loggedinuserid']))
    print(request.POST)
    return redirect("/success")
# -----------------------------------------------


def user(request, userid):
    context = {
        'loggedinuser': User.objects.get(id=request.session['loggedinuserid']),
        'userinformation': User.objects.get(id=userid),
        'petinformation': Pet.objects.all(),
        'appointment': Appointment.objects.all()

    }
    return render(request, 'user.html', context)


def makeappointment(request, userid):
    Appointment.objects.create(
        time=request.POST['time'],
        description=request.POST['description'],
        client=User.objects.get(id=request.session['loggedinuserid'])),
    print(request.POST)
    return redirect(f'/user/{userid}')
