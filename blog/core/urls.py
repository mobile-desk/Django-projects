from django.contrib import admin
from django.urls import path, include
from blog import settings
from . import views
from .views import blog, articleView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', blog.as_view(), name="home" ),
    path('signup', views.signup , name="signup"),
    path('signin', views.signin , name="signin"),
    path('signout', views.signout , name="signout"),
    path('article/<int:pk>', articleView.as_view(), name="article"),
]


urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)