from django import forms
from django.forms import ModelForm, TextInput, IntegerField, URLField
from django.core.exceptions import ValidationError

from .models import Customer,Bookmark,CustomerBookmark
cust_all=Customer.objects.all()
customers=[]
for c in cust_all:
    customers.append(c.name)

class CustomerBookmarkForm (ModelForm):
    class Meta:
        model = CustomerBookmark
        fields = '__all__'


class BookmarkForm (ModelForm):
    class Meta:
        model = Bookmark
        fields = '__all__'




