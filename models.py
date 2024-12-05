from django.db import models

# Create your models here.

class matchlist(models.Model):
    matches= models.CharField(verbose_name="matchfield",max_length=300)
    team_won=models.CharField(verbose_name="winningteam",max_length=300)
    over=models.IntegerField()
    score=models.IntegerField(default=0)

    def __str__(self):
        return self.matches

class playerslist(models.Model):
    match=models.ForeignKey(matchlist,blank=True,null=True, on_delete=models.CASCADE)
    players=models.TextField(null=True,blank=True)
 
    def __str__(self):
        return self.match.matches