"""teaReviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.views import LoginView, LogoutView
from review import views as reviewViews
from tea import views as teaViews


router = routers.DefaultRouter()
router.register(r'reviews', reviewViews.ReviewView, 'review')
router.register(r'teas', teaViews.TeaView, 'teas')

# urlpatterns = [
#     path('teasReviews', include('review.urls')),
#     path('admin', admin.site.urls),
#     path('userLogin', LoginView.as_view(template_name='authentication/login.html'), name='user_login'),
#     path('register', LoginView.as_view(), name='register'),
#     path('/userLogout', LogoutView.as_view(template_name='review/index.html'), name='user_logout'),
# ]
urlpatterns = [
        path('admin/', admin.site.urls),
        path('teaReviews/api/', include(router.urls)),
    ]