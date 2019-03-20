from django.conf.urls import url, include
from .views import chatbotView

urlpatterns = [
    url(r'^api/?$', chatbotView.as_view())
]
