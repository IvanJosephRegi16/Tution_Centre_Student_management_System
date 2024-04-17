# forms.py



from .models import Subject, SESSION_CHOICES
from django import forms
from .models import Timetable
from .models import Note
from .models import StudentFeedback






class TimetableForm(forms.ModelForm):
    class_number = forms.ChoiceField(choices=[(i, f"Class {i}") for i in range(6, 11)])  # Classes 6 to 10

    class Meta:
        model = Timetable
        fields = ['class_number', 'day', 'subject']



SESSION_CHOICES = [
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
]

class SubjectForm(forms.ModelForm):
    session = forms.ChoiceField(choices=SESSION_CHOICES, required=True)

    class Meta:
        model = Subject
        fields = ['subject_name', 'class_name', 'session']



# from django import forms
# from .models import MyClass  # or any other model that ClassForm is associated with

# class ClassForm(forms.ModelForm):
#     class Meta:
#         model = MyClass  # Use the appropriate model
#         fields = ['field1', 'field2']  # Specify the fields


from django import forms
from .models import MyClass

class ClassForm(forms.ModelForm):
    class Meta:
        model = MyClass
        fields = ['class_name']  # Replace with actual fields of MyClass



class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()





from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['chapter', 'topic', 'pdf_file']


from django import forms
from .models import StudentFeedback, Subject

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = ['subject', 'feedback']  # Update to include subject instead of staff


