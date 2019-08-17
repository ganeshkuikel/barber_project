from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from pages.models import Barbers, Opening, Appointment, Services, Feedback


def index(request):
    barbers=Barbers.objects.all()
    context={
        'barbers':barbers
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')

def appointment(request):
    openings=Opening.objects.all
    context={
        'openings':openings
    }
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone=request.POST['phone']
        time=request.POST['time']
        date=request.POST['date']
        details=request.POST['comments']
        appointment=Appointment(first_name=first_name,last_name=last_name,email=email,phone=phone,time=time,date=date,more_details=details)
        appointment.save()
        messages.success(request,'Your appointment has been booked')
        return redirect('appointment')
    return render(request,'pages/appointment.html',context)

def services(request):
    services=Services.objects.all()
    context={
        'services':services
    }
    return render(request,'pages/services.html',context)

def barbers(request):
    # linkings=Linking.objects.all
    # context1={
    #     'linkings':linkings
    # }
    barbers = Barbers.objects.all
    context = {
        'barbers': barbers
    }
    return render(request,'pages/barbers.html',context)
def contact(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone=request.POST['phone']
        feedback=request.POST['comments']
        contact = Feedback(first_name=first_name, last_name=last_name, email=email, phone=phone,more_details=feedback)
        contact.save()
        messages.success(request, 'Your feedback has been posted')
        return redirect('contact')
    return render(request,'pages/contact.html')