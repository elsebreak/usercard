from django.urls import path

from .views import *

urlpatterns = [
    path('', cards_list, name='cards_list_url'),
    path('usercard/create/', CardCreate.as_view(), name='card_create_url'),
    path('usercard/<str:uniq>/', CardRead.as_view(), name='card_read_url'),
    path('usercard/<str:uniq>/update/', CardUpdate.as_view(), name='card_update_url'),
    path('usercard/<str:uniq>/delete/', CardDelete.as_view(), name='card_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:uniq>/', TagRead.as_view(), name='tag_read_url'),
    path('tag/<str:uniq>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:uniq>/delete/', TagDelete.as_view(), name='tag_delete_url')
]
