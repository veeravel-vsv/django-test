from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
					url(r'^$', views.login_page, name = 'login'),
					# url(r'^login/',TemplateView.as_view(template_name="login.html")),
					url(r'^index/', views.index, name = 'index_name'),
					url(r'^$', views.logout_page,name = 'logout')				
			  ]