from django.urls import path
from user import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("signup/", view=views.signup, name="signup"),
    path("signin/", view=views.signin, name="signin"),
]
