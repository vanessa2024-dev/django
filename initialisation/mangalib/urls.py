from django.urls import path # gere les routes
from . import views


urlpatterns = [
    path(
        "", views.index, name="index"
    )
]
