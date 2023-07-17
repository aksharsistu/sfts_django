from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('stage/', include('stage.urls')),
    path('data/', include('data.urls')),
    path('process/', include('process.urls'))
]
