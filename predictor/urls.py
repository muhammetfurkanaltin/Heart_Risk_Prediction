from django.urls import path
from . import views
urlpatterns = [
    path("", views.predict_risk, name="predict_risk"),
]