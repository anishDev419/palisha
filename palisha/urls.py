
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from palisha.views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', TemplateView.as_view(template_name='base.html'), name='home'),
    # path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
    path('', HomePageView.as_view(), name='home'),
]
