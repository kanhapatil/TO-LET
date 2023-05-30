from django.contrib import admin
from .models import FlatOwner, AddFlat

# REGISTER FLAT OWNER MODEL
admin.site.register(FlatOwner)

# REGISTER ADD FLAT MODEL
admin.site.register(AddFlat)
