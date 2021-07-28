from django.urls import path
from groups.views import get_group, create_group, update_group, delete_group

app_name = 'groups'

urlpatterns = [
    path('', get_group, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:pk>/', update_group, name='update'),
    path('delete/<int:pk>/', delete_group, name='delete')
]
