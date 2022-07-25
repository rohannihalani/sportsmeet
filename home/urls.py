from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.home, name="home-page"),
    path('home/', views.PostListView.as_view(), name="main-page"),
    path('create/', views.PostCreateView.as_view(template_name="home/create.html"), name="create-page"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"  ),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(template_name='home/create.html'), name="post-update"  ),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(template_name='home/post_confirm_delete.html'), name="post-delete"  ),
    path('filter/', views.filter_options, name="filter-options"),
    path('filter/sport/', views.PostFilterSport, name="filter-sport"),
    path('filter/user/', views.PostFilterUser, name="filter-user"),
    path('filter/location/', views.PostFilterLocation, name="filter-location"),


]