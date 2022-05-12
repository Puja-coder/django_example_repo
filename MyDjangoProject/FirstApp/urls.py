from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save_data, name='save'),
    path('employee/', views.get_emp_data, name='employee'),
    path('emp_table/', views.get_dataframe, name='emp_table'),
]