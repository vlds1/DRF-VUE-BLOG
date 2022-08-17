from django.urls import path
from .views import *

urlpatterns = [
    path('all/', AllPublicationsAPIView.as_view()),
    path('blog/', BlogPublicationsAPIView.as_view()),
    path('articles/', ArticlesPublicationsAPIView.as_view()),

    path('create/', CreatePublAPIView.as_view()),
    path('<str:id>', GetPublAPIView.as_view()),    
    path('edit/<str:id>', EditPublicationAPIView.as_view()),
    path('delete/<str:id>', DeletePublAPIView.as_view()),
]