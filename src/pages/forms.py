from django import forms
from django.utils.translation import gettext_lazy as _
from .models import HEPoi

class EOI_Form(forms.Form):
    first_name = forms.CharField(max_length = 32, help_text=_('First name'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('First name')}), error_messages={'required': _('Please enter your first name')})

    last_name = forms.CharField(max_length = 32, help_text=_('Last name'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last name')}), error_messages={'required': _('Please enter your last name')})

    organization_pozition = forms.CharField(max_length = 64, help_text=_('Organization pozition'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Position in organisation')}), error_messages={'required': _('Please enter your pozition in the organization')})

    email = forms.EmailField(help_text=_('Email address'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Email')}), error_messages={'required': _('Please enter your email')})

    organization_name = forms.CharField(max_length = 64, help_text=_('Organization name'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Organization name')}), error_messages={'required': _('Please enter your organization name')})
    
    organization_acronym = forms.CharField(max_length = 16, help_text=_('Organization acronym'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Organization acronym')}), error_messages={'required': _('Please enter your organization acronym')})
    
    organization_short_description = forms.CharField(max_length = 1024, help_text=_('Organization short description'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'placeholder': _('Short description of the organization (max. 1000 characters)')}), error_messages={'required': _('Please enter a short description of your organization')})
    
    research_fields = forms.CharField(max_length = 256, help_text=_('Research fields'), widget=forms.Textarea(attrs={'class': 'form-control','rows':2, 'placeholder': _('Research Field(s) (Please indicate the research field(s) most relevant for Horizon Europe proposals)')}), error_messages={'required': _('Please enter research fields')})
    
    key_words = forms.CharField(max_length = 512, help_text=_('Key words'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'placeholder': _('Key words (Please mention up to 10 key words best describing your expertis and research field(s))')}), error_messages={'required': _('Please enter keywords')})
   
    try:
        programm_of_interest_CHOICES = HEPoi.objects.all()
    except: 
        programm_of_interest_CHOICES = HEPoi.objects.none()
    hepoi = forms.ModelMultipleChoiceField(
        queryset = programm_of_interest_CHOICES,
        widget  = forms.CheckboxSelectMultiple(attrs={'class': 'cCdhN7'}),
        error_messages={'required': _('Please select at least one programm of interest')}
    )
    
    department_short_description = forms.CharField(max_length = 2048, help_text=_('Department short description'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': _('Short description of the department: Please provide a description of a department / school, that intends to participate in the Horizon Europe proposal. Please mention here: relevant expertise, relevant infrastructure, relevant existing networks / partnerships / collaborations (everything that shows the strengths of your department as a partner in a Horizon Europe  proposal) (max. 2000 characters).')}), error_messages={'required': _('Please enter a short description of your department')})
    
    skills_competences = forms.CharField(max_length = 1024, help_text=_('Skills and competences'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'placeholder': _('Skills & Competences: Please indicate skills and competences that are relevant for your research field(s) and are part of your expertise in the area (max. 1000 characters).')}), error_messages={'required': _('Please enter skills and competences')})
    
    scientific_publication = forms.CharField(max_length = 2048, help_text=_('Scientific publications'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'placeholder': _('Scientific Publications: Please provide a list of the most important and relevant publications and patents in your field of expertise (maximum of 2000 characters).')}), error_messages={'required': _('Please enter your scientific publications')})
    
    related_projects = forms.CharField(max_length = 2048, help_text=_('Related projects'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': _('Previous related projects: Please provide a list of the most important and relevant projects in your field of expertise (international / EU / national). The projects listed here should be not older than 5 years (from 2018 and newer). Please indicate title of projects, funding body, duration of project. (max. 2000 characters).')}), error_messages={'required': _('Please enter related projects')})
    
    achievements = forms.CharField(max_length = 2048, help_text=_('Department short description'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': _('Significant Achievements (if the case): Please provide a list of the most important and relevant achievements in your field of expertise (international / EU / national). For example, significant exhibitions, conferences, actions your organised. The actions listed here should be not older than 5 years (from 2018 and newer). Please indicate title of the event and the year (max. 2000 characters).')}), error_messages={'required': _('Please enter related achievements')})
    
    other = forms.CharField(max_length = 1024, help_text=_('Other information'), widget=forms.Textarea(attrs={'class': 'form-control', 'rows':2, 'placeholder': _('Other: Please list here any other added value you can bring as a potential partner in a Horizon Europe proposal (for example, collaboration with civil society organisations, activities that involved citizens, etc.) (max. 1000 characters).')}), required=False)

