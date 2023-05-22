from django.urls import path
from .views import *

urlpatterns = [
    path('create',Create.as_view()),
    path('',BookList.as_view()),
    path('<int:id>',BookDetails.as_view()),
    path('update/<int:id>/',Update.as_view()),
    path('search',Search.as_view()),
    path('buy/<int:id>/',Buy.as_view()),
    path('history',History.as_view()),
    path('comment/<int:id>/',Comments.as_view()),
]