import email
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from projement_app.models import Project




class ProjectTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="john@gmailcom",
            password="johnpassword123",
            full_name="John Doe",
            is_staff=False
        )
        self.client.force_authenticate(self.user)
   

    def test_project_actual_hours_incrementaL(self):
        """Test incremental actual hours developers making update at the same time"""

        proj = Project.objects.create(
                    title='Project title',
                    description='This is a static project project description',
                    actual_hours=25 # initial value
                
                )
    
        payload = {
            "actual_hours": 10,
        }
        payload2 = {
            "actual_hours": 10,
        }
        developer1 = self.client.patch(f"/api/v1/edit-project/{proj.id}", payload)
        developer2 = self.client.patch(f"/api/v1/edit-project/{proj.id}", payload2)

        self.assertEqual(developer1.status_code, status.HTTP_200_OK)
        self.assertEqual(developer2.status_code, status.HTTP_200_OK)
        self.assertEqual(float(developer1.data["data"]["actual_hours"]), 35.00) #  initial value 25 + 10 = 35
        self.assertEqual(float(developer2.data["data"]["actual_hours"]), 45.00) # initial value 35 + 10 = 45

       