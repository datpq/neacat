from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Graph, Vertex, Edge

def index(request):
    return render(request, "easygraph/index.html")

def dfs(request):
    # Retrieve all graph objects
    all_graphs = Graph.objects.values('id', 'name', 'category', 'undirected')

    # Filter the graphs manually to include only those where 'dfs' is one of the categories
    graphs = [
        graph for graph in all_graphs 
        if 'dfs' in map(str.strip, graph['category'].split(','))  # Split and trim each category
    ]
    # Convert to list of dictionaries with only required fields
    graphs_list = [{'id': graph['id'], 'name': graph['name'], 'undirected': graph['undirected']} for graph in graphs]
    return render(request, "easygraph/dfs.html", {"graphs": graphs_list})

def bfs(request):
    # Retrieve all graph objects
    all_graphs = Graph.objects.values('id', 'name', 'category', 'undirected')

    # Filter the graphs manually to include only those where 'bfs' is one of the categories
    graphs = [
        graph for graph in all_graphs 
        if 'bfs' in map(str.strip, graph['category'].split(','))  # Split and trim each category
    ]
    # Convert to list of dictionaries with only required fields
    graphs_list = [{'id': graph['id'], 'name': graph['name'], 'undirected': graph['undirected']} for graph in graphs]
    return render(request, "easygraph/bfs.html", {"graphs": graphs_list})

def dijkstra(request):
    # Retrieve all graph objects
    all_graphs = Graph.objects.values('id', 'name', 'category', 'undirected')

    # Filter the graphs manually to include only those where 'dijkstra' is one of the categories
    graphs = [
        graph for graph in all_graphs 
        if 'dijkstra' in map(str.strip, graph['category'].split(','))  # Split and trim each category
    ]
    # Convert to list of dictionaries with only required fields
    graphs_list = [{'id': graph['id'], 'name': graph['name'], 'undirected': graph['undirected']} for graph in graphs]
    return render(request, "easygraph/dijkstra.html", {"graphs": graphs_list})

def get_vertices(request, graph_id):
    vertices = Vertex.objects.filter(graph_id=graph_id).values('id', 'label')
    # Return the vertices as JSON
    return JsonResponse(list(vertices), safe=False)

def get_edges(request, graph_id):
    graph = get_object_or_404(Graph, id=graph_id)
    edges = Edge.objects.filter(vertex_from__graph=graph).values('id', 'vertex_from', 'vertex_to', 'weight')
    # Return the vertices as JSON
    return JsonResponse(list(edges), safe=False)
