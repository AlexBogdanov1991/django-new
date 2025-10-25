from django.urls import path

from . import views  # импортируем представления

urlpatterns = [
    path("", views.index, name="index"),
]

from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

router = DefaultRouter()
router.register("questions", views.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
