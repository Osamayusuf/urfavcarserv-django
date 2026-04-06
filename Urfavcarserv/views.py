from django.shortcuts import render, redirect
from .forms import BookingForm, ContactForm
from .models import Newsletter

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        else:
            # Form has errors, display them to user
            return render(request, 'contact.html', {'form': form, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            print(form.errors)  # ADD THIS LINE
            return render(request, 'booking.html', {'form': form})
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
def booking_success(request):
    return render(request, 'booking_success.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def error404(request):
    return render(request, '404.html')
from .models import Newsletter

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Newsletter.objects.get_or_create(email=email)
    return redirect(request.META.get('HTTP_REFERER', 'home'))
