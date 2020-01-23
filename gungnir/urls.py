
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import visualizedata.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'home'),
    #path('visualize/', views.visualize1, name = 'visualize'),
    path('predict/', views.predict, name = 'predict'),
    path('visualize/', include('visualizedata.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
