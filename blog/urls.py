from django.urls import path ,include
from . import views
from .views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    path("", PostListView.as_view() ,name="blog"),
    path("post/<int:pk>/",PostDetailView.as_view(),name="blog-detail"),
    path("post/new/",PostCreateView.as_view(),name="blog-create"),
    path("post/<int:pk>/update/",PostUpdateView.as_view(),name="blog-update"),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(),name="blog-delete")

]