from django.urls import path, include
from .views import EcomProfileView, NotificationHistoryView, UnreadNotificationsView


urlpatterns = [
    path("profile/", EcomProfileView.as_view()),
    path("notifications/", NotificationHistoryView.as_view()),
    path("unread-notifications/", UnreadNotificationsView.as_view())
]