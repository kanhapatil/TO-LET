from django.contrib import admin
from .models import FlatOwner, AddFlat, UserModel, Contact

# REGISTER FLAT OWNER MODEL
admin.site.register(FlatOwner)

# REGISTER ADD FLAT MODEL
admin.site.register(AddFlat)

# REGISTER USER MODEL
admin.site.register(UserModel)

# REGISTER CONTACT US MODEL
admin.site.register(Contact)
