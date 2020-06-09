from profiles_api import views
from django.urls import path


urlpatterns = [
                path('hello/',views.HelloApiView.as_view()),
]
