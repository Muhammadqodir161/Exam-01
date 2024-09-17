from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=20)
    def str(self):
        return (f"{self.first_name}"
                f" {self.last_name}")

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def str(self):
        return self.name

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def str(self):
        return f"{self.subject.name},{self.date}"

class QuestionType(models.TextChoices):
    MULTIPLE_CHOICE = 'MC', 'Multiple Choice'
    SHORT_ANSWER = 'SA', 'Short Answer'


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(
        max_length=2, choices=QuestionType.choices, default=QuestionType.MULTIPLE_CHOICE
    )

    def str(self):
        return self.text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def str(self):
        return self.text