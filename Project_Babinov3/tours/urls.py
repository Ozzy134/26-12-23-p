from django.urls import path
from .views import tours_add, tours_list, tours_detail, tours_edit, tours_delete

urlpatterns = [
    path('', tours_list, name='tours_list'),
    path('add/', tours_add, name='tours_add'),
    path('<int:pk>/', tours_detail, name='tours_detail'),
    path('edit/<int:pk>/', tours_edit, name='tours_edit'),
    path('delete/<int:pk>/', tours_delete, name='tours_delete'),
]