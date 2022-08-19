from django.urls import path
from .views import CommunityView

urlpatterns = [
  path('communities/', CommunityView.as_view(), name='communities_list'),
  path('communities/<int:id>', CommunityView.as_view(), name='communities_process')
]
