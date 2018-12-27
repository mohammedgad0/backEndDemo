"""backEndDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from project import viewset
from rest_framework.authtoken import views
from project.models import Employee

router = routers.DefaultRouter()
router.register(r'employees', viewset.EmployeeViewSet)
# router.register('employee', views.CreateEmployee, base_name=Employee)
router.register(r'groups', viewset.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^add-employee/', viewset.CreateEmployee.as_view()),
    path('employee/<int:pk>/update/', viewset.UpdateEmployee.as_view()),
    path('employee/<int:pk>/delete/', viewset.DeleteEmployee.as_view()),
    path('api-auth-token/', views.obtain_auth_token, name='api-auth-token')
    # url(r'^update-employee/(?P<pk>[^/.]+)/$', views.UpdateEmployee.as_view())

] + router.urls
