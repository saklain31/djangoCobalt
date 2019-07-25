from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


from user.views import *
from SocialAuth.views import *
from countdown.views import *
from event.views import *


from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # path('setPerm/',setUserPermissions),
    # path('objPerm/',createObjectWithPermission),

    path("login/", login, name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path("logout/", logout_view, name="logout"),

    path('countdown/',countDownTime),
    path('eventinfo/',takeEventInfo),
    path('createEvent/',createEvent),
    # path('createEvent/',createEvent),
    path('displayEvents/',displayEvents),
    path('addEventToCalendar/',addEventToCalendar),
    path('exportEvents/',exportEvents),
    # path('getEventsFromDB/',getEventsFromDB),

    path('accounts/', include('allauth.urls')),

    #user sign-up-log-in-page
    path('user/', include('user.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
