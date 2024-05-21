from django.urls import path                                                                          
from .views import TaskList
urlpatterns = [
    path('post/' , TaskList.as_view() ),
    path('delete/<int:pk>/' , TaskList.as_view() ),
    path('put/<int:pk>/' , TaskList.as_view()  ),
    path('all/' , TaskList.as_view()),
    path('get/<int:pk>/' , TaskList.as_view()),
    path('model/<model>/' , TaskList.as_view()),
    path('rang/<rang>/' , TaskList.as_view()),
    path('brent/<brent>/' , TaskList.as_view()),
    path('yil/<int:yil>/' , TaskList.as_view()),
    path('narx/<int:narx>/' , TaskList.as_view()),
     
    
]