from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'kia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'kia_app.views.home', name='home'),
    url(r'^logout/', 'kia_app.views.logout_view', name='logout'),
    url(r'^catalog/', 'kia_app.views.catalog', name='catalog'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^send_email/', 'kia.views.send_email', name='send-email'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
