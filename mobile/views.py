from django.shortcuts import render,redirect
from mobile.forms import BrandCreateForm,MobileCreateform,UserRegForm,Userorder
from mobile.models import Brands,Mobile,Order
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return wrapper

def admin_permission_required_id(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper

def user_only_id(func):
    def wrapper(request,id):
        if not request.user.is_superuser and request.user:
            return redirect("userlogin")
        else:
            return func(request,id)
    return wrapper

def user_only(func):
    def wrapper(request):
        if not request.user.is_superuser and request.user:
            return redirect("userlogin")
        else:
            return func(request)
    return wrapper

def errorpg(request):
    return render(request,"mobile/errorpage.html")



def user_registration(request):
    form = UserRegForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form = UserRegForm(request.POST)
            context["form"] = form
            return render(request,"mobile/userreg.html",context)
    return render(request,"mobile/userreg.html",context)

def user_login(request):
    if request.method=="POST":
        username = request.POST.get("uname")    # as we havnt created form, we are takig usernmae and password from html page by their name given in htmk page
        password = request.POST.get("pwd")
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if request.user.is_superuser: 
                return redirect("brandview")
            else:
                return redirect("listmobiles")
        else:
            return render(request,"mobile/userlogin.html")
    return render(request,"mobile/userlogin.html")

def user_logout(request):
    logout(request)
    return redirect("userlogin")



@admin_permission_required
def brand_view(request):
    form = BrandCreateForm()
    context = {}
    # to get all created brands also when posting form
    brands = Brands.objects.all()
    # adding to the context and add them in the html page also
    context["brands"] = brands
    # adding form to the context
    context["form"] = form
    if request.method == "POST":
        form = BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved")
            return redirect("brandview")
    return render(request,"mobile/brandcreate.html",context)

@admin_permission_required_id
def brand_delete(request,id):
    brand = Brands.objects.get(id=id)
    brand.delete()
    return redirect("brandview")

@admin_permission_required_id
def brand_edit(request,id):
    brand = Brands.objects.get(id=id)
    form = BrandCreateForm(instance=brand)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form = BrandCreateForm(request.POST,instance=brand)   # if instance is not given in post part, then new object will be created
        if form.is_valid():
            form.save()
            return redirect("brandview")
    return render(request,'mobile/brandedit.html',context)


def mobile_create(request):
    form = MobileCreateform()
    context = {}
    context["form"]= form
    if request.method=="POST":
        form=MobileCreateform(request.POST,files=request.FILES)  # for saving images, we should give files=request.FILES also
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("mobilecreate")
    return render(request,"mobile/mobilecreate.html",context)

def list_mobiles(request):
    mobiles = Mobile.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request,"mobile/mobilelist.html",context)

def mobile_edit(request,id):
    mobile = Mobile.objects.get(id=id)
    form = MobileCreateform(instance=mobile)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = MobileCreateform(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
    return render(request, 'mobile/mobileedit.html', context)

def mobile_delete(request,id):
    mobile = Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobiles")

def mobile_detail(request,id):
    mobile = Mobile.objects.get(id=id)
    context = {}
    context["mobile"] = mobile
    return render(request,"mobile/mobiledetail.html",context)

def order_item(request,id):
    product = Mobile.objects.get(id = id)
    username = request.user
    form = Userorder(initial={"product":product,"user":username})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = Userorder(request.POST)
        print("testpoint")
        if form.is_valid():
            print("testpoint get item")
            # product_name = form.cleaned_data.get("product")
            # product = Mobile.objects.get(model_name = product_name)
            # address = form.cleaned_data.get("address")
            # username = request.user
            # order = Order(product = product,address= address,user = username)
            # order.save()
            form.save()
            return redirect("cartitems")
        else:
            context["form"] = form
            return render(request, "mobile/orderitem.html", context)
    return render(request,"mobile/orderitem.html",context)

def cart(request):
    username = request.user
    orders = Order.objects.all().filter(user = username)
    print(orders)
    context = {}
    context["orders"] = orders
    return render(request,"mobile/cart.html",context)

def cart_view(request,name):
    mobile = Mobile.objects.get(model_name=name)
    context = {}
    context["mobile"] = mobile
    return render(request,"mobile/cartview.html",context)

def cart_cancel(request,id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect("cartitems")



    




