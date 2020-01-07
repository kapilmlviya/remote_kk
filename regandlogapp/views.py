from django.shortcuts import render
from regandlogapp.models import RegistrationData
from regandlogapp.form import RegistrationForm
from regandlogapp.form import LoginForm
from django.http.response import HttpResponse

def index(request):
    return render(request,'index.html')

def registration_views(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            uname = request.POST.get('username')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')

            gender = rform.cleaned_data.get('gender')
            dob = rform.cleaned_data.get('date_of_birth')

            data = RegistrationData(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=password,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=dob
            )
            data.save()
            rform = RegistrationForm()
            return render(request, 'registration.html', {'rform': rform})

        else:
                    return HttpResponse("User Missed values")
    else:
            rform = RegistrationForm()
            return render(request, 'registration.html', {'rform': rform})


def login_views(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname= request.POST.get('uname')
            pwd= request.POST.get('password')


            lform=LoginForm()

            return render(request, 'Login.html', {'lform': lform})
        else:
            return HttpResponse("User some Missed Value")
    else:
        lform = LoginForm()
        return render(request,'Login.html',{'lform':lform})










