from django import forms

from app.models import Resume, Vacancy


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'name', 'surname', 'patronymic', 'date_of_birth', 'email', 'skills', 'experience', 'education')


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'company_name', 'salary', 'required_skills', 'responsibilities', 'address')