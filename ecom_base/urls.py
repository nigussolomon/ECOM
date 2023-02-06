from django.urls import path, include
from .views import EcomProfileView, NotificationHistoryView, UnreadNotificationsView, Logout


urlpatterns = [
    path("profile/", EcomProfileView.as_view()),
    path("notifications/", NotificationHistoryView.as_view()),
    path("unread-notifications/", UnreadNotificationsView.as_view()),
    path("logout/", Logout.as_view()),
]