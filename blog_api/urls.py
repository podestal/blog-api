from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('posts', views.PostViewSet)
router.register('topics', views.TopicViewSet)
router.register('sections', views.SectionViewSet)
router.register('bodies', views.BodyViewSet)
router.register('authors', views.AuthorViewSet)

urlpatterns = router.urls
