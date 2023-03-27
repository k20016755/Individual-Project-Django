import pytest
from django.urls import reverse
from django.test import TestCase,Client
from mydjangoapp.views import task_list
from django.contrib.auth.models import User
import datetime
from datetime import date
from django.utils import timezone
from mydjangoapp.models import Task
class TESTVIEWS(TestCase):
    def setUp(self):
        self.client = Client()
        try:
            self.user = User.objects.get(username='testuser')
        except User.DoesNotExist:
            self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task1 = Task.objects.create(
            
            title="Task 1",
            description="Description 1",
            completed=False,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            
        )
        self.client = Client()
        try:
            self.user = User.objects.get(username='testuser')
        except User.DoesNotExist:
            self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task2 = Task.objects.create(
            

            title="Task 2",
            description="Description 2",
            completed=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            
        )
    @pytest.mark.django_db
    def test_task_list_view(self):     
        #try:
         #   self.client.login(username='testuser', password='testpass')
        #except:
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(user)
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
    

       
        assert response.status_code == 200
    


