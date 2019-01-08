from django.urls import path

from . import views

urlpatterns = [
    path('analysis/', views.company_analysis_view, name='company_analysis_url'),
    path('comparison/', views.company_comparison_view, name='company_comparison_url')
]
