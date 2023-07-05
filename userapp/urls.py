from django.urls import path
from userapp import views

urlpatterns=[
    path('',views.home,name="home"),
    path('product/<itemcat>/',views.product,name="product"),
    path('moreproduct/<itemcat>/',views.moreproduct,name="moreproduct"),
    path('genres/<itemcat>/',views.genres,name="genres"),
    path('singleproduct/<int:dataid>/', views.singleproduct, name="singleproduct"),
    path('cart/',views.cart,name="cart"),
    path('savecart/',views.savecart,name="savecart"),
    path('Deletecart/<dataid>/',views.Deletecart,name="Deletecart"),
    path('checkout/',views.checkout,name="checkout"),
    path('savecheckout/',views.savecheckout,name="savecheckout"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('usersavedata/',views.usersavedata,name="usersavedata"),
    path('userloginpage/',views.userloginpage,name="userloginpage"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('purchaseinfo/',views.purchaseinfo,name="purchaseinfo"),
    path('profile/',views.profile,name="profile"),
    path('allbooks/',views.allbooks,name="allbooks"),

]