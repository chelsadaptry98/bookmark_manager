from django.shortcuts import render,redirect
from .models import Customer,Bookmark,CustomerBookmark
from .forms import CustomerBookmarkForm,BookmarkForm
import geopy.distance
# Create your views here.
def createWithNewBookmark(request,name):
   
    if request.method == "POST":
        book_form=BookmarkForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            book_title=(book_form.cleaned_data.get('title'))
            bookmark=Bookmark.objects.filter(title__iexact = book_title ).first()
            CustomerBookmark.objects.create(customer=Customer.objects.filter(name=name).first(),bookmark=bookmark)

    book_form=BookmarkForm()
    return render(request,"customer/create.html",{'form' : book_form })


def createWithExistingValues(request):

    if request.method == "POST":
        cust_book_form = CustomerBookmarkForm(request.POST)
        if cust_book_form.is_valid():
                cust_book_form.save()
    cust_book_form = CustomerBookmarkForm()    
    return render(request,"customer/create.html",{'form' : cust_book_form})

cbs=CustomerBookmark.objects.all()
def browse(request):
    valid=1
    global cbs
    if request.method == "POST" and 'cid' in request.POST:
        cid=Customer.objects.filter(pk=int(request.POST['cid'])).first()
        cbs=CustomerBookmark.objects.filter(customer=cid)
        if(not cid):
            valid=0
        return render(request,"customer/browse.html" , { 'cbs' : cbs, 'valid':valid , 'alert_msg' : "Invalid Customer ID"})
    
    elif request.method == "POST" and 'source_name' in request.POST:
        bookmark=Bookmark.objects.filter(source_name=request.POST['source_name'])
        cbs=CustomerBookmark.objects.filter(bookmark__in=bookmark)
        if(not bookmark):
            valid=0
        return render(request,"customer/browse.html" , { 'cbs' : cbs , 'valid':valid , 'alert_msg' : "No Bookmarks Found "})
    
    elif request.method == "POST" and 'title' in request.POST:
        bookmark=Bookmark.objects.filter(title__icontains=request.POST['title'])
        cbs=CustomerBookmark.objects.filter(bookmark__in=bookmark)
        if(not bookmark):
            valid=0
        return render(request,"customer/browse.html" , { 'cbs' : cbs , 'valid':valid , 'alert_msg' : "No Bookmarks Found"})

    elif request.method == "POST" and 'radius' in request.POST :
        origin=(request.POST['position_0'] , request.POST['position_1'])
        radius=int(request.POST['radius'])
        cid=[]
        for customer in Customer.objects.all():
            dest=(customer.position.latitude, customer.position.longitude)
            if(geopy.distance.distance(origin,dest) < radius):
                cid.append(customer)
        if(not cid):
            valid=0
        cbs=CustomerBookmark.objects.filter(customer__in=cid)
        return render(request,"customer/browse.html" , { 'cbs' : cbs , 'valid':valid , 'alert_msg' : "No Bookmarks Found" })
        
    elif request.method == "POST":
        print(request.POST)
        print(type(cbs))
        sortby=request.POST['sort']
        print(sortby)
        if(sortby == 'cid'):
            return render(request,"customer/browse.html" , { 'cbs' : cbs.order_by('customer__id') })
        if(sortby == 'cname'):
            return render(request,"customer/browse.html" , { 'cbs' : cbs.order_by('customer__name') })
        if(sortby == 'title'):
            return render(request,"customer/browse.html" , { 'cbs' : cbs.order_by('bookmark__title') })
        if(sortby == 'source_name'):
            return render(request,"customer/browse.html" , { 'cbs' : cbs.order_by('bookmark__source_name') })

    return render(request,"customer/browse.html")
    