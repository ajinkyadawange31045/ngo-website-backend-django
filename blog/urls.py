from django.contrib import admin
from django.urls import path, include
from blog.views import home,category,post,category_page
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post),
    path('category/', category_page, name='category_page'),  # New URL for category page
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('', home),
#     path('blog/<slug:url>', post),
#     path('about/',about),
#     path('category/<slug:url>',category),
#     path('search/', post_search, name="search"),
#     path('likes/<int:ids>', add_likes, name="likes"),
#     path('bookmark/<int:ids>', add_bookmark, name="bookmark")
# ]