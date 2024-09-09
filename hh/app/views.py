from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from app.forms import ResumeForm, VacancyForm
from app.models import Vacancy, Resume, Response


# Create your views here.

def vacancy_list(request):
    search_query = request.GET.get('q', '')
    vacancies = Vacancy.objects.filter(title__icontains=search_query)
    user_responses = Response.objects.filter(user=request.user).values_list('vacancy_id', flat=True)

    ctx = {
        'vacancies': vacancies,
        'user_responses': user_responses,
    }

    return render(request, 'app/vacancy_list.html', ctx)

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    has_responded = Response.objects.filter(user=request.user, vacancy=vacancy).exists()
    ctx = {
        'vacancy': vacancy,
        'has_responded': has_responded,
    }

    return render(request, 'app/vacancy_detail.html', ctx)


def profile(request):
    resumes = Resume.objects.filter(user=request.user)

    vacancies = Vacancy.objects.filter(user=request.user)
    ctx = {'resumes': resumes,
            'vacancies':vacancies
           }
    return render(request, 'app/profile.html', ctx)



def resume_create(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('profile')
    ctx = {'form': form}
    return render(request, 'app/resume_create.html', ctx)


def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    ctx = {'resume': resume}
    return render(request, 'app/resume_detail.html', ctx)



def resume_edit(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    form = ResumeForm(instance=resume)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('profile')
    ctx = {'form': form}
    return render(request, 'app/resume_edit.html', ctx)


def resume_delete(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        resume.delete()
        return redirect('profile')
    ctx = {'resume': resume}
    return render(request, 'app/profile.html', ctx)


def resume_list(request):
    vacancies = Vacancy.objects.filter(user=request.user)
    responses = Response.objects.filter(vacancy__in=vacancies)

    ctx = {
        'vacancies': vacancies,
        'responses': responses,
    }
    return render(request, 'app/resume_list.html', ctx)

def vacancy_create(request):
    form = VacancyForm()
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('profile')
    ctx = {'form': form}
    return render(request, 'app/vacancy_create.html', ctx)



def respond_to_vacancy(request, vacancy_id):

    vacancy = get_object_or_404(Vacancy, id=vacancy_id)

    resume = Resume.objects.filter(user=request.user).first()

    if not resume:

        return redirect('resume_create')
    response, created = Response.objects.get_or_create(
        user=request.user, resume=resume, vacancy=vacancy
    )
    return redirect('vacancy_detail', vacancy_id=vacancy.id)