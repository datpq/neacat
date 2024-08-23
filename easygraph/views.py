from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Graph, Vertex, Edge

def index(request):
    return render(request, "easygraph/index.html")

def dfs(request):
    # Convert QuerySet to a list of dictionaries using `values()`
    graphs = list(Graph.objects.filter(category='dfs').values('id', 'name', 'undirected'))
    # graphs = Graph.objects.filter(category='dfs')
    return render(request, "easygraph/dfs.html", {"graphs": graphs})

def get_vertices(request, graph_id):
    vertices = Vertex.objects.filter(graph_id=graph_id).values('id', 'label')
    # Return the vertices as JSON
    return JsonResponse(list(vertices), safe=False)

def get_edges(request, graph_id):
    graph = get_object_or_404(Graph, id=graph_id)
    edges = Edge.objects.filter(vertex_from__graph=graph).values('id', 'vertex_from', 'vertex_to', 'weight')
    # Return the vertices as JSON
    return JsonResponse(list(edges), safe=False)
