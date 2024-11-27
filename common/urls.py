from django.urls import path
from common  import views

urlpatterns = [
    path('',views.commonbase,name='commonbase'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('register',views.register,name='register'),
    path('userlogout',views.userlogout,name='userlogout')

]