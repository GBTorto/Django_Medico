from django.contrib import admin
from app_medico.models import *
from app_especialidade import *
from accounts.models import *
# Register your models here.

admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(UserProfile)