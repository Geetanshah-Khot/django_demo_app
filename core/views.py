from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import matplotlib.pyplot as plt
from django.shortcuts import render
import io, base64

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer

@api_view(["GET"])
def joke_api(request):
    """Simple API integration example."""
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    if r.status_code == 200:
        data = r.json()
        return Response({"setup": data["setup"], "punchline": data["punchline"]})
    return Response({"error": "Failed to fetch joke"}, status=500)

def report_view(request):
    """Simple data visualization."""
    tasks = Task.objects.all()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()

    fig, ax = plt.subplots()
    ax.bar(["Completed", "Pending"], [completed, pending])
    ax.set_title("Task Completion Report")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()
    plt.close(fig)
    return render(request, "report.html", {"chart": img})
