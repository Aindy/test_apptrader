from django.contrib import admin
from django.urls import path
from menuapp.views import test_menu_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-menu/', test_menu_view, name='test_menu'),
]
