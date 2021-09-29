from django.conf.urls import url
# from django.urls import path
from . import views
# from .views import EmployeeView

urlpatterns = [
    url('create_employee/', views.EmployeeView.as_view()),
    url('get_employee/', views.EmployeeGetView.as_view()),
    url(r'^update_employee/(?P<pk>\d+)/$', views.EmployeePutView.as_view()),
    url('delete_employee/', views.EmployeeDeleteView.as_view()),
    url('login/', views.loginApi.as_view())
]