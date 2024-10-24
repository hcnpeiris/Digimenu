from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('menu/<int:menu_id>/', views.menu_products, name='menu_products'),
    path('product/<int:product_id>/', views.product_info, name='product_info'),
    path('addproduct/', views.add_product, name='add_product'),
    path('addmenu/', views.add_menu, name='add_menu'),
    path('chanegmenu/<int:menu_id>', views.change_menu, name='change_menu'),
    path('menu/delete/<int:menu_id>/', views.delete_menu, name='delete_menu'),
    path('qr/<int:resturant_id>/', views.generate_qr_code, name='qr'),
    path('orders/', views.pending, name='orders'),
    path('orders/approved/', views.approved, name='approved'),



]
