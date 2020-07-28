from accounts.api.views import (RoleViewSet, #BloggerViewSet, 
	PostViewSet, CommentViewSet, ProfileViewSet 
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
#router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls