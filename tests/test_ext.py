import pytest
from django.test import TestCase
from socities.models import Societies
# @pytest.mark.skip
@pytest.mark.django_db
def test_society_model():
    Societies.objects.create(Society_name='leg',Venue='io',Days_of_meeting='ok')
    soc = Societies.objects.get(id=1)
    print(soc.__str__())
    assert str(soc), 'leg'

