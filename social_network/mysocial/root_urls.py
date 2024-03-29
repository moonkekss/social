from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path

from .views import home, inbox, profile, read_message, send_message


def home_or_register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return redirect("register")


urlpatterns = [
    path("home/", home, name="home"),
    path("profile/", profile, name="profile"),
    path("send_message/", send_message, name="send_message"),
    path("inbox/", inbox, name="inbox"),
    path("read_message/<int:message_id>/", read_message, name="read_message"),
    path("", home_or_register, name="home_or_register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
