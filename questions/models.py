from django.db import models
from company.models import Company

class Questionnaire(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):

    QUESTION_TYPES = [
        ('multiple_choice', 'Multiple Choice'),
        ('single_choice', 'Single Choice'),
        ('text', 'Text'),
        ('boolean', 'Boolean'),
        ('rating', 'Rating'),
    ]

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text

