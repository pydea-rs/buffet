from .models import Account
from django import forms


class RegisterForm(forms.ModelForm):
    # this for is related to register tab
    password = forms.CharField(widget=forms.PasswordInput())  # determine password field in the form
    confirm_password = forms.CharField(widget=forms.PasswordInput())   # determine confirm_password field in the form
    rules_accepted = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Account
        fields = ['username', 'contact', 'password']  # connect form with the Account model

    # RegisterForm class constructor
    # initiates form and gives styles to the fields to make well in the register tab
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # texts that will be shown in register text boxes
        placeholders = {'username': 'نام کاربری', 'contact': 'شماره تلفن یا ایمیل', 'password': 'رمزعبور', \
                        'confirm_password': 'تایید رمزعبور'}
        # this loop sets the styles of form members (text boxes and fields)
        for field in self.fields:
            if field != 'rules_accepted': # rules_accepted is a checkbox and doesnt need to get style
                # because rules_accepted is stylized before in line 9
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]

    # this method is for data validation, wrong account data will raise errors
    def clean(self):
        # get sent form's data to start checking
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get('username')
        contact = cleaned_data.get('contact')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        rules_accepted = cleaned_data.get('rules_accepted')

        if len(username) < 3:  # check username length
            raise forms.ValidationError('نام کاربری باید حداقل ۳ کاراکتر باشد.')
        if username.isdigit():  # check if username is valid text and not a number
            raise forms.ValidationError('نام کاربری نباید عدد باشد.')
        if len(password) < 6:  # check password is strong and at least 6 characters
            raise forms.ValidationError('رمزعبور باید حداقل ۶ کاراکتر باشد.')
        if password != confirm_password:  # check if both passwords match
            raise forms.ValidationError('رمزعبورها مطابقت ندارند.')
        if not rules_accepted:  # check if the account actually accepted website's rules
            raise forms.ValidationError('برای ثبت نام باید قوانین را بپذیرید')
        if contact and Account.objects.filter(contact=contact).count():  # if there is a account with this email/phone number
            raise forms.ValidationError("کاربری با این ایمیل یا شماره تلفن قبلا ثبت نام کرده است.")
        if username and Account.objects.filter(username=username).count():  # if there is a account with this username
            raise forms.ValidationError("کاربری با این نام کاربری قبلا ثبت نام کرده است.")
