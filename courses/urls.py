from django.urls import path
from courses.views import get_course, create_course, update_courses, delete_courses

app_name = 'courses'

urlpatterns = [
    path('', get_course, name='list'),
    path('create/', create_course, name='create'),
    path('update/<int:pk>/', update_courses, name='update'),
    path('delete/<int:pk>/', delete_courses, name='delete')
]
