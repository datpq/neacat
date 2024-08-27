from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class Graph(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    undirected = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} ({self.category})"

class Vertex(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    label = models.CharField(max_length=30)
    class Meta:
        unique_together = ('graph', 'label')
    def __str__(self):
        return f"{self.label} ({self.graph.name})"

class Edge(models.Model):
    vertex_from = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='edges_from')
    vertex_to = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='edges_to')
    weight = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    class Meta:
        unique_together = ('vertex_from', 'vertex_to')
    def clean(self):
        # Ensure both vertices belong to the same graph
        if self.vertex_from.graph != self.vertex_to.graph:
            raise ValidationError("Both vertices must belong to the same graph.")

        # Check for undirected graph constraints
        if self.vertex_from.graph.undirected:
            # Check if an edge already exists in either direction
            if Edge.objects.filter(vertex_from=self.vertex_to, vertex_to=self.vertex_from).exists():
                raise ValidationError("An edge in the opposite direction already exists for undirected graphs.")

    def save(self, *args, **kwargs):
        # Call the clean method to perform validations
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.vertex_from.label} -> {self.vertex_to.label} (Weight: {self.weight}) ({self.vertex_from.graph.name})"
