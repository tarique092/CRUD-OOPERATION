from django.urls import path
from . import views
# from django.conf.urls import url
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create,name='create'),
    path('retrive',views.retrive,name='retrive'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]