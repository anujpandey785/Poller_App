from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    slug=models.SlugField()

    # TODO: Define fields here
    content=models.CharField(max_length=1024)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.content

class Answer(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    choice=models.ForeignKey('Choice',on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)




class Choice(models.Model):

    content=models.CharField(max_length=256)
    question=models.ForeignKey('Question',on_delete=models.CASCADE)

    @property
    def answer_count(self):
        return Answer.objects.filter(
            question=self.question,
            choice=self.id
        ).count


    def __str__(self):
        return "{} - {}".format(self.question.content[:50],self.content)


