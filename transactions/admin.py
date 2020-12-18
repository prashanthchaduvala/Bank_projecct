from django.contrib import admin

from .models import Diposit, Withdrawal
# Register your models here.

admin.site.register(Diposit)
admin.site.register(Withdrawal)

