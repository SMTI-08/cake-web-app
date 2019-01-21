from django.urls import path

from . import views

urlpatterns = [

    path('', views.main_dashboard_view, name='main_dashboard_url'),
    path('company/', views.company_dashboard_view, name='company_dashboard_url'),
    path('sector/', views.sector_dashboard_view, name='sector_dashboard_url'),
    path('analysis/', views.company_analysis_view, name='company_analysis_url'),
    path('comparison/', views.company_comparison_view, name='company_comparison_url'),
    path('help/', views.help_view, name='help_url'),

]
