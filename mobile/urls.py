from django.urls import path
from django.shortcuts import render
from mobile.views import brand_view,brand_delete,brand_edit,mobile_create,list_mobiles,mobile_detail,user_registration,user_login,user_logout,cart,order_item,errorpg,mobile_edit,mobile_delete,cart_view,cart_cancel

urlpatterns = [
    path("error",errorpg,name="errorpage"),
    path("",lambda request:render(request,"mobile/index.html")),  # giving empty name link, will move direclty into html page by giving "...../mobile/"
    path("userRegistration",user_registration,name="register"),
    path("userlogin",user_login,name="userlogin"),
    path("userlogout",user_logout,name="userlogout"),

    path("brands",brand_view,name="brandview"),
    path("delete/<int:id>",brand_delete,name="branddelete"),
    path("edit/<int:id>",brand_edit,name="brandedit"),

    path("mobiles",mobile_create,name="mobilecreate"),
    path("mobiles/list",list_mobiles,name="listmobiles"),
    path("mobiles/edit/<int:id>",mobile_edit,name="mobileedit"),
    path("mobiles/delete/<int:id>",mobile_delete,name="mobiledelete"),
    path("mobiles/detail/<int:id>",mobile_detail,name="mobiledetail"),
    path("order/<int:id>",order_item,name="orderitem"),

    path("cart",cart,name="cartitems"),
    path("cartview/<str:name>",cart_view,name="cartview"),
    path("cartcancel/<int:id>",cart_cancel,name="cartcancel")

]