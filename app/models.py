from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book/',null=True)
    book_name = models.CharField(max_length=50)
    price = models.CharField(max_length=25)

    def __str__(self) :
        return self.book_name
    
class BuyBook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.book.book_name
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE) 
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book.book_name
    


