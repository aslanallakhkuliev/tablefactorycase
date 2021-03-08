from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views as api_views
from tables import views as table_views

api_router = routers.DefaultRouter()
api_router.register(r'tables', api_views.TableViewSet)
api_router.register(r'legs', api_views.LegViewSet)
api_router.register(r'feet', api_views.FootViewSet)

table_router = routers.DefaultRouter()
table_router.register(r'tables', table_views.TablesReadOnlyViewSet)
table_router.register(r'legs', table_views.LegsReadOnlyViewSet)
table_router.register(r'feet', table_views.FeetReadOnlyViewSet)

urlpatterns = [
    path('', include(table_router.urls)),
    path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
]
