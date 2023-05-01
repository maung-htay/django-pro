from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


from .models import Book,Review

class BookTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="XXXXXXXXXXXXXXXXXXXX",
            password="XXXXXXXXXXX",
        )
        
        cls.book = Book.objects.create(
            title="A good title",
            author="Maung Htay",
            price="12.00",
        )
        
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review",
        )
        
    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "A good title")
        self.assertEqual(f"{self.book.author}", "Maung Htay")
        self.assertEqual(f"{self.book.price}", "12.00")
        
    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "books/book_list.html")
        
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "books/book_detail.html")        