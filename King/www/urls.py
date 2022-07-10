from django.urls import path
from . import views

urlpatterns = [
    path('', views. www, name = 'www'),
    path('create', views. create, name = 'create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name = 'www-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name = 'www-update'),
    path('<int:pk>/delete', views.NewsDeletelView.as_view(), name = 'www-delete')
]