from django.core.management.base import BaseCommand
from core.models import Task, Report
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **options):
        # Create superuser if not exists
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin", email="admin@example.com", password="admin123"
            )
            self.stdout.write(self.style.SUCCESS("✅ Superuser 'admin' created (pwd: admin123)"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Superuser 'admin' already exists."))

        # Create sample tasks
        if not Task.objects.exists():
            Task.objects.bulk_create([
                Task(title="Design Homepage", description="UI/UX design for landing page", completed=False),
                Task(title="Set up CI/CD", description="Integrate GitHub actions and Railway", completed=True),
                Task(title="API Integration", description="Connect frontend to Django REST API", completed=False),
            ])
            self.stdout.write(self.style.SUCCESS("✅ Sample Tasks created."))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Tasks already exist."))

        # Create sample reports
        if not Report.objects.exists():
            Report.objects.bulk_create([
                Report(title="Q1 Progress", content="Initial sprint goals achieved."),
                Report(title="Q2 Planning", content="Setting targets for next quarter."),
            ])
            self.stdout.write(self.style.SUCCESS("✅ Sample Reports created."))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Reports already exist."))
