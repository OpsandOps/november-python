# Django Forms Complete Guide

A comprehensive guide to implementing Django forms using ModelForms and custom forms, with examples based on the polls application.

---

## Table of Contents
1. [Introduction to Django Forms](#introduction)
2. [ModelForms - Forms from Models](#modelforms)
3. [Custom Forms - Building from Scratch](#custom-forms)
4. [Form Validation](#form-validation)
5. [Rendering Forms in Templates](#rendering-forms)
6. [Processing Form Data in Views](#processing-forms-in-views)
7. [Advanced Examples](#advanced-examples)

---

## Introduction to Django Forms {#introduction}

Django forms handle three main tasks:
- **Rendering** form fields as HTML
- **Validating** user input
- **Processing** cleaned data

There are two main approaches:
1. **ModelForms** - Automatically generated from Django models
2. **Custom Forms** - Manually defined form fields

---

## ModelForms - Forms from Models {#modelforms}

ModelForms automatically create form fields based on your model structure.

### Basic ModelForm Example

Based on our `Question` and `Choice` models, here's how to create ModelForms:

```python
# polls/forms.py
from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    """
    ModelForm for creating/editing Question objects.
    Automatically generates fields from the Question model.
    """
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        # Or use '__all__' to include all fields
        # fields = '__all__'
        
        # Exclude specific fields
        # exclude = ['author']
        
        # Custom labels
        labels = {
            'question_text': 'Enter your question',
            'pub_date': 'Publication Date',
        }
        
        # Custom help text
        help_texts = {
            'question_text': 'Maximum 255 characters',
            'pub_date': 'Select when this question should be published',
        }
        
        # Custom error messages
        error_messages = {
            'question_text': {
                'required': 'Please enter a question',
                'max_length': 'Question is too long (max 255 characters)',
            },
        }
        
        # Custom widgets (HTML input types)
        widgets = {
            'question_text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Type your question here...',
                'class': 'form-control',
            }),
            'pub_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
        }
```

### ModelForm with Foreign Key

```python
class ChoiceForm(forms.ModelForm):
    """
    ModelForm for Choice model with ForeignKey to Question.
    """
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'question']
        
        widgets = {
            'choice_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter choice text',
            }),
            'votes': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
            }),
            'question': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
```

### ModelForm with Custom Fields

You can add extra fields not in the model:

```python
class QuestionFormWithExtras(forms.ModelForm):
    # Extra field not in the model
    agree_to_terms = forms.BooleanField(
        required=True,
        label='I agree to the terms and conditions'
    )
    
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
    
    def save(self, commit=True, user=None):
        """
        Override save to add the author (current user)
        """
        question = super().save(commit=False)
        if user:
            question.author = user
        if commit:
            question.save()
        return question
```

### Using ModelForm in Views

```python
# polls/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, ChoiceForm
from .models import Question

def create_question(request):
    """
    View to create a new question using ModelForm.
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Save the form and set the author
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('polls:detail', question_id=question.id)
    else:
        form = QuestionForm()
    
    return render(request, 'polls/question_form.html', {'form': form})


def edit_question(request, question_id):
    """
    View to edit an existing question.
    """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        # Pass instance to populate form with existing data
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('polls:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'polls/question_form.html', {
        'form': form,
        'question': question,
    })


def add_choice_to_question(request, question_id):
    """
    Add a choice to a specific question.
    """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('polls:detail', question_id=question.id)
    else:
        # Pre-populate the question field
        form = ChoiceForm(initial={'question': question})
    
    return render(request, 'polls/choice_form.html', {
        'form': form,
        'question': question,
    })
```

---

## Custom Forms - Building from Scratch {#custom-forms}

Custom forms give you complete control over form fields without being tied to a model.

### Basic Custom Form

```python
# polls/forms.py
from django import forms

class ContactForm(forms.Form):
    """
    Custom form for contacting the poll administrator.
    """
    name = forms.CharField(
        max_length=100,
        label='Your Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        })
    )
    
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com',
        })
    )
    
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Type your message here...',
        })
    )
    
    priority = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
```

### All Field Types Example

```python
class AllFieldTypesForm(forms.Form):
    """
    Demonstrates all common Django form field types.
    """
    # Text inputs
    text_field = forms.CharField(max_length=100)
    email_field = forms.EmailField()
    url_field = forms.URLField()
    slug_field = forms.SlugField()
    
    # Number inputs
    integer_field = forms.IntegerField()
    float_field = forms.FloatField()
    decimal_field = forms.DecimalField(max_digits=5, decimal_places=2)
    
    # Boolean
    boolean_field = forms.BooleanField(required=False)
    
    # Choice fields
    choice_field = forms.ChoiceField(choices=[
        ('opt1', 'Option 1'),
        ('opt2', 'Option 2'),
    ])
    
    multiple_choice = forms.MultipleChoiceField(choices=[
        ('choice1', 'Choice 1'),
        ('choice2', 'Choice 2'),
        ('choice3', 'Choice 3'),
    ])
    
    # Date and time
    date_field = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    time_field = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    datetime_field = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    
    # File upload
    file_field = forms.FileField()
    image_field = forms.ImageField(required=False)
    
    # Text area
    textarea_field = forms.CharField(widget=forms.Textarea)
    
    # Hidden field
    hidden_field = forms.CharField(widget=forms.HiddenInput())
```

### Vote Form Example (Based on Polls App)

```python
class VoteForm(forms.Form):
    """
    Custom form for voting on a poll question.
    """
    choice = forms.ModelChoiceField(
        queryset=None,  # Will be set in __init__
        widget=forms.RadioSelect,
        empty_label=None,
        label='Select your choice',
    )
    
    def __init__(self, question, *args, **kwargs):
        """
        Initialize form with choices for a specific question.
        """
        super().__init__(*args, **kwargs)
        # Set queryset to choices for this question
        self.fields['choice'].queryset = question.choice_set.all()
        self.fields['choice'].label_from_instance = lambda obj: obj.choice_text
```

### Search Form Example

```python
class QuestionSearchForm(forms.Form):
    """
    Custom form for searching questions.
    """
    query = forms.CharField(
        max_length=255,
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search questions...',
        })
    )
    
    date_from = forms.DateField(
        required=False,
        label='From Date',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
    )
    
    date_to = forms.DateField(
        required=False,
        label='To Date',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
    )
    
    author = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Author username',
        })
    )
```

### Using Custom Forms in Views

```python
# polls/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import VoteForm, ContactForm, QuestionSearchForm
from .models import Question, Choice

def vote(request, question_id):
    """
    Handle voting using a custom form.
    """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = VoteForm(question, request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choice']
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('polls:results', question_id=question.id)
    else:
        form = VoteForm(question)
    
    return render(request, 'polls/vote.html', {
        'form': form,
        'question': question,
    })


def contact(request):
    """
    Handle contact form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            priority = form.cleaned_data['priority']
            
            # Send email or save to database
            # send_mail(subject, message, email, ['admin@example.com'])
            
            return render(request, 'polls/contact_success.html', {
                'name': name,
            })
    else:
        form = ContactForm()
    
    return render(request, 'polls/contact.html', {'form': form})


def search_questions(request):
    """
    Search questions using custom form.
    """
    form = QuestionSearchForm(request.GET or None)
    results = None
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        author = form.cleaned_data.get('author')
        
        # Start with all questions
        results = Question.questionManager.all()
        
        # Apply filters
        if query:
            results = results.filter(question_text__icontains=query)
        if date_from:
            results = results.filter(pub_date__gte=date_from)
        if date_to:
            results = results.filter(pub_date__lte=date_to)
        if author:
            results = results.filter(author__username__icontains=author)
    
    return render(request, 'polls/search.html', {
        'form': form,
        'results': results,
    })
```

---

## Form Validation {#form-validation}

Django provides multiple levels of validation.

### Field-Level Validation

```python
class QuestionFormWithValidation(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
    
    def clean_question_text(self):
        """
        Custom validation for question_text field.
        Method name: clean_<field_name>
        """
        question_text = self.cleaned_data['question_text']
        
        # Check minimum length
        if len(question_text) < 10:
            raise forms.ValidationError(
                'Question must be at least 10 characters long.'
            )
        
        # Check for prohibited words
        prohibited_words = ['spam', 'inappropriate']
        for word in prohibited_words:
            if word.lower() in question_text.lower():
                raise forms.ValidationError(
                    f'Question contains prohibited word: {word}'
                )
        
        # Check for duplicate questions
        if Question.questionManager.filter(
            question_text__iexact=question_text
        ).exists():
            raise forms.ValidationError(
                'A question with this text already exists.'
            )
        
        return question_text
    
    def clean_pub_date(self):
        """
        Validate publication date is not in the past.
        """
        from datetime import datetime
        pub_date = self.cleaned_data['pub_date']
        
        if pub_date and pub_date < datetime.now():
            raise forms.ValidationError(
                'Publication date cannot be in the past.'
            )
        
        return pub_date
```

### Form-Level Validation

```python
class ChoiceFormWithValidation(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'question']
    
    def clean(self):
        """
        Cross-field validation.
        Called after all field-level clean methods.
        """
        cleaned_data = super().clean()
        choice_text = cleaned_data.get('choice_text')
        question = cleaned_data.get('question')
        votes = cleaned_data.get('votes')
        
        # Validate votes are not negative
        if votes and votes < 0:
            raise forms.ValidationError('Votes cannot be negative.')
        
        # Check if choice already exists for this question
        if choice_text and question:
            existing = Choice.choice.filter(
                question=question,
                choice_text__iexact=choice_text
            )
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            
            if existing.exists():
                raise forms.ValidationError(
                    f'Choice "{choice_text}" already exists for this question.'
                )
        
        return cleaned_data
```

### Custom Validators

```python
from django.core.exceptions import ValidationError

def validate_no_numbers(value):
    """
    Custom validator to ensure text has no numbers.
    """
    if any(char.isdigit() for char in value):
        raise ValidationError(
            'Text cannot contain numbers.',
            code='contains_numbers'
        )

def validate_min_words(value, min_words=5):
    """
    Validate minimum word count.
    """
    word_count = len(value.split())
    if word_count < min_words:
        raise ValidationError(
            f'Text must contain at least {min_words} words. You entered {word_count}.',
            code='too_few_words'
        )

class QuestionFormWithCustomValidators(forms.ModelForm):
    question_text = forms.CharField(
        max_length=255,
        validators=[validate_no_numbers]
    )
    
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
    
    def clean_question_text(self):
        question_text = self.cleaned_data['question_text']
        validate_min_words(question_text, min_words=3)
        return question_text
```

---

## Rendering Forms in Templates {#rendering-forms}

Multiple ways to render forms in Django templates.

### Template for ModelForm

```html
<!-- polls/templates/polls/question_form.html -->
{% extends 'polls/base.html' %}

{% block content %}
<div class="container">
    <h2>{% if question %}Edit{% else %}Create{% endif %} Question</h2>
    
    <form method="post">
        {% csrf_token %}
        
        <!-- Method 1: Render entire form automatically -->
        {{ form.as_p }}
        
        <button type="submit" class="btn btn-primary">Save Question</button>
        <a href="{% url 'polls:index' %}" class="btn btn-secondary">Cancel</a>
    </form>
</div>
{% endblock %}
```

### Different Rendering Methods

```html
<!-- Method 1: as_p (paragraph tags) -->
{{ form.as_p }}

<!-- Method 2: as_table (table rows) -->
<table>
    {{ form.as_table }}
</table>

<!-- Method 3: as_ul (list items) -->
<ul>
    {{ form.as_ul }}
</ul>

<!-- Method 4: Manual field rendering (most control) -->
<form method="post">
    {% csrf_token %}
    
    <div class="form-group">
        <label for="{{ form.question_text.id_for_label }}">
            {{ form.question_text.label }}
        </label>
        {{ form.question_text }}
        
        {% if form.question_text.errors %}
            <div class="alert alert-danger">
                {{ form.question_text.errors }}
            </div>
        {% endif %}
        
        {% if form.question_text.help_text %}
            <small class="form-text text-muted">
                {{ form.question_text.help_text }}
            </small>
        {% endif %}
    </div>
    
    <div class="form-group">
        <label for="{{ form.pub_date.id_for_label }}">
            {{ form.pub_date.label }}
        </label>
        {{ form.pub_date }}
        
        {% if form.pub_date.errors %}
            <div class="alert alert-danger">
                {{ form.pub_date.errors }}
            </div>
        {% endif %}
    </div>
    
    <!-- Display non-field errors -->
    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {{ form.non_field_errors }}
        </div>
    {% endif %}
    
    <button type="submit">Submit</button>
</form>
```

### Vote Form Template (Custom Form)

```html
<!-- polls/templates/polls/vote.html -->
{% extends 'polls/base.html' %}

{% block content %}
<div class="container">
    <h2>{{ question.question_text }}</h2>
    <p class="text-muted">Published: {{ question.pub_date }}</p>
    
    <form method="post">
        {% csrf_token %}
        
        {% if form.errors %}
            <div class="alert alert-danger">
                <strong>Please correct the errors below:</strong>
                {{ form.errors }}
            </div>
        {% endif %}
        
        <div class="form-group">
            {% for radio in form.choice %}
                <div class="form-check">
                    {{ radio }}
                </div>
            {% endfor %}
        </div>
        
        <button type="submit" class="btn btn-primary">Vote</button>
    </form>
</div>
{% endblock %}
```

### Contact Form Template

```html
<!-- polls/templates/polls/contact.html -->
{% extends 'polls/base.html' %}

{% block content %}
<div class="container">
    <h2>Contact Us</h2>
    
    <form method="post" class="needs-validation" novalidate>
        {% csrf_token %}
        
        {% for field in form %}
            <div class="form-group mb-3">
                <label for="{{ field.id_for_label }}" class="form-label">
                    {{ field.label }}
                    {% if field.field.required %}
                        <span class="text-danger">*</span>
                    {% endif %}
                </label>
                
                {{ field }}
                
                {% if field.errors %}
                    {% for error in field.errors %}
                        <div class="invalid-feedback d-block">
                            {{ error }}
                        </div>
                    {% endfor %}
                {% endif %}
                
                {% if field.help_text %}
                    <small class="form-text text-muted">
                        {{ field.help_text }}
                    </small>
                {% endif %}
            </div>
        {% endfor %}
        
        <button type="submit" class="btn btn-primary">Send Message</button>
    </form>
</div>
{% endblock %}
```

---

## Processing Form Data in Views {#processing-forms-in-views}

### Complete CRUD Example with ModelForm

```python
# polls/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import QuestionForm, ChoiceForm
from .models import Question, Choice

@login_required
def create_question(request):
    """Create a new question."""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Question created successfully!')
            return redirect('polls:detail', question_id=question.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = QuestionForm()
    
    return render(request, 'polls/question_form.html', {'form': form})


@login_required
def edit_question(request, question_id):
    """Edit an existing question."""
    question = get_object_or_404(Question, pk=question_id)
    
    # Check if user is the author
    if question.author != request.user:
        messages.error(request, 'You can only edit your own questions.')
        return redirect('polls:detail', question_id=question_id)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated successfully!')
            return redirect('polls:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'polls/question_form.html', {
        'form': form,
        'question': question,
    })


@login_required
def delete_question(request, question_id):
    """Delete a question."""
    question = get_object_or_404(Question, pk=question_id)
    
    if question.author != request.user:
        messages.error(request, 'You can only delete your own questions.')
        return redirect('polls:detail', question_id=question_id)
    
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Question deleted successfully!')
        return redirect('polls:index')
    
    return render(request, 'polls/question_confirm_delete.html', {
        'question': question,
    })
```

### Processing Custom Form with File Upload

```python
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)

def feedback(request):
    """Handle feedback form with file upload."""
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            attachment = form.cleaned_data.get('attachment')
            
            # Process the attachment
            if attachment:
                # Save file
                import os
                from django.core.files.storage import default_storage
                file_name = default_storage.save(
                    f'feedback/{attachment.name}',
                    attachment
                )
                file_url = default_storage.url(file_name)
            
            # Send email or save to database
            messages.success(request, 'Thank you for your feedback!')
            return redirect('polls:index')
    else:
        form = FeedbackForm()
    
    return render(request, 'polls/feedback.html', {'form': form})
```

---

## Advanced Examples {#advanced-examples}

### Formsets - Multiple Forms

```python
from django.forms import formset_factory, modelformset_factory

# Create multiple choice forms at once
ChoiceFormSet = modelformset_factory(
    Choice,
    fields=['choice_text', 'votes'],
    extra=3,  # Number of empty forms
    can_delete=True
)

def manage_choices(request, question_id):
    """Manage multiple choices for a question using formsets."""
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        formset = ChoiceFormSet(
            request.POST,
            queryset=question.choice_set.all()
        )
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.question = question
                instance.save()
            
            # Handle deletions
            for obj in formset.deleted_objects:
                obj.delete()
            
            messages.success(request, 'Choices updated successfully!')
            return redirect('polls:detail', question_id=question.id)
    else:
        formset = ChoiceFormSet(queryset=question.choice_set.all())
    
    return render(request, 'polls/manage_choices.html', {
        'formset': formset,
        'question': question,
    })
```

### Inline Formsets (Parent-Child Relationship)

```python
from django.forms import inlineformset_factory

# Create inline formset for Question and its Choices
ChoiceInlineFormSet = inlineformset_factory(
    Question,  # Parent model
    Choice,    # Child model
    fields=['choice_text', 'votes'],
    extra=3,
    can_delete=True
)

def create_question_with_choices(request):
    """Create a question and its choices together."""
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question.save()
            
            choice_formset = ChoiceInlineFormSet(
                request.POST,
                instance=question
            )
            if choice_formset.is_valid():
                choice_formset.save()
                messages.success(request, 'Question and choices created!')
                return redirect('polls:detail', question_id=question.id)
    else:
        question_form = QuestionForm()
        choice_formset = ChoiceInlineFormSet()
    
    return render(request, 'polls/question_with_choices_form.html', {
        'question_form': question_form,
        'choice_formset': choice_formset,
    })
```

### Form with Dynamic Fields

```python
class DynamicQuestionForm(forms.Form):
    """Form with dynamically generated fields."""
    
    def __init__(self, *args, **kwargs):
        num_choices = kwargs.pop('num_choices', 3)
        super().__init__(*args, **kwargs)
        
        # Add question field
        self.fields['question_text'] = forms.CharField(
            max_length=255,
            widget=forms.Textarea(attrs={'rows': 3})
        )
        
        # Dynamically add choice fields
        for i in range(num_choices):
            self.fields[f'choice_{i}'] = forms.CharField(
                max_length=200,
                label=f'Choice {i+1}',
                required=False
            )

def create_question_dynamic(request):
    """Create question with dynamic number of choices."""
    num_choices = int(request.GET.get('num_choices', 4))
    
    if request.method == 'POST':
        form = DynamicQuestionForm(request.POST, num_choices=num_choices)
        if form.is_valid():
            # Create question
            question = Question.questionManager.create(
                question_text=form.cleaned_data['question_text'],
                pub_date=timezone.now(),
                author=request.user
            )
            
            # Create choices
            for i in range(num_choices):
                choice_text = form.cleaned_data.get(f'choice_{i}')
                if choice_text:
                    Choice.choice.create(
                        question=question,
                        choice_text=choice_text,
                        votes=0
                    )
            
            return redirect('polls:detail', question_id=question.id)
    else:
        form = DynamicQuestionForm(num_choices=num_choices)
    
    return render(request, 'polls/dynamic_form.html', {
        'form': form,
        'num_choices': num_choices,
    })
```

### AJAX Form Submission

```python
from django.http import JsonResponse

def ajax_vote(request, question_id):
    """Handle vote submission via AJAX."""
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        choice_id = request.POST.get('choice')
        
        try:
            selected_choice = question.choice_set.get(pk=choice_id)
        except Choice.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Invalid choice'
            }, status=400)
        
        selected_choice.votes += 1
        selected_choice.save()
        
        return JsonResponse({
            'success': True,
            'new_votes': selected_choice.votes,
            'message': 'Vote recorded successfully!'
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
```

```html
<!-- Template with AJAX -->
<script>
document.getElementById('vote-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    fetch('{% url "polls:ajax_vote" question.id %}', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            location.reload();
        } else {
            alert(data.error);
        }
    });
});
</script>
```

---

## URL Configuration

Add these URLs to use the form views:

```python
# polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # Existing URLs
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    
    # Question CRUD
    path('question/create/', views.create_question, name='create_question'),
    path('question/<int:question_id>/edit/', views.edit_question, name='edit_question'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    
    # Choice management
    path('question/<int:question_id>/add-choice/', views.add_choice_to_question, name='add_choice'),
    path('question/<int:question_id>/manage-choices/', views.manage_choices, name='manage_choices'),
    
    # Voting
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('question/<int:question_id>/ajax-vote/', views.ajax_vote, name='ajax_vote'),
    
    # Other forms
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_questions, name='search'),
    path('feedback/', views.feedback, name='feedback'),
]
```

---

## Summary

### When to Use ModelForms
- ✅ Creating/editing database records
- ✅ Quick form generation from models
- ✅ Automatic validation based on model fields
- ✅ Less code, automatic field types

### When to Use Custom Forms
- ✅ Forms not tied to a model
- ✅ Search forms, contact forms, filters
- ✅ Complex validation logic
- ✅ Multiple models in one form
- ✅ Complete control over fields

### Key Takeaways
1. **ModelForms** save time when working with models
2. **Custom Forms** give complete flexibility
3. Always validate user input (field-level and form-level)
4. Use `cleaned_data` to access validated form data
5. Remember `{% csrf_token %}` in all POST forms
6. Use formsets for multiple related forms
7. Customize widgets for better UX

This guide provides a complete foundation for working with Django forms in the polls application!
