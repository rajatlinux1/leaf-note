from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls'))
]


handler404 = 'App.views.NotFound_404'
handler500 = 'App.views.InternalServerError_500'
handler403 = 'App.views.Forbidden_403'
handler400 = 'App.views.BadRequest_400'
