from django.urls import path
from bookapp import  views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),

    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:dataid>',views.editcategory,name="editcategory"),
    path('updatecategorye/<int:dataid>', views.updatecategorye, name="updatecategorye"),
    path('deletecategory/<int:dataid>', views.deletecategory, name="deletecategory"),

    path('genres/', views.genres, name="genres"),
    path('savegenres/', views.savegenres, name="savegenres"),
    path('displaygenres/', views.displaygenres, name="displaygenres"),
    path('deletegenres/<dataid>/', views.deletegenres, name="deletegenres"),


    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>', views.deleteproduct, name="deleteproduct"),
    path('cartdisplay/', views.cartdisplay, name="cartdisplay"),
    path('deletecart/<int:dataid>', views.deletecart, name="deletecart"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

]