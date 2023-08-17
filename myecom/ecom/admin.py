from django.contrib import admin
from ecom.models import UserProfileInfo,BlogModel,Product,Orders

# Register your models here.

# register UserProfile and Blog Models
admin.site.register(UserProfileInfo)
admin.site.register(BlogModel)
admin.site.register(Product)
admin.site.register(Orders)
