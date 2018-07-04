
from django.contrib import admin
from django.urls import path, include
from products import views
# from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('accounts/', include('accounts.urls'))
    # path('signup', accounts_views.signup, name='signup'),
    # path('login', accounts_views.login, name='login'),
]
