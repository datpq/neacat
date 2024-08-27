from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dfs", views.dfs, name="dfs"),
    path("bfs", views.bfs, name="bfs"),
    path("dijkstra", views.dijkstra, name="dijkstra"),
    path('get_vertices/<int:graph_id>/', views.get_vertices, name='get_vertices'),
    path('get_edges/<int:graph_id>/', views.get_edges, name='get_edges'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)