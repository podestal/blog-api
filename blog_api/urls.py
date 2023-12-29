from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('posts', views.PostViewSet, basename='posts')
router.register('allPosts', views.AllPostsViewSet)
router.register('topics', views.TopicViewSet)
router.register('authors', views.AuthorViewSet, basename='authors')

sections_router = routers.NestedDefaultRouter(router, 'posts', lookup='posts')
sections_router.register("sections", views.SectionViewSet, basename='sections')

bodies_router = routers.NestedDefaultRouter(sections_router, 'sections', lookup='sections')
bodies_router.register("bodies", views.BodyViewSet, basename='bodies')

urlpatterns = router.urls + sections_router.urls + bodies_router.urls
