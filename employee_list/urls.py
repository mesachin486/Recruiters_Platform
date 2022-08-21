
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candiadte/', views.candidate_detail, name='candidate_detail'),
    path('StatusChanged/<int:pk>', views.change_status, name='change_status'),
    path('upload/<int:pk>', views.upload_resume, name='upload_resume'),
    path('AddCandidate', views.add_candidate, name='add_candidate'),
    path('Form', views.candidate_form, name='candidate_form'),
]
