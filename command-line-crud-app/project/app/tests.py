from django.test import TestCase
from .models import Model


# Create your tests here.
class TestModel_test_cases(TestCase):
    def test_Model_creation(self):
        Model = Model(title="dog")
        Model.save()
        self.assertEqual(Model.objects.count(), 1)

    def test_read_all_games(self):
        Model = Model.objects.create(title="dog")
        Model.save()

        Models = Model.objects.all()
        title = [Model.title for Model in Models]
        self.assertEqual(len(title), 1)

    def test_delete_Model(self):
        D = Model(title="dog")
        D.save()

        

        D.delete()
        Models = Model.objects.all()
        self.assertEqual(len(Models), 0)

    def test_update_Model(self):
        Model = Model.objects.create(title="dog")
        Model.save()
        Model.title = "dog: Black"
        Model.save()

        self.assertEqual(Model.title, "dog: Black")

    def test_read_by_title(self):
        Model = Model.objects.create(title="dog")
        Model.save()
        Model_return = Model.objects.get(title="dog")
        self.assertEqual(Model_return.title, "dog")

    def test_filtered_search(self):
        Model = Model.objects.create(title="dog")
        Model.save()
        Model_return = Model.objects.filter(title="dog")
        self.assertEqual(Model_return[0].title, "dog")