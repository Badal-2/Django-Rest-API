from django.db import models

# Create your models here.


class Todo(models.Model):
    id=models.AutoField(primary_key=True)
    Tittle=models.CharField(max_length=100)
    description=models.TextField()
    completed=models.BooleanField(default=False)




    def __str__(self):
        return self.Tittle
    



class instagram(models.Model):

    id=models.AutoField(primary_key=True)
    user_Name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    password=models.IntegerField()

    def __str__(self):
        return self.user_Name