from django.urls import path
from . import views
urlpatterns=[
    path('',views.employee_form,name='employee_insert'), # get and post req.for insert operation
    path('<int:id>/',views.employee_form,name='employee_update'), # get and post req.for update operation
    path('delete/<int:id>',views.employee_delete,name='emp_delete'),
    path('list/',views.employee_list,name="chinna"),# get request and retrieve nad display all records
   
]