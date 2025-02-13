from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Customer-related views
    path('customerclick/', views.customerclick_view, name='customerclick'),
    path('customersignup/', views.customer_signup_view, name='customersignup'),
    path('customerlogin/', views.customer_signup_view, name='customerlogin'),  # Login page added
    path('customer-dashboard/', views.customer_dashboard_view, name='customer-dashboard'),
    path('customerlogout/', LogoutView.as_view(), name='customerlogout'),  # LogoutView added

    # Policy-related views
    path('apply-policy/', views.apply_policy_view, name='apply-policy'),
    path('apply/<int:pk>/', views.apply_view, name='apply'),
    path('history/', views.history_view, name='history'),
    
    # Question-related views
    path('ask-question/', views.ask_question_view, name='ask-question'),
    path('question-history/', views.question_history_view, name='question-history'),
]
