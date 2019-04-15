from django.test import TestCase

# Create your tests here.
class TestCase1(TestCase):
    def test1(self):
        print("testing pass")
        self.assertEqual("asd", "asd")
