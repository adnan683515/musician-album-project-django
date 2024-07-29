from django.db import models
from musican_app.models import musican

# Create your models here.
class Album(models.Model):
    Album_Name = models.CharField(max_length=200)
    Musican = models.ForeignKey(musican,on_delete=models.CASCADE)
    Album_Realese_Date = models.DateField(auto_now_add=True)
    rat = [('One','1'),('Two','2'),('Three','3'),('Four','4'),('Five','5')]
    Rating = models.CharField( 
        max_length = 5, 
        choices = rat, 
        default = '1'
        ) 
    
    def __str__(self):
        return self.Album_Name
    