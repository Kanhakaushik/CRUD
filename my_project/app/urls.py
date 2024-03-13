from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('savedata/',savedata,name='savedata'),
    path('login/',login,name='login'),
    path('about/',about,name='about'),
    path('register/',register,name='register'),
    path('logindata/',logindata,name='logindata'),
    # path('delete/',delete,name="delete"),
    path("query/",query,name="query"),
    path('showdata/<str:pk>',showdata,name='showdata'),

    path('contact',contact,name="contact"),
    path('edit/<int:pk>',edit,name='edit'),
    path('dash/',dash,name="dash"),
    path('table/', table,name="table"),
    path('update/<int:pk>',update,name='update'),
    path('delete/<int:pk>',delete,name='delete'),
    path('search/<str:var>',search,name="search")

    # <td><a href="{% url 'delete' pk=i.id %}"><i class="bx bxs-x"></i></a></td> 
]
