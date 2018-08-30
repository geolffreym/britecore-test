from django.urls import path
from .views import RiskView

# Setting up endpoints for risks
urlpatterns = [
    path('', RiskView.as_view()),
    path('<int:risk_pk>/', RiskView.as_view())
]
