from django.db import models

# Create your models here.
class Questions(models.Model):
    qno = models.IntegerField()
    question = models.CharField(max_length=100)
    
    sinpu = models.CharField(max_length=100)
    soutpu = models.CharField(max_length=100)
    
    inpu = models.CharField(max_length=100)
    outpu = models.CharField(max_length=100)
    
    inpu2 = models.CharField(max_length=100)
    outpu2 = models.CharField(max_length=100)
    
    inpu3 = models.CharField(max_length=100)
    outpu3 = models.CharField(max_length=100)
    
    inpu4 = models.CharField(max_length=100)
    outpu4 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question
class time(models.Model):
    time = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.time
    
class score(models.Model):
    uname = models.CharField(max_length=100)
    question1 = models.IntegerField(default=0)
    question2 = models.IntegerField(default=0)
    question3 = models.IntegerField(default=0)
    question4 = models.IntegerField(default=0)
    question5 = models.IntegerField(default=0)
    question6 = models.IntegerField(default=0)
    question7 = models.IntegerField(default=0)
    question8 = models.IntegerField(default=0)
    question9 = models.IntegerField(default=0)
    question10 = models.IntegerField(default=0)
    question11 = models.IntegerField(default=0)
    question12 = models.IntegerField(default=0)
    question13 = models.IntegerField(default=0)
    question14 = models.IntegerField(default=0)
    question15 = models.IntegerField(default=0)
    question16 = models.IntegerField(default=0)
    question17 = models.IntegerField(default=0)
    question18 = models.IntegerField(default=0)
    question19 = models.IntegerField(default=0)
    question20 = models.IntegerField(default=0)
    question21 = models.IntegerField(default=0)
    question22 = models.IntegerField(default=0)
    question23 = models.IntegerField(default=0)
    question24 = models.IntegerField(default=0)
    question25 = models.IntegerField(default=0)
    question26 = models.IntegerField(default=0)
    question27 = models.IntegerField(default=0)
    question28 = models.IntegerField(default=0)
    question29 = models.IntegerField(default=0)
    question30 = models.IntegerField(default=0)
    
    score = models.IntegerField(default=0)
    
    def calculate_total_score(self):
        question_values = [getattr(self, f'question{i}') for i in range(1, 31)]

        total_score = sum(question_values)
        
        self.score = total_score

    def save(self, *args, **kwargs):
        self.calculate_total_score()
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.uname
    
