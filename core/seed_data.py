from core.models import Task

def run():
    if Task.objects.exists():
        print("✅ Tasks already exist — skipping.")
        return

    Task.objects.bulk_create([
        Task(title="Prepare demo report", description="Add example data", completed=False),
        Task(title="Fix static files issue", description="Resolved 404 errors", completed=True),
        Task(title="Verify deployment", description="Run through all endpoints", completed=True),
    ])
    print("🌱 Demo tasks created successfully.")
