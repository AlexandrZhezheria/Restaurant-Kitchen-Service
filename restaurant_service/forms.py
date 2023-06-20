from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from typing import Union

from restaurant_service.models import Dish, Cook


def validate_years_of_experience(
    years_of_experience: int
) -> Union[int, ValidationError]:
    if years_of_experience == 0:
        raise ValidationError("years of experience cannot be 0")

    return years_of_experience


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self) -> Union[int, ValidationError]:
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class Cook_Years_of_experienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self) -> Union[int, ValidationError]:
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class CooksSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by username....."})
    )


class DishesSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by dishes....."})
    )


class DishTypesSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by DishType......"})
    )
