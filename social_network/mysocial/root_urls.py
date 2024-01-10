from django.urls import path
from .views import home, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    #path('send_message/', SendMessageView.as_view(), name='send_message'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)