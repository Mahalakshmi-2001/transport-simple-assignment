from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.post_question, name='post_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]
