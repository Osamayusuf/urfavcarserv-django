from django.urls import path
from Urfavcarserv import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('booking/', views.booking, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error404, name='error404'),
    path('newsletter/', views.newsletter_signup, name='newsletter'),
]