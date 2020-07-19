from django.test import TestCase

from ..forms import TaskForm

class TestForms(TestCase):
    def test_task_form_should_be_valid_when_title_is_passed(self):
        form = TaskForm(
            data={ 'title': 'test task'}
        )

        self.assertTrue(form.is_valid())

    def test_task_form_should_be_invalid_when_data_not_passed(self):
        form = TaskForm(
            data={}
        )

        self.assertFalse(form.is_valid())