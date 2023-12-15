
# crudapp/urls.py
from django.urls import path
from .views import candidate_list, create_candidate, edit_candidate, delete_candidate, index, view_candidate

urlpatterns = [
    path('', index, name='index'),
    path('candidate_list', candidate_list, name='candidate_list'),
    path('create/', create_candidate, name='create_candidate'),
    path('view/<int:candidate_id>/', view_candidate, name='view_candidate'),
    path('edit/<int:candidate_id>/', edit_candidate, name='edit_candidate'),
    path('delete/<int:candidate_id>/', delete_candidate, name='delete_candidate'),
]

