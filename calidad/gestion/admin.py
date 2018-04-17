# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User,Person,Question,Answer
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)