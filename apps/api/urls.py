from django.urls import path, include


urlpatterns = [
    path('user/', include('api.registration.urls')),
    path('order/', include('api.order.urls')),
]

