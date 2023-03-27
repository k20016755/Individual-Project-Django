import pytest
from django.urls import reverse
from django.test import TestCase,RequestFactory
from mydjangoapp.views import task_list
class TESTVIEWS(TestCase):
    @pytest.mark.django_db
    def test_task_list_view(self):
        factory = RequestFactory()
        self.assertTemplateUsed('mydjangoapp/task_list.html')
        request = factory.get(reverse('task_list'))
        response = task_list(request)
        self.assertContains(response,'<h1>Task List<h1>')
       
        assert response.status_code == 200
    


