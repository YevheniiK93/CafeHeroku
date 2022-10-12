from django import forms
from manager.models import UserReservations


class UserReservationsForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100,
        min_length=4,
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "name",
            'class': "form-control",
            'id': "name",
            'placeholder': "Your Name",
            'data-rule': "minlen:4",
            'data-msg': "Please enter at least 4 chars"}))

    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'type': "email",
            'class': "form-control",
            'name': "email",
            'id': "email",
            'placeholder': "Your Email",
            'data-rule': "email",
            'data-msg': "Please enter a valid email"}))

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "form-control",
            'name': "phone",
            'id': "phone",
            'placeholder': "Your Phone",
            'data-rule': "minlen:10",
            'data-msg': "Please enter at least 10 chars"}))

    num_of_people = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': "number",
            'class': "form-control",
            'name': "people",
            'id': "people",
            'placeholder': "Number of guests",
            'data-rule': "minlen:1",
            'data-msg': "Input number of places"}))

    order_date = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={
            'type': "text",
            'name': "date",
            'class': "form-control",
            'id': "date",
            'placeholder': "Order date",
            'data-rule': "minlen:6",
            'data-msg': "Input date in d/m/y-format"}))

    order_time = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "form-control",
            'name': "time",
            'id': "time",
            'placeholder': "Time or order",
            'data-rule': "minlen:4",
            'data-msg': "Input visit time"}))

    message = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'type': "message",
            'class': "form-control",
            'name': "message",
            'rows': "5",
            'placeholder': "Message"}))

    class Meta:
        model = UserReservations
        fields = ('name', 'email', 'phone', "num_of_people", 'order_date', 'order_time', 'message')
