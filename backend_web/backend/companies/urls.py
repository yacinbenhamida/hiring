from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompaniesView)

urlpatterns = [
    path('', include(router.urls)),
    re_path('^matches/(?P<company>.+)/$', views.CompanyMatching.as_view()),
]