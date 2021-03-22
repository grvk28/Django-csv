from django.urls import path,re_path
from . import views
from .views import ( 
                    index,
                    add,
                    update,
                    delete,
                    i,
                    index1
                    #index,video_watch_view,liked_video,dislike_video,subscriber_view,video_comment, 
                   )


urlpatterns=[
   path('', i, name="home1"),
   path('index', index, name="home"),
   path('accounts/profile/',index,name="home2"),    
   path("add", add, name="edit"),
   path("edit/<int:pk>", views.update.as_view(), name="update"),
   path("delete/<int:id>/", delete, name="home3"),
   path("filter",views.filter,name="j")
]
