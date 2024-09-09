from django.contrib import admin

from app.models import Resume, Vacancy

# Register your models here.


admin.site.register([Resume, Vacancy])