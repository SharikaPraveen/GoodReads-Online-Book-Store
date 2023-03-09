from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'GoodApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add_book'),
    path('update/<int:id>/',views.update,name='update'),
    # path('delete/<int:id>/', views.deleted, name='delete'),
    path('submit/<int:id>/', views.submit, name='submit')

]
