from django.conf.urls import include, url
from django.contrib import admin
import app.views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'helix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.landing_view'),
    url(r'^events/$', 'app.views.events_view'),
    url(r'^gallery/$', 'app.views.gallery_view'),
    url(r'^events/app/$', 'app.views.event_app'),
    url(r'^events/smart/$', 'app.views.event_smart'),
    url(r'^events/startup/$', 'app.views.event_startup'),
    url(r'^events/roundtable/$', 'app.views.event_roundtable'),
    url(r'^events/photo/$', 'app.views.event_photo'),
    url(r'^events/code/$', 'app.views.event_code'),
    url(r'^events/mockcamp/$', 'app.views.event_mockcamp'),
    url(r'^events/mockupsc/$', 'app.views.event_mockupsc'),
]
