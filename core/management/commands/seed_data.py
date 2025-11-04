from django.core.management.base import BaseCommand
from core.models import Task

class Command(BaseCommand):
    help = "Seeds the database with sample Task data."

    def handle(self, *args, **options):
        if Task.objects.exists():
            self.stdout.write(self.style.WARNING("✅ Tasks already exist — skipping."))
            return

        Task.objects.bulk_create([
            Task(title="Prepare demo report", description="Add example data", completed=False),
            Task(title="Fix static files issue", description="Resolved 404 errors", completed=True),
            Task(title="Verify deployment", description="Run through all endpoints", completed=True),
        ])

        self.stdout.write(self.style.SUCCESS("🌱 Demo tasks created successfully."))
