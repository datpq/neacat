from django.contrib import admin

# Register your models here.
from .models import Graph, Vertex, Edge

admin.site.register(Graph)
admin.site.register(Vertex)
admin.site.register(Edge)
