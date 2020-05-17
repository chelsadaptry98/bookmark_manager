from django.contrib import admin

# Register your models here.
from .models import Customer,Bookmark,CustomerBookmark
admin.site.register(Bookmark)
admin.site.register(Customer)
admin.site.register(CustomerBookmark)