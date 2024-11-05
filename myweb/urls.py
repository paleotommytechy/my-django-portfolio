from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='home'),
    path('about/',views.about, name='about'),
    path('projects/',views.project, name='projects'),
    path('testimonies/',views.testimonies, name='testimonies'),
    path('contact/',views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)