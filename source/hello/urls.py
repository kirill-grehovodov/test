from django.contrib import admin
from django.urls import path
from webapp.views import article_create_view, article_update_view, article_delete_view, IndexView, ArticleView, IndexRedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index_view),
#     path('articles/add/', article_create_view),
#     # path('article/', article_view),
#     path('article/<int:pk>', article_view)
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexRedirectView.as_view(), name='article_index_redirect'),
    path('article/<int:pk>', ArticleView.as_view(), name='article_view'),
    path('articles/add', article_create_view, name='article_add'),
    path('article/<int:pk>/edit/', article_update_view, name='article_update'),
    path('article/<int:pk>/delete/', article_delete_view, name='article_delete')
]


