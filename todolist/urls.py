from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('add',views.addTodoItem,name='add'),
    path('completed/<todo_id>',views.completedTodo,name='completed'),
    path('delete',views.delete,name='delete'),
    path('deleteall',views.deleteAll,name='deleteall')

]
