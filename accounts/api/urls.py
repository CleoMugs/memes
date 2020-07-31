from accounts.api.views import (RoleViewSet, #BloggerViewSet, 
	PostViewSet, CommentViewSet, ProfileViewSet 
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ROLES', RoleViewSet)
router.register(r'PROFILES', ProfileViewSet)
#router.register(r'POSTS', PostViewSet)
router.register(r'COMMENTS', CommentViewSet)

urlpatterns = router.urls