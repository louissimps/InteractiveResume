from django.contrib import admin
from app.models import Resume, Contact, Company, Skill, WorkHistory, WorkSkill
from app.forms import RequiredInlineFormSet

class ResumeAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class WorkSkillTabularInline(admin.TabularInline):
    model = WorkSkill
    
    


class SkillAdmin(admin.ModelAdmin):
    pass

class WorkHistoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    inlines = [WorkSkillTabularInline,]


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Skill)
admin.site.register(WorkHistory, WorkHistoryAdmin)
