
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

   


urlpatterns = [
    # path('',views.home, name="home")
    path('about/',views.about, name="about"),
    path('post/new', PostCreateView.as_view(), name="blog-new"),
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="delete"),
    
    
]