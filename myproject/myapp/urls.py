from django.urls import path

from . import views
from .views import (AddProduct, Favorites, HomeView, Tags, comment_add,
                    favorite_add, favorite_delete)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tags/<slug:tag_slug>/', Tags.as_view(), name='tags'),
    path('chat/', views.chat, name='chat'),
    path('add_product/', AddProduct.as_view(), name='add_product'),
    path('comment_add<int:product_id>/', comment_add, name='comment_add'),
    path('favorite_add/<int:product_id>/', favorite_add, name='favorite_add'),
    path('favorite_delete/<int:favorite_id>/', favorite_delete, name='favorite_delete'),
    path('favorites/', Favorites.as_view(), name='favorites'),
]
