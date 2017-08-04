from django.test import TestCase
from sign.models import Event,Guest

# Create your tests here.
class ModelsTest(TestCase):
	"""docstring for modelsTest"""
	def setUp(self):
		Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,address='shenzhen',start_time='2017-08-08 08:30:00')
		Guest.objects.create(id=1,event_id=1,realname='alen2',phone='13711001101',email='alen1@mail.com',sign=False)

	def test_event_models(self):
			result = Event.objects.get(name="oneplus 3 event")
			self.assertEqual(result.address,"shenzhen")
			self.assertTrue(result.status)

	def test_guest_models(self):
			result = Guest.objects.get(phone='13711001101')
			self.assertEqual(result.realname,"alen2")
			self.assertFalse(result.sign)

		