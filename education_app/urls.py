from django.urls import path
# from .views import work_list, work_detail

from .views import (
    WorkListView,
    WorkDetailView,
    WorkCreateView,
    WorkUpdateView,
    WorkDeleteView
)

urlpatterns = [
    path('', WorkListView.as_view(), name='works-list'),
    path('create/', WorkCreateView.as_view(), name='works-create'),
    path('<int:id>/', WorkDetailView.as_view(), name='works-detail'),
    path('<int:id>/delete/', WorkDeleteView.as_view(), name='works-delete'),
    path('<int:id>/update/', WorkUpdateView.as_view(), name='works-update'),
    # path('', work_list),
    # path('<int:id>/', work_detail, name='works-detail'),
]