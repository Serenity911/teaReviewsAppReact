from django.urls import path

from . import views

urlpatterns = [
    path('/reviews', views.reviews_index, name='reviews_index'),
    path('/reviews/new', views.review_new, name='review_new'),
    path('/teas', views.teas_index, name='teas_index'),
    path('/teas/new', views.tea_new, name='tea_new'),
    path('/userLogout', views.user_logout, name='user_logout')
]