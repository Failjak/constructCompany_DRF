from django.urls import path, include


urlpatterns = [
    path('auth/', include('api.registration.urls')),
    path('order/', include('api.order.urls')),
    path('worker/', include('api.worker.urls')),
    path('itme/', include('api.item.urls')),
]

