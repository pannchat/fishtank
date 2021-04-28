"""fishhi_p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import tankManage.views
import account.views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc', tankManage.views.tankcalc, name='calc'),
    path('list/<str:keyword>', tankManage.views.list, name="list"),
    path('search', tankManage.views.search, name="search"),
    path('', tankManage.views.feed, name="index"),
    path('test', tankManage.views.test, name="test"),
    path('create_fishtank', tankManage.views.create_fishtank, name="create_fishtank"),
    path('add_fish/<int:pid>', tankManage.views.add_fish, name="add_fish"),
    path('add_plant/<int:pid>', tankManage.views.add_plant, name="add_plant"),
    path('add_supplies/<int:pid>', tankManage.views.add_supplies, name="add_supplies"),
    path('profile/<str:pk>', account.views.profile, name='profile'),
    path('profile/', account.views.my_profile, name='my_profile'),
    path('signup/', account.views.signup, name="signup"),
    path('signin/', account.views.signin, name="signin"),   
    path('signout/', account.views.signout, name="signout"),  
    path('fishtank/<int:pid>', tankManage.views.fishtank, name="fishtank"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)