from django.urls import path
from customer  import views
from customer.views import successview,CancelView



urlpatterns = [
    path('customerhome',views.customerhome,name='customerhome'),
    path('details/<int:id>',views.details,name='details'),
    path('add_cart',views.add_cart,name='add_cart'),
    path('cartview',views.cartview,name='cartview'),
    path('plus/<int:id>',views.plus,name='plus'),
    path('minus/<int:id>',views.minus,name='minus'),
    path('delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
    path('summary',views.summary,name='summary'),

    path('create_checkout_session/',views.create_checkout_session,name="create_checkout_session"),
    path('checkout_success/',successview.as_view(),name="checkout_success"),
    path('checkout_cancel/',CancelView.as_view(),name="checkout_cancel"),
    

   
]