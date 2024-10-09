from django.db import models

# Create your models he
class Author(models.Model):
    name=models.CharField(max_length=500,null=True)

    def __str__(self):
        return '{}'.format(self.name)
class bk(models.Model):
    title=models.CharField(max_length=500,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media')
    quantity=models.IntegerField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
       return '{}'.format(self.title)