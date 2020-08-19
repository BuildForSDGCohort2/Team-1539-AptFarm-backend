from django.contrib import admin
from procedures.models import *
from broiler.models import *
from layer.models import *

# Register your models here.


admin.site.register(Procedures)
admin.site.register(Vaccine)
admin.site.register(Drugs)
admin.site.register(Feed)
admin.site.register(Broiler)
admin.site.register(Layers)