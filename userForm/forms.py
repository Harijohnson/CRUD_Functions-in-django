from django import forms
from userForm.models import user 

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = user
        fields = ['username','email','password']



'''<form action="" method="post">
    <ul class="contactList">
        <li id="subject" class="contact">{{ form.subject }}</li>
        <li id="email" class="contact">{{ form.email }}</li>
        <li id="message" class="contact">{{ form.message }}</li>
    </ul>
    <input type="submit" value="Submit">
</form>'''