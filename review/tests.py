from django.test import TestCase
from review.models import *

class TeaTestCase(TestCase):
    def setUp(self):
        self.tea1 = Tea.objects.create(tea_name = "Earl Grey")
        self.review1 = Review.objects.create(review_text = "Best tea ever",  username="Silvia", tea = self.tea1)

    def test_tea_saved(self):
        self.assertGreater(self.tea1.pk, 0)

    def test_review_saved(self):
        self.assertGreater(self.review1.pk, 0)

    def test_review_fk(self):
        self.assertEqual(self.review1.tea.pk, self.tea1.pk)