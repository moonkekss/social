from django.urls import path
from .views import home, profile, send_message, inbox, read_message 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('send_message/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('read_message/<int:message_id>/', read_message, name='read_message')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)