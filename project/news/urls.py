from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetails, PostCreate, PostDelete, PostUpdate


urlpatterns = [

   path('', PostsList.as_view()),
   path('<int:pk>', PostDetails.as_view()),
   path('post/<int:pk>/', PostDetails.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name="post_create"),
   path('news/create/', PostCreate.as_view(), name="news_create"),
   path('<int:pk>/update/', PostUpdate.as_view(), name="post_update"),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name="post_update"),
   path('<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),
   path('news/<int:pk>/update/', PostDelete.as_view(), name="news_delete"),
]