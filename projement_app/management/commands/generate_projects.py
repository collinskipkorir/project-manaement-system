from django.core.management.base import BaseCommand
from projement_app.models import Project

class Command(BaseCommand):
    help = 'Generates 300 projects in the database'

    def handle(self, *args, **kwargs):
        
        for i in range(301):
            if not Project.objects.filter(title=f'Project title {i}').exists():
                Project.objects.create(
                    title=f'Project title {i}',
                    description='This is a static project project description',
                
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully created projects'))
