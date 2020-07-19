from django.test import TestCase
from django.urls import reverse, resolve

from ..views import task_list, task_completed, task_delete, task_update


class TestUrls(TestCase):
    def test_task_list_view_should_be_resolveed(self):
        url = reverse('task_list')

        self.assertEqual(resolve(url).func, task_list)

    def test_task_completed_view_should_be_resolveed(self):
        url = reverse('task_completed', args=['1'])

        self.assertEqual(resolve(url).func, task_completed)

    def test_ttask_delete_view_should_be_resolveed(self):
        url = reverse('task_delete', args=['1'])

        self.assertEqual(resolve(url).func, task_delete)

    def test_task_update_view_should_be_resolveed(self):
        url = reverse('task_update', args=['1'])

        self.assertEqual(resolve(url).func, task_update)