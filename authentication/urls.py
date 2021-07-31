from django.urls import path
from .views import LoginView, StudentView, TeacherView


urlpatterns = [ 
    path('login/', LoginView.as_view(), name='login'),
    path('student/', StudentView.as_view(), name='student'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
]