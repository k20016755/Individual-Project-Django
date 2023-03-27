import pytest
from django.urls import reverse
from django.test import TestCase,RequestFactory
from mydjangoapp.views import task_list
import datetime
from datetime import date
from django.utils import timezone
from mydjangoapp.models import Task
class TESTVIEWS(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(
            title="Task 1",
            description="Description 1",
            completed=False,
            created=datetime.now(),
            due=datetime.date.today()
        )
        self.task2 = Task.objects.create(
            title="Task 2",
            description="Description 2",
            completed=True,
            created=datetime.now(),
            due=datetime.date.today()
        )
    @pytest.mark.django_db
    def test_task_list_view(self):
        response = self.client.get(reverse('mydjangoapp:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
    

       
        assert response.status_code == 200
    


