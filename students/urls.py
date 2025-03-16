from django.urls import path
from .views import student_list, student_create, student_update, student_delete, student_detail

urlpatterns = [
    path('', student_list, name='student_list'),
    path('create/', student_create, name='student_create'),
    path('update/<int:id>/', student_update, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
    path('detail/<int:id>/', student_detail, name='student_detail'),
]
