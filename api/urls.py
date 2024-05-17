from django.urls import path                                                                          
from .views import TaskList
urlpatterns = [
    path('post/' , TaskList.as_view() ),
    path('delete/<int:pk>/' , TaskList.as_view() ),
    path('put/<int:pk>/' , TaskList.as_view()  ),
    path('get/<int:pk>/' , TaskList.as_view()),
    path('get_model/<model>/' , TaskList.as_view()),
    path('get_narx/<int:pk>/' , TaskList.as_view()),
    path('get_yil/<int:pk>/' , TaskList.as_view()),
    path('get_rang/<rang>/' , TaskList.as_view()),
    path('get_min_max/<int:pk>/' , TaskList.as_view()),
    path('get/<int:pk>/' , TaskList.as_view()),
    path('get/<int:pk>/' , TaskList.as_view()),
    path('get/<int:pk>/' , TaskList.as_view()),
    
]