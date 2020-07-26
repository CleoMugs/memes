from accounts.api.views import (RoleViewSet, #BloggerViewSet, 
	PostViewSet, CommentViewSet 
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
#router.register(r'blogers', BloggerViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
#router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls