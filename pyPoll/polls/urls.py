from django.urls import path
from . import views

# add namespace for links
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index') # "/polls"
]