from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('post',views.post,name='post'),
    path('',include('home.urls')),
    path('praduct',include('praduct.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls'))
]
