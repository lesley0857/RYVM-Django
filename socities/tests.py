from django.test import TestCase
from .models import Societies

# Create your tests here.

class Tests_on_Society_model(TestCase):
    def test_Society_str(self):
        Societies.objects.create(Society_name='leg',Venue='io',Days_of_meeting='ok')
        soc = Societies.objects.get(id=1)
        print(type(soc))
        self.assertEqual(str(soc),'leg')