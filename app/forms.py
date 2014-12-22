"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.forms.models import BaseInlineFormSet
from app.models import WorkSkill, Skill, WorkHistory
from django.contrib.admin.widgets import FilteredSelectMultiple, RelatedFieldWidgetWrapper
from django.db.models.fields.related import ManyToManyRel

__all__ = ('RequiredInlineFormSet',)

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))




class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """

        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form





# class WorkSkillForm(forms.ModelForm):
#     workskills = forms.ModelMultipleChoiceField(
#         queryset=Skill.objects.all().order_by("skill_name"),
#         required=False,
#         widget=FilteredSelectMultiple(
#             verbose_name="workskills",
#             is_stacked=False
#         )
#
#     )
#
#     class Meta:
#         model = WorkSkill
#
#     def __init__(self, *args, **kwargs):
#         super(WorkSkillForm, self).__init__(*args, **kwargs)
#         if(self.instance.pk):
#             self.initial['workskills'] = self.instance.workskills.all()
#             rel = ManyToManyRel(WorkHistory)
#             self.fields['workskills'].widget = RelatedFieldWidgetWrapper(self.fields['workskills'].widget, rel, admin.site)
#
#     def save(self, commit=True):
#         workskill = super(WorkSkillForm, self).save(commit=False)
#
#         if commit:
#             workskill.save()
#
#         if(workskill.pk):
#             workskill.workskills = self.cleaned_data['workskills']
#             self.save_m2m()
#
#         return workskill


