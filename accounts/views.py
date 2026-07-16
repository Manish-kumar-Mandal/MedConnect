from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Contact
from .models import Appointment
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Welcome to Medconnect. ")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        number = request.POST.get("number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match. ")
            return redirect("register")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. ")
            return redirect("register")
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request,"Account Created Successfully. ")
        return redirect("login")
    return render(request, 'register.html')



@never_cache
@login_required(login_url='login')
def home(request):
    return render(request, "index.html")

def logout_page(request):
    logout(request)
    return redirect("login")


@never_cache
@login_required(login_url='login')
def doctors_page(request):
    return render(request, "all_doctors.html")





@never_cache
@login_required(login_url='login')
def doctor_profile_page(request):
    return render(request, "doctor_profile.html")


@never_cache
@login_required(login_url='login')
def appointment(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")
        reason = request.POST.get("reason")

        Appointment.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason
        )
        messages.success(request, "Your appointment has been booked successfully! Doctor will connects with you on the time,Thankyou")

        return redirect("bookappointment")

    return render(request, "book_appointment.html")



def forgot_page(request):
    return render(request, "forgotpass.html")



@never_cache
@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")