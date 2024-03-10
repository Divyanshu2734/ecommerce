from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name='index' ),
    path('contact/',views.contact,name='contact' ),
    path('collections/',views.collections,name='collections' ),
    path('subcribe/',views.subscribe,name='suscribe' ),
    path('blog/',views.blogs,name='blog' ),
    path('payment/',views.payment,name='payment' )
]