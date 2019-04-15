from django.test import TestCase

# Create your tests here.
class TestCase(TestCase):
    def test1(self):
        print("testing pass")
        self.assertEqual("asd", "asd")

    # def test2(self):
    #     print("testing fail")
    #     self.assertEqual("asd", "asd2")
