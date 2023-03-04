from django.urls import path
from myapp.views import TodoList, TodoDetail

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]