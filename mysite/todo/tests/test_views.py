from django.test import TestCase

from ..models import Task


class TestViews(TestCase):
    def setUp(self):
        Task.objects.create(title='test task')
        self.url = 'http://127.0.0.1:8000/'

    def test_task_list_status_code_should_be_200_when_get_task_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_task_create_status_code_should_be_302_when_task_created(self):
        data = {'title': 'post test'}

        response = self.client.post(self.url, data,
                                    format='json')

        self.assertEqual(response.status_code, 302)

    def test_task_update_status_code_should_be_302_when_task_updated(self):
        data = {'title': 'post test (updated)'}

        response = self.client.post(self.url + 'task-update/1', data,
                                    format='json')

        self.assertEqual(response.status_code, 302)

    def test_task_update_status_code_should_be_404_when_task_not_exist(self):
        data = {'title': 'post test (updated)'}

        response = self.client.post(self.url + 'task-update/11', data,
                                    format='json')

        self.assertEqual(response.status_code, 404)

    def test_task_completed_status_code_should_be_302_when_task_status_changed(self):
        data = {'completed': True}

        response = self.client.post(self.url + 'task-completed/1', data,
                                    format='json')

        self.assertEqual(response.status_code, 302)

    def test_task_completed_status_code_should_be_404_when_task_not_exist(self):
        data = {'completed': True}

        response = self.client.post(self.url + 'task-completed/11', data,
                                    format='json')

        self.assertEqual(response.status_code, 404)

    def test_task_delete_status_code_should_be_302_when_task_status_changed(self):
        response = self.client.get(self.url + 'task-delete/1',
                                   format='json')

        self.assertEqual(response.status_code, 302)

    def test_task_delete_status_code_should_be_404_when_task_not_exist(self):
        response = self.client.post(self.url + 'task-delete/11',
                                    format='json')

        self.assertEqual(response.status_code, 404)

    def test_task_list_main_template_should_be_index_html(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, 'todo/index.html')
