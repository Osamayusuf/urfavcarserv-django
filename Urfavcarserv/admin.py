from django.contrib import admin
from .models import Booking, Contact
# register your models here.
admin.site.register(Booking)
admin.site.register(Contact)
from .models import Booking, Contact, Newsletter

admin.site.register(Newsletter)