"""
Definition of models.
"""

from django.db import models
from tinymce import models as tinymce_models
from autoslug import AutoSlugField


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(default=0)

    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True, blank=True)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Skill(models.Model):
    skill_name = models.CharField('Skill Name', max_length=200)

    def __str__(self):
        return self.skill_name


class WorkHistory(models.Model):
    is_current = models.NullBooleanField("Is Current Position")

    place_of_work = models.CharField('Place Of Work', max_length=200)
    location = models.CharField('Location', max_length=200)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', null=True, blank=True)
    position = models.CharField("Position Title", max_length=200, null=True, blank=True)
    work_description = tinymce_models.HTMLField('Description of Position', null=True, blank=True)
    slug = AutoSlugField(populate_from='place_of_work', always_update=True, unique_with=('start_date__year',))

    work_skills = models.ManyToManyField(Skill, through="WorkSkill", verbose_name="Skills Used", null=True, blank=True)


    @models.permalink
    def get_absolute_url(self):
        return ('workhistory', (), {
            'id': self.id,
            'slug': self.slug,
        })

    @staticmethod
    def autocomplete_search_fields():
        return ('place_of_work__icontains',)

    def get_dates_string(self):
        return "({0}) - ({1})".format(self.start_date, self.end_date)

    def __str__(self):
        return "{0} {1}".format(self.place_of_work, self.get_dates_string())





class WorkSkill(models.Model):
    SKILL_MINIMAL_EXPOSURE = 0
    SKILL_WORKING_KNOWLEDGE = 1
    SKILL_EXPERT = 2
    SKILL_NINJA = 3
    SKILL_PROFICIENCY_LEVELS = (
        (SKILL_MINIMAL_EXPOSURE, 'Minimal Exposure'),
        (SKILL_WORKING_KNOWLEDGE, 'Working Knowledge'),
        (SKILL_EXPERT, 'Expert'),
        (SKILL_NINJA, 'Ninja'),
    )



    skill = models.ForeignKey(Skill)
    skill_proficiency_level = models.IntegerField(choices=SKILL_PROFICIENCY_LEVELS, default=SKILL_WORKING_KNOWLEDGE)
    work_history = models.ForeignKey(WorkHistory)

    def __str__(self):
        return self.skill.skill_name

    def get_level(self):
        return self.SKILL_PROFICIENCY_LEVELS[self.skill_proficiency_level]

    def get_label_class(self):
        b = self.SKILL_PROFICIENCY_LEVELS[self.skill_proficiency_level][1]
        if b == 'Ninja':
            return 'success'
        elif b == 'Expert':
            return 'primary'
        elif b == 'Working Knowledge':
            return 'warning'
        elif b == 'Minimal Exposure':
            return 'danger'


class Education(models.Model):
    school_name = models.CharField('School Name', max_length=200)
    school_location = models.CharField('School Location', max_length=200)
    coursework = models.TextField('School Name', max_length=200)

    def __str__(self):
        return "{0}".format(self.school_name)


class Company(models.Model):
    company_name = models.CharField('Company Name', max_length=200)
    contact_name = models.CharField('Contact Name', max_length=200, null=True, blank=True)
    contact_email = models.EmailField('Contact Email', null=True, blank=True)
    contact_phone = models.CharField('Contact Phone', max_length=20, null=True, blank=True)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)

    @staticmethod
    def autocomplete_search_fields():
        return ('company_name__icontains',)

    def __str__(self):
        return self.company_name


class Resume(models.Model):
    is_default = models.NullBooleanField("Is This the Default Resume you want to show?")
    about_me = tinymce_models.HTMLField('About Me')
    position = models.CharField('What kind of Opportunity are you looking for?', max_length=200)
    description = tinymce_models.HTMLField('Vision Statement:', null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True)
    company = models.ForeignKey(Company, null=True)
    work_histories = models.ManyToManyField(WorkHistory, null=True, blank=True)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)

    def __str__(self):
        return "{0} {1}".format(self.company.company_name, self.position)


class Application(models.Model):
    bootstrap_theme = models.CharField("Twitter Bootstrap image", max_length=200, null=False, blank=False)

