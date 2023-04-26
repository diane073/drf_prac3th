from django.urls import path
from articles import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'),
    path('<int:article_id>/comment/', views.CommentView.as_view(), name='comment_view'),
    path('<int:article_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail.view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='like_view'), 
    #aritcle조회 시 가져오므로 get필요X .. 있으면 적용 없으면 지우기 방식으로 post, delete함께 작성
]