from django.contrib import admin
from django.urls import path, include
from blog.views import home,category,post,category_page,what_we_do1,what_we_do2,what_we_do3,what_we_do4
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    # path('blog/<slug:url>', post),
    # path('category/', category_page, name='category_page'),  # New URL for category page
    # # url for what we do pages
    # path('category/<slug:url>',category),

    path('category/blog/<slug:url>', post, name='post'),  # Post detail page
    path('category/', category_page, name='category_page'),  # All categories page
    path('category/<slug:url>', category, name='category_detail'),  # Category detail page
    path('donate-to-educational-enpowerment-program/',what_we_do1),
    path('donate-to-moral-and-ethical-development/',what_we_do2),
    path('donate-to-mental-health-and-wellbeing-program/',what_we_do3),
    path('donate-to-cultural-enrichment-program/',what_we_do4),
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