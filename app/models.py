"""
Definition of models.
"""

from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(default=0)

    email = models.EmailField()
    phone = models.CharField(max_length=20)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)

    def __str__(self):           
        return "{0} {1}".format(self.first_name, self.last_name)








class WorkHistory(models.Model):
    place_of_work = models.CharField('Place Of Work', max_length=200)
    location = models.CharField('Location', max_length=200)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', null=True, blank=True)
    work_description = models.TextField('Description of Position', null=True, blank=True)
#    skills = models.ForeignKey(WorkSkill)
    def __str__(self):
        return "{0} ({1}-{2}".format(self.place_of_work, self.start_date, self.end_date)

    
class Company(models.Model):
    company_name = models.CharField('Company Name', max_length=200)
    contact_name = models.CharField('Contact Name', max_length=200, null=True, blank=True)
    contact_email = models.EmailField('Contact Email', null=True, blank=True)
    contact_phone = models.CharField('Contact Phone', max_length=20, null=True, blank=True)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)
    def __str__(self):           
        return self.company_name

class Resume(models.Model):
    about_me = models.TextField('About Me')
    position = models.CharField('What kind of Opportunity are you looking for?', max_length=200)
    contact = models.ForeignKey(Contact, null=True)
    company = models.ForeignKey(Company, null=True)
    work_histories = models.ManyToManyField(WorkHistory, null=True, blank=True)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)
    def __str__(self):           
        return "{0} {1}".format(self.company.company_name, self.position)

class Skill(models.Model):

    skill_name = models.CharField('Skill Name', max_length=200)
    def __str__(self):
        return self.skill_name

class WorkSkill(models.Model):
    SKILL_MINIMAL_EXPOSURE = 1
    SKILL_WORKING_KNOWLEDGE = 2
    SKILL_EXPERT = 3
    SKILL_NINJA = 4
    SKILL_PROFICIENCY_LEVELS = (
        (SKILL_MINIMAL_EXPOSURE, 'Minimal Exposure'),
        (SKILL_WORKING_KNOWLEDGE, 'Working Knowledge'),
        (SKILL_EXPERT, 'Expert'),
        (SKILL_NINJA, 'Ninja'),
        )
    skill = models.ForeignKey(Skill, null=True, blank=True)
    skill_proficiency_level = models.IntegerField(choices=SKILL_PROFICIENCY_LEVELS, default=SKILL_WORKING_KNOWLEDGE)
    work_history = models.ForeignKey(WorkHistory, null=True, blank=True)
    def __str__(self):
        return "{0} - {1}".format(self.skill.skill_name, self.SKILL_PROFICIENCY_LEVELS[self.skill_proficiency_level])

