from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import HomeworkViewSet, HomeworkListView, HomeworkDetailView, HomeworkUpdateView, HomeworkDeleteView

router = DefaultRouter()
router.register('homework',HomeworkViewSet,basename='homework'),
urlpatterns = [
    path('',include(router.urls)),
    path('list/',HomeworkListView.as_view(),name='homework-list'),
    path('detail/<int:pk>/',HomeworkDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',HomeworkUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',HomeworkDeleteView.as_view(),name='delete'),
]