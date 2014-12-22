from django.contrib import admin
from os import path
from django.conf import settings

from app.models import *
from app.forms import RequiredInlineFormSet#, WorkSkillForm

class ResumeAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass

class WorkSkillTabularInline(admin.TabularInline):
    model = WorkSkill
    extra = 5
    min_num = 10

class WorkSkillAdmin(admin.ModelAdmin):
    pass

class WorkHistoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    inlines = [
        WorkSkillTabularInline,
    ]

admin.site.register(Resume, ResumeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Application)
admin.site.register(WorkHistory, WorkHistoryAdmin)
