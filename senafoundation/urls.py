"""
URL configuration for senafoundation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from gallery.views import home, details, addlike
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('gallery/',home, name="home"),
    # path('<int:image_id>',details, name="details"),
    # path('image_like/<int:id>',addlike, name="image_like"),
    # path('gallery_image/upload',views.image_upload, name="image-upload")
    # path('gallery_image/upload', user_passes_test(views.is_admin)(views.image_upload), name="image-upload"),
]
