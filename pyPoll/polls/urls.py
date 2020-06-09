from django.urls import path
from . import views

# add namespace for links
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'), # "/polls"
    path('<int:question_id>/', views.detail, name='detail'), 
    path('<int:question_id>/results', views.results, name='results'), 
    path('<int:question_id>/vote', views.vote, name='vote') 
]