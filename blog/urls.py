from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostLike,
    CommentUpdateView,
    CommentDeleteView,
    manage_blogs,
    bulk_delete_blogs
)

urlpatterns = [
    path('manage-blogs/', manage_blogs, name='manage_blogs'),
    path('bulk_delete/', bulk_delete_blogs,
         name='bulk_delete_blogs'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
    path('update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(),
         name='update_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(),
         name='delete_comment'),
    path('', PostListView.as_view(), name='blogs'),
    path('summernote/', include('django_summernote.urls')),
    path('tinymce/', include('tinymce.urls')),
]
