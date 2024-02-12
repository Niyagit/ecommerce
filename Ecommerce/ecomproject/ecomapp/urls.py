from django.urls import include, path
from . import views
from .views import allproductcat
app_name='ecomapp'

urlpatterns = [
    
    path('',views.allproductcat,name="allproductcat"),
    path('<slug:c_slug>/',views.allproductcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='procatdetail'),

]