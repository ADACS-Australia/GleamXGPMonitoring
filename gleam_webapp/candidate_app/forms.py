from django import forms
from django.core.exceptions import ValidationError
from . import models

# Add a default to candidate type choices
CAND_TYPE_CHOICES = models.CAND_TYPE_CHOICES
N = 'None'
CAND_TYPE_CHOICES += ((N,   'All columns'),)

ORDER_BY_CHOICES = (
    ('id','ID'),
    ('avg_rating', 'Rating'),
    ('num_ratings', 'Count'),
    ('notes', 'Notes'),
    ('T_count', 'N Tranisent'),
    ('AP_count', 'N Airplane'),
    ('RFI_count', 'N RFI'),
    ('SL_count', 'N Sidelobe'),
    ('A_count', 'N Alias'),
    ('CC_count', 'N CHG Center'),
    ('S_count', 'N Scintillation'),
    ('P_count', 'N Pulsar'),
    ('O_count', 'N Other'),
    ('ra_hms', 'RA'),
    ('dec_dms', 'Dec'),
    ('obs_id', 'Obs ID'),
)

ASC_DEC_CHOICES = (
    ('', 'Ascending'),
    ('-', 'Decending')
)

class CanidateFilterForm(forms.Form):
    rating_cutoff = forms.FloatField(required=False)
    observation_id = forms.ModelChoiceField(models.Observation.objects.all(), empty_label="All observations", required=False)
    column_display = forms.ChoiceField(choices=CAND_TYPE_CHOICES, required=False, initial='None')
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, required=False, initial='avg_rating')
    asc_dec = forms.ChoiceField(choices=ASC_DEC_CHOICES, required=False, initial='-')
    ra_hms = forms.CharField(required=False, max_length=64)
    dec_dms = forms.CharField(required=False, max_length=64)
    search_radius_arcmin = forms.FloatField(required=False, initial=2)

SESSION_ORDER_CHOICES = (
    ('rand', 'Random'),
    ('new',  'Newest'),
    ('old',  'Oldest'),
    ('brig', 'Brightest'),
    ('faint','Faintest'),
)
SESSION_FILTER_CHOICES = (
    ('unrank', 'Unranked Candidates'),
    ('old',    'Candidates Not Ranked Recently'),
    ('all',    'All Candidates'),
)
class SessionSettingsForm(forms.Form):
    ordering  = forms.ChoiceField(choices=SESSION_ORDER_CHOICES,  required=False, initial='rand')
    filtering = forms.ChoiceField(choices=SESSION_FILTER_CHOICES, required=False, initial='unrank')
    exclude_87  = forms.BooleanField(required=False)
    exclude_118 = forms.BooleanField(required=False)
    exclude_154 = forms.BooleanField(required=False)
    exclude_184 = forms.BooleanField(required=False)
    exclude_200 = forms.BooleanField(required=False)
    exclude_215 = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("filtering") == 'all' and cleaned_data.get("ordering") != 'rand':
            raise ValidationError(
                "ERROR: You can not order all candidates by anything other than random as it will always give you the same candidate. "
                "Please either order randomly or filter by candidates not ranked recently."
            )
