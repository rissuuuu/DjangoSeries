
# Create your models here.
from django.db import models

class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')
    cover=models.ImageField(upload_to='books/covers/',null=True,blank=True)
    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'save_loc':self.pdf,
            'cover':self.cover
        }



