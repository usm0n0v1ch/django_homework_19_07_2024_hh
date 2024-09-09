from django.db import models

# Create your models here.


class Resume(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, related_name='responses', null=True, blank=True)  # related_name для обратной связи



class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    required_skills = models.TextField()
    responsibilities = models.TextField()
    address = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
