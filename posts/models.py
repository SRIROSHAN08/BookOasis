from django.db import models

# Create your models here.
class BookDetails(models.Model):
    
    book_name=models.CharField(max_length=250,null=True)
    author_name=models.CharField(max_length=250,null=True)
    published_date=models.DateField()
    front_page_summary=models.CharField(max_length=250,null=True)
    detailed_summary=models.TextField(blank=True)
    book_picture=models.ImageField(null=True, upload_to='images/')
    front_page_picture=models.ImageField(null=True,upload_to='images/front/')
    contributor=models.CharField(max_length=100,null=True)
    
    
    def __str__(self):
        return self.book_name+ " " + self.author_name 