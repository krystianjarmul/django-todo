from django.test import TestCase

from ..models import Task


class TestModels(TestCase):
    def setUp(self):
        Task.objects.create(title='test task')
        self.task = Task.objects.get(id=1)

    def test_task_should_be_added_to_db_when_created(self):
        title = self.task.title
        self.assertEqual(title, 'test task')

    def test_task_object_name_should_be_its_title(self):
        self.assertEqual(self.task.__str__(), 'test task')

    def test_task_completed_should_be_False_when_initialized(self):
        self.assertFalse(self.task.completed)

    def test_task_should_change_status_when_overwritten(self):
        self.task.completed = True

        self.task.save()

        self.assertTrue(Task.objects.get(id=1).completed)

    def test_task_should_raise_DoesNotExist_exception_when_not_exist(self):
        self.task.delete()

        self.assertRaises(Task.DoesNotExist, lambda: Task.objects.get(id=1))