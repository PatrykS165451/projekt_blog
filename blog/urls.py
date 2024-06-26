from django.urls import path
from .views import HomeView, CategoryView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryListView, AddCommentView, SearchView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category_list/', CategoryListView, name='category-list'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name="delete_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('search/', SearchView.as_view(), name="search"),

]