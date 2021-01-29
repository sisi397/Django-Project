# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Members
from .models import product


class MembersAdmin(admin.ModelAdmin):
    list_display = ('userid', 'userpassword', 'useremail')
    pass

admin.site.register(Members)

class productAdmin(admin.ModelAdmin):
    list_display = ('food', 'price', 'images', 'type')
    pass

admin.site.register(product, productAdmin)