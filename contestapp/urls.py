from django.urls import path
from . import views

urlpatterns = [
     path('',views.landing, name="landing" ),
     path('question1/<int:qno>/',views.home, name="home" ),
     path('questions',views.questions, name="questions" ),
     path('login',views.user_login, name="login" ),
     path('register',views.register, name="register" )
]
