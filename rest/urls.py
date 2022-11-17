from django.urls import path
from rest_framework import routers

from .views import WorkViewSet, AssessmentViewSet, UserViewSet

router = routers.SimpleRouter()

router.register(r'works', WorkViewSet)
router.register(r'assessments', AssessmentViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('works/', WorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='work-list'),
#     path('works/<int:pk>', WorkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='work-detail'),
#
#     path('assessments/', AssessmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='assessment-list'),
#     path('assessments/<int:pk>', AssessmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='assessment-detail'),
#
#     path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
#     path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
# ]