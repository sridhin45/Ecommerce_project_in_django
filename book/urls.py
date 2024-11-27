from django.urls import path
from book import views

urlpatterns = [
    path('add_category',views.add_category,name='add_category'),
    path('categoryadd',views.categoryadd,name="categoryadd"),
    path('edit_ca/<int:id>',views.edit_ca,name='edit_ca'),
    path('delete_ca/<int:id>',views.delete_ca,name='delete_ca'),
    path('covertype',views.covertype,name='covertype'),
    path('add_cover',views.add_cover,name='add_cover'),
    path('edit_co/<int:id>',views.edit_co,name='edit_co'),
    path('delete_co/<int:id>',views.delete_co,name='delete_co'),
    path('product',views.product,name='product'),
    path('add_product',views.add_product,name='add_product'),
    path('edit_product/<int:id>',views.edit_product,name='edit_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('manageorder',views.manageorder,name='manageorder'),
    path('load_table',views.load_table,name='load_table'),
    path('cancel_order/<int:order_id>',views.cancel_order,name='cancel_order'),
    path('more_details/<int:id>',views.more_details,name='more_details'),
    path('processing',views.processing,name='processing'),
    path('ship_order',views.ship_order,name='ship_order'),


    
]