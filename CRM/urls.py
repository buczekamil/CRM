from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from Clients import views
from Clients.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers_list/', views.CustomersListView),
    path('add_customer/', views.CustomerAddView.as_view()),
    path('edit_customer/<pk>', views.CustomerUpdateView.as_view()),
    path('delete_customer/<pk>', views.CustomerDeleteView.as_view()),
    path('', TemplateView.as_view(template_name='basic_page.html'), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('Accounts.urls')),
    path('calendar/', include('Calendar.urls')),
    ### Product
    path('products_list/', views.ProductsListView),
    path('add_product/', views.ProductAddView.as_view()),
    path('edit_product/<pk>', views.ProductUpdateView.as_view()),
    path('delete_product/<pk>', views.ProductDeleteView.as_view()),
    ### Order
    path('orders/', views.OrdersListView),
    path('add_order/', views.OrderAddView.as_view()),
    path('edit_order/<pk>', views.OrderEditView.as_view()),
    path('order/<int:id>/', views.OrderAddLinesView.as_view()),
    path('delete_line/<pk>', views.OrderLineDeleteView.as_view()),
    path('pdf_generate/<int:id>', views.PDF_render_view.as_view()),

    path('map/', TemplateView.as_view(template_name='map.html'), name='map'),
]
