from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('addCourse',views.addCourse,name="addCourse"),
    path('saveCourse',views.saveCourse,name="saveCourse"),
    path('addStudent',views.addStudent,name="addStudent"),
    path('saveStudent',views.saveStudent,name="saveStudent"),
    path('displayStudent',views.displayStudent,name="displayStudent"),
    path('edit<int:pk>',views.edit,name="edit"),
    path('updateStudent<int:pk>',views.updateStudent,name="updateStudent"),
    path('delete<int:pk>',views.delete,name="delete")
]