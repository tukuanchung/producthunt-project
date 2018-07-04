
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static
# from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls'))
    # path('signup', accounts_views.signup, name='signup'),
    # path('login', accounts_views.login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
