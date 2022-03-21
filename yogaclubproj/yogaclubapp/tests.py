from django.test import TestCase
from django.contrib.auth.models import User
from .models import Classes, ClassDetail, Pricing, Schedule
from .forms import ClassForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class ClassTest(TestCase):
    def setUp(self):
        self.type=Classes(title='Yoga Class')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Yoga Class')

    def test_tablename(self):
        self.assertEqual(str(Classes._meta.db_table), 'classes')


class ClassDetailTest(TestCase):
    def setUp(self):
        self.type=ClassDetail(detail='details')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'details')

    def test_tablename(self):
        self.assertEqual(str(ClassDetail._meta.db_table), 'classdetail')

class PricingTest(TestCase):
    def setUp(self):
        self.title=Pricing(title='Pricing')

    def test_typestring(self):
        self.assertEqual(str(self.title), 'Pricing')

    def test_tablename(self):
        self.assertEqual(str(Pricing._meta.db_table), 'pricing')

class ScheduleTest(TestCase):
    def setUp(self):
        self.type=Schedule(title='schedule')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'schedule')

    def test_tablename(self):
        self.assertEqual(str(Schedule._meta.db_table), 'schedule')

class NewClassForm(TestCase):
    # valid form data
    def test_classform(self):
        data={
            'title':'Title', 
            'date':'2022-04-28', 
            'time':'12:00:00', 
            'location':'Location', 
            'style':'yogaStyle',
            'detail':'detail'
            }
        form=ClassForm (data)
        self.assertTrue(form.is_valid)

class New_Class_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testUser2', password='P@ssw0rd!')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newclass'))
        self.assertRedirects(response, '/accounts/login/?next=/yogaclubapp/newclass/')

