from django import forms

from .models import District, City, Region


class RegionCreationForm(forms.ModelForm):
    district = forms.ModelChoiceField(empty_label="Select District", to_field_name='name',queryset=District.objects.all())
    city = forms.ModelChoiceField(empty_label="Select City", to_field_name='city',queryset=City.objects.all())

    class Meta:
        model = Region
        fields = ['district', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.all()

        if 'district' in self.data:
            try:
                district = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district=district).order_by('city')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')
