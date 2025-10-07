from django.db import models

class BookersDetails(models.Model):
    
    booker_name=models.CharField(max_length=250,null=True)
    booker_pic=models.ImageField(null=True,upload_to='pic/')
    contribution=models.IntegerField(max_length=200,null=True)
    about_me=models.TextField(blank=True)
    contributed_books=models.TextField(blank=True,null=True)
    role=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.booker_name
