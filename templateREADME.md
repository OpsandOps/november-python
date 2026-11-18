# Django Templates Guide for Polls App

This comprehensive guide demonstrates Django template operations using our polls application. You'll learn template syntax, filters, tags, template inheritance, and best practices.

---

## Table of Contents

1. [Template Basics](#template-basics)
2. [Template Variables](#template-variables)
3. [Template Filters](#template-filters)
4. [Template Tags](#template-tags)
5. [Template Inheritance](#template-inheritance)
6. [URL Handling](#url-handling)
7. [Static Files](#static-files)
8. [Complete Examples](#complete-examples)

---

## Template Basics

### What are Django Templates?

Django templates are text files (usually HTML) that contain:
- **Static content**: HTML markup, CSS, JavaScript
- **Dynamic content**: Variables and tags processed by Django's template engine

### Template Syntax Overview

```django
{# This is a comment - it won't appear in the output #}

{{ variable }}              {# Outputs a variable #}
{{ variable|filter }}       {# Applies a filter to a variable #}
{% tag %}                   {# Template tags for logic #}
{% tag %} ... {% endtag %}  {# Block tags #}
```

---

## Template Variables

### Basic Variable Output

```django
{# In your view: context = {"question_text": "What's your favorite color?"} #}

<h1>{{ question_text }}</h1>
{# Output: <h1>What's your favorite color?</h1> #}
```

### Accessing Object Attributes

```django
{# Question object with attributes #}
<h2>{{ question.question_text }}</h2>
<p>Published: {{ question.pub_date }}</p>
<p>Author: {{ question.author.username }}</p>
```

### Accessing Dictionary Keys

```django
{# context = {"data": {"name": "John", "age": 30}} #}
<p>Name: {{ data.name }}</p>
<p>Age: {{ data.age }}</p>
```

### Accessing List Items

```django
{# context = {"colors": ["red", "blue", "green"]} #}
<p>First color: {{ colors.0 }}</p>
<p>Second color: {{ colors.1 }}</p>
```

### Method Calls

```django
{# Calling methods (no parentheses!) #}
<p>{{ question.recently_published }}</p>
<p>{{ question.validate_question }}</p>
<p>{{ question.author_fullname }}</p>
```

---

## Template Filters

Filters modify variables for display. Syntax: `{{ variable|filter:argument }}`

### String Filters

```django
{# lower - Convert to lowercase #}
{{ question.question_text|lower }}

{# upper - Convert to uppercase #}
{{ question.question_text|upper }}

{# title - Title Case #}
{{ question.question_text|title }}

{# capfirst - Capitalize first character #}
{{ question.question_text|capfirst }}

{# truncatewords - Limit word count #}
{{ question.question_text|truncatewords:5 }}
{# Output: "What's your favorite color..." (first 5 words) #}

{# truncatechars - Limit character count #}
{{ question.question_text|truncatechars:20 }}
{# Output: "What's your favori..." #}

{# length - Get length #}
{{ question.question_text|length }}

{# default - Default value if variable is False/None/empty #}
{{ question.question_text|default:"No question text available" }}

{# default_if_none - Default only if None #}
{{ question.author|default_if_none:"Anonymous" }}

{# linebreaks - Convert newlines to <p> and <br> tags #}
{{ question.question_text|linebreaks }}

{# linebreaksbr - Convert newlines to <br> tags #}
{{ question.question_text|linebreaksbr }}

{# safe - Mark string as safe (don't escape HTML) #}
{{ html_content|safe }}

{# escape - Force HTML escaping #}
{{ user_input|escape }}

{# striptags - Remove HTML tags #}
{{ html_content|striptags }}

{# slugify - Convert to URL-friendly slug #}
{{ question.question_text|slugify }}
{# Output: "whats-your-favorite-color" #}
```

### Number Filters

```django
{# add - Add a value #}
{{ choice.votes|add:10 }}

{# floatformat - Format decimal places #}
{{ value|floatformat:2 }}  {# 2 decimal places #}

{# divisibleby - Check if divisible by argument #}
{% if choice.votes|divisibleby:2 %}
    <p>Even number of votes</p>
{% endif %}
```

### Date Filters

```django
{# date - Format date #}
{{ question.pub_date|date:"Y-m-d" }}
{# Output: "2024-10-22" #}

{{ question.pub_date|date:"F j, Y" }}
{# Output: "October 22, 2024" #}

{{ question.pub_date|date:"D, M j, Y g:i A" }}
{# Output: "Thu, Oct 22, 2024 3:45 PM" #}

{# time - Format time #}
{{ question.pub_date|time:"H:i" }}
{# Output: "15:45" #}

{# timesince - Time since date #}
{{ question.pub_date|timesince }}
{# Output: "2 days, 3 hours" #}

{# timeuntil - Time until date #}
{{ future_date|timeuntil }}
```

### List Filters

```django
{# join - Join list items #}
{{ colors|join:", " }}
{# Output: "red, blue, green" #}

{# first - First item #}
{{ questions|first }}

{# last - Last item #}
{{ questions|last }}

{# slice - Slice list #}
{{ questions|slice:":3" }}  {# First 3 items #}

{# random - Random item #}
{{ questions|random }}

{# length - List length #}
{{ questions|length }}
```

### Chaining Filters

```django
{# Apply multiple filters #}
{{ question.question_text|lower|truncatewords:5|title }}

{{ question.pub_date|date:"F j, Y"|upper }}
```

---

## Template Tags

Tags provide logic and control flow in templates.

### if/elif/else

```django
{% if questions %}
    <h2>Available Questions</h2>
{% else %}
    <p>No questions available.</p>
{% endif %}

{# Multiple conditions #}
{% if question.votes > 100 %}
    <span class="popular">Popular!</span>
{% elif question.votes > 50 %}
    <span class="trending">Trending</span>
{% else %}
    <span class="new">New</span>
{% endif %}

{# Logical operators: and, or, not #}
{% if question.author and question.pub_date %}
    <p>By {{ question.author }} on {{ question.pub_date|date:"F j, Y" }}</p>
{% endif %}

{% if not question.is_published %}
    <span class="draft">Draft</span>
{% endif %}

{# Comparison operators: ==, !=, <, >, <=, >=, in #}
{% if question.votes >= 100 %}
    <span class="milestone">100+ votes!</span>
{% endif %}

{% if "keyword" in question.question_text %}
    <span class="tagged">Tagged</span>
{% endif %}
```

### for Loop

```django
{# Basic loop #}
<ul>
{% for question in questions %}
    <li>{{ question.question_text }}</li>
{% endfor %}
</ul>

{# Loop with empty #}
<ul>
{% for question in questions %}
    <li>{{ question.question_text }}</li>
{% empty %}
    <li>No questions available.</li>
{% endfor %}
</ul>

{# Loop counter variables #}
{% for question in questions %}
    <p>
        {{ forloop.counter }}. {# 1-indexed counter #}
        {{ question.question_text }}
        
        {# Other forloop variables: #}
        {# forloop.counter0 - 0-indexed counter #}
        {# forloop.revcounter - Reverse counter #}
        {# forloop.first - True on first iteration #}
        {# forloop.last - True on last iteration #}
    </p>
    
    {% if forloop.first %}
        <hr> {# Line after first item #}
    {% endif %}
    
    {% if not forloop.last %}
        <hr> {# Line between items #}
    {% endif %}
{% endfor %}

{# Nested loops #}
{% for question in questions %}
    <h3>{{ question.question_text }}</h3>
    <ul>
    {% for choice in question.choice_set.all %}
        <li>
            {{ forloop.parentloop.counter }}.{{ forloop.counter }}
            {{ choice.choice_text }} ({{ choice.votes }} votes)
        </li>
    {% endfor %}
    </ul>
{% endfor %}
```

### with Tag

```django
{# Store value in variable #}
{% with total_votes=choice.votes|add:100 %}
    <p>Total votes: {{ total_votes }}</p>
{% endwith %}

{# Multiple variables #}
{% with author_name=question.author.username pub_year=question.pub_date|date:"Y" %}
    <p>{{ author_name }} ({{ pub_year }})</p>
{% endwith %}
```

### url Tag

```django
{# Generate URLs from URL patterns #}
<a href="{% url 'polls:index' %}">Home</a>
<a href="{% url 'polls:detail' question.id %}">Details</a>
<a href="{% url 'polls:results' question.id %}">Results</a>
<a href="{% url 'polls:vote' question.id %}">Vote</a>

{# With query parameters #}
<a href="{% url 'polls:index' %}?page=2">Page 2</a>
```

### csrf_token

```django
{# Required for POST forms #}
<form method="post" action="{% url 'polls:vote' question.id %}">
    {% csrf_token %}
    <input type="text" name="choice">
    <button type="submit">Vote</button>
</form>
```

### now Tag

```django
{# Current date/time #}
<p>Generated on: {% now "F j, Y H:i" %}</p>
<p>Year: {% now "Y" %}</p>
```

### cycle Tag

```django
{# Cycle through values #}
{% for question in questions %}
    <tr class="{% cycle 'row1' 'row2' %}">
        <td>{{ question.question_text }}</td>
    </tr>
{% endfor %}
```

### spaceless Tag

```django
{# Remove whitespace between HTML tags #}
{% spaceless %}
    <p>
        <a href="/">Home</a>
    </p>
{% endspaceless %}
{# Output: <p><a href="/">Home</a></p> #}
```

### verbatim Tag

```django
{# Don't process Django template syntax #}
{% verbatim %}
    <script>
        var data = {{ jsonData }};  // This won't be processed by Django
    </script>
{% endverbatim %}
```

---

## Template Inheritance

Template inheritance is Django's most powerful feature for reducing code duplication.

### Creating base.html

**Location**: `polls/templates/polls/base.html`

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    {# Block for page-specific title #}
    <title>{% block title %}Polls App{% endblock %}</title>
    
    {# Block for extra head content (CSS, meta tags, etc.) #}
    {% block extra_head %}{% endblock %}
    
    <style>
        /* Base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            margin-bottom: 2rem;
        }
        
        header h1 {
            text-align: center;
        }
        
        nav {
            background-color: #34495e;
            padding: 1rem;
            margin-bottom: 2rem;
        }
        
        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        
        nav a:hover {
            background-color: #2c3e50;
        }
        
        .content {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            min-height: 400px;
        }
        
        footer {
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
            color: #666;
        }
        
        {% block extra_styles %}{% endblock %}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>{% block header_title %}Django Polls Application{% endblock %}</h1>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                {% block navigation %}
                <li><a href="{% url 'polls:index' %}">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
                {% endblock %}
            </ul>
        </div>
    </nav>
    
    <div class="container">
        {# Messages/Alerts block #}
        {% block messages %}
        {% endblock %}
        
        {# Breadcrumbs block #}
        {% block breadcrumbs %}{% endblock %}
        
        {# Main content block #}
        <div class="content">
            {% block content %}
            <p>This is the default content. Override this block in child templates.</p>
            {% endblock %}
        </div>
        
        {# Sidebar block (optional) #}
        {% block sidebar %}{% endblock %}
    </div>
    
    <footer>
        <div class="container">
            {% block footer %}
            <p>&copy; {% now "Y" %} Polls App. All rights reserved.</p>
            {% endblock %}
        </div>
    </footer>
    
    {# Block for extra scripts #}
    {% block extra_scripts %}{% endblock %}
</body>
</html>
```

### Using base.html in Child Templates

#### Example 1: polls/index.html

```django
{% extends "polls/base.html" %}

{% block title %}Latest Polls - Polls App{% endblock %}

{% block header_title %}Latest Polls{% endblock %}

{% block breadcrumbs %}
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item active">Home</li>
    </ol>
</nav>
{% endblock %}

{% block content %}
<h2>Available Questions</h2>

{% if questions %}
    <div class="question-list">
        {% for question in questions %}
            <div class="question-item">
                <h3>
                    {{ forloop.counter }}. 
                    <a href="{% url 'polls:detail' question.id %}">
                        {{ question.question_text }}
                    </a>
                </h3>
                
                <div class="meta">
                    <span class="author">By {{ question.author.username }}</span>
                    <span class="date">{{ question.pub_date|date:"F j, Y" }}</span>
                    <span class="time-ago">{{ question.pub_date|timesince }} ago</span>
                </div>
                
                {% if not forloop.last %}
                    <hr>
                {% endif %}
            </div>
        {% endfor %}
    </div>
{% else %}
    <div class="alert alert-info">
        <p>No polls are available at this time.</p>
        <p>Check back later for new questions!</p>
    </div>
{% endif %}
{% endblock %}

{% block extra_styles %}
<style>
    .question-list {
        margin: 20px 0;
    }
    
    .question-item {
        margin-bottom: 20px;
    }
    
    .question-item h3 {
        color: #2c3e50;
        margin-bottom: 10px;
    }
    
    .question-item a {
        color: #3498db;
        text-decoration: none;
    }
    
    .question-item a:hover {
        text-decoration: underline;
    }
    
    .meta {
        color: #666;
        font-size: 0.9rem;
    }
    
    .meta span {
        margin-right: 15px;
    }
    
    .alert {
        padding: 15px;
        border-radius: 4px;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
</style>
{% endblock %}
```

#### Example 2: polls/detail.html

```django
{% extends "polls/base.html" %}

{% block title %}{{ question.question_text }} - Polls App{% endblock %}

{% block breadcrumbs %}
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li><a href="{% url 'polls:index' %}">Home</a></li>
        <li class="active">Question Details</li>
    </ol>
</nav>
{% endblock %}

{% block content %}
<article class="question-detail">
    <header>
        <h2>{{ question.question_text }}</h2>
        <div class="question-meta">
            <p>
                <strong>Author:</strong> {{ question.author.username|title }}
                <span class="separator">|</span>
                <strong>Published:</strong> {{ question.pub_date|date:"F j, Y \a\t g:i A" }}
                <span class="separator">|</span>
                <strong>Time:</strong> {{ question.pub_date|timesince }} ago
            </p>
        </div>
    </header>
    
    <section class="voting-section">
        <h3>Cast Your Vote</h3>
        
        {% if error_message %}
            <div class="error">{{ error_message }}</div>
        {% endif %}
        
        <form method="post" action="{% url 'polls:vote' question.id %}">
            {% csrf_token %}
            
            {% for choice in question.choice_set.all %}
                <div class="choice-item">
                    <input 
                        type="radio" 
                        name="choice" 
                        id="choice{{ forloop.counter }}" 
                        value="{{ choice.id }}"
                    >
                    <label for="choice{{ forloop.counter }}">
                        {{ choice.choice_text }}
                        <span class="vote-count">({{ choice.votes }} vote{{ choice.votes|pluralize }})</span>
                    </label>
                </div>
            {% empty %}
                <p class="no-choices">No choices available for this question.</p>
            {% endfor %}
            
            <button type="submit" class="btn-submit">Submit Vote</button>
        </form>
    </section>
    
    <aside class="question-stats">
        <h4>Question Statistics</h4>
        {% with total_votes=question.choice_set.all|length %}
            <p>Total Choices: {{ total_votes }}</p>
        {% endwith %}
    </aside>
    
    <nav class="question-navigation">
        <a href="{% url 'polls:results' question.id %}" class="btn">View Results</a>
        <a href="{% url 'polls:index' %}" class="btn btn-secondary">Back to List</a>
    </nav>
</article>
{% endblock %}

{% block extra_styles %}
<style>
    .question-detail {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .question-meta {
        color: #666;
        margin: 10px 0 30px 0;
        padding: 15px;
        background-color: #f8f9fa;
        border-radius: 4px;
    }
    
    .separator {
        margin: 0 10px;
    }
    
    .voting-section {
        margin: 30px 0;
    }
    
    .choice-item {
        padding: 12px;
        margin: 10px 0;
        background-color: #f8f9fa;
        border-radius: 4px;
        border: 2px solid transparent;
        transition: all 0.3s;
    }
    
    .choice-item:hover {
        border-color: #3498db;
        background-color: #e3f2fd;
    }
    
    .choice-item input[type="radio"] {
        margin-right: 10px;
    }
    
    .vote-count {
        color: #666;
        font-size: 0.9rem;
    }
    
    .btn-submit {
        margin-top: 20px;
        padding: 12px 30px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1rem;
    }
    
    .btn-submit:hover {
        background-color: #2980b9;
    }
    
    .error {
        background-color: #f8d7da;
        color: #721c24;
        padding: 12px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    
    .question-navigation {
        margin-top: 30px;
        display: flex;
        gap: 10px;
    }
    
    .btn {
        padding: 10px 20px;
        background-color: #3498db;
        color: white;
        text-decoration: none;
        border-radius: 4px;
        display: inline-block;
    }
    
    .btn-secondary {
        background-color: #95a5a6;
    }
</style>
{% endblock %}
```

#### Example 3: polls/results.html

```django
{% extends "polls/base.html" %}

{% block title %}Results: {{ question.question_text }} - Polls App{% endblock %}

{% block breadcrumbs %}
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li><a href="{% url 'polls:index' %}">Home</a></li>
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text|truncatewords:3 }}</a></li>
        <li class="active">Results</li>
    </ol>
</nav>
{% endblock %}

{% block content %}
<div class="results-container">
    <h2>{{ question.question_text }}</h2>
    
    {% with total_votes=question.choice_set.all.0.votes|add:question.choice_set.all.1.votes %}
        <p class="total-votes">Total votes: {{ total_votes }}</p>
    {% endwith %}
    
    <div class="results-list">
        {% for choice in question.choice_set.all %}
            {% with percentage=choice.votes|floatformat:0 %}
                <div class="result-item">
                    <div class="choice-header">
                        <span class="choice-text">{{ choice.choice_text }}</span>
                        <span class="vote-count">{{ choice.votes }} vote{{ choice.votes|pluralize }}</span>
                    </div>
                    
                    <div class="progress-bar">
                        <div 
                            class="progress-fill {% cycle 'color-1' 'color-2' 'color-3' %}" 
                            style="width: {% widthratio choice.votes 100 100 %}%"
                        >
                            {% widthratio choice.votes 100 100 %}%
                        </div>
                    </div>
                    
                    {% if forloop.first %}
                        <span class="winner-badge">🏆 Leading</span>
                    {% endif %}
                </div>
            {% endwith %}
        {% empty %}
            <p>No votes yet.</p>
        {% endfor %}
    </div>
    
    <div class="actions">
        <a href="{% url 'polls:detail' question.id %}" class="btn">Vote Again</a>
        <a href="{% url 'polls:index' %}" class="btn btn-secondary">Back to Polls</a>
    </div>
</div>
{% endblock %}

{% block extra_styles %}
<style>
    .results-container {
        max-width: 700px;
        margin: 0 auto;
    }
    
    .total-votes {
        color: #666;
        margin: 10px 0 30px 0;
        font-size: 1.1rem;
    }
    
    .result-item {
        margin-bottom: 25px;
        padding: 15px;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    
    .choice-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    
    .choice-text {
        font-weight: bold;
        color: #2c3e50;
    }
    
    .vote-count {
        color: #666;
    }
    
    .progress-bar {
        background-color: #ecf0f1;
        height: 30px;
        border-radius: 15px;
        overflow: hidden;
        position: relative;
    }
    
    .progress-fill {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        transition: width 0.5s ease;
    }
    
    .color-1 { background-color: #3498db; }
    .color-2 { background-color: #e74c3c; }
    .color-3 { background-color: #2ecc71; }
    
    .winner-badge {
        display: inline-block;
        margin-top: 10px;
        padding: 5px 10px;
        background-color: #f39c12;
        color: white;
        border-radius: 4px;
        font-size: 0.9rem;
    }
    
    .actions {
        margin-top: 30px;
        display: flex;
        gap: 10px;
    }
</style>
{% endblock %}
```

---

## URL Handling

### Basic URL Tag Usage

```django
{# Named URL patterns #}
<a href="{% url 'polls:index' %}">Home</a>

{# URLs with arguments #}
<a href="{% url 'polls:detail' question.id %}">View Question</a>

{# URLs with multiple arguments #}
<a href="{% url 'app_name:view_name' arg1 arg2 %}">Link</a>

{# URLs with keyword arguments #}
<a href="{% url 'app_name:view_name' pk=question.id %}">Link</a>
```

### Dynamic URL Generation

```django
{% for question in questions %}
    <a href="{% url 'polls:detail' question.id %}">
        {{ question.question_text }}
    </a>
{% endfor %}
```

### URL with Query Parameters

```django
{# Manual query string #}
<a href="{% url 'polls:index' %}?page=2&sort=votes">Page 2</a>

{# Using request context #}
<a href="{% url 'polls:index' %}?next={{ request.path }}">Login</a>
```

---

## Static Files

### Loading Static Files

```django
{% load static %}

<!DOCTYPE html>
<html>
<head>
    {# CSS files #}
    <link rel="stylesheet" href="{% static 'polls/css/style.css' %}">
    
    {# With path joining #}
    <link rel="stylesheet" href="{% static 'polls/css/'|add:'style.css' %}">
</head>
<body>
    {# Images #}
    <img src="{% static 'polls/images/logo.png' %}" alt="Logo">
    
    {# JavaScript #}
    <script src="{% static 'polls/js/script.js' %}"></script>
    
    {# Dynamic static files #}
    {% with icon='icon.png' %}
        <img src="{% static 'polls/images/'|add:icon %}" alt="Icon">
    {% endwith %}
</body>
</html>
```

---

## Complete Examples

### Example 1: Full Featured Question List

**polls/templates/polls/question_list.html**

```django
{% extends "polls/base.html" %}
{% load static %}

{% block title %}All Questions - Polls App{% endblock %}

{% block extra_head %}
<link rel="stylesheet" href="{% static 'polls/css/questions.css' %}">
{% endblock %}

{% block content %}
<div class="questions-page">
    <header class="page-header">
        <h2>All Questions</h2>
        <p class="subtitle">Browse and vote on all available polls</p>
    </header>
    
    {# Search/Filter Section #}
    <div class="filters">
        <form method="get" action="{% url 'polls:index' %}">
            <input type="text" name="search" placeholder="Search questions..." value="{{ request.GET.search }}">
            <button type="submit">Search</button>
        </form>
    </div>
    
    {# Statistics Section #}
    <div class="stats-grid">
        <div class="stat-card">
            <h3>{{ questions|length }}</h3>
            <p>Total Question{{ questions|length|pluralize }}</p>
        </div>
        <div class="stat-card">
            <h3>{% now "Y" %}</h3>
            <p>Current Year</p>
        </div>
    </div>
    
    {# Questions Grid #}
    {% if questions %}
        <div class="questions-grid">
            {% for question in questions %}
                <article class="question-card {% cycle 'card-blue' 'card-green' 'card-orange' %}">
                    <div class="card-header">
                        <span class="question-number">#{{ forloop.counter }}</span>
                        <span class="date">{{ question.pub_date|date:"M d" }}</span>
                    </div>
                    
                    <div class="card-body">
                        <h3>
                            <a href="{% url 'polls:detail' question.id %}">
                                {{ question.question_text|truncatechars:60 }}
                            </a>
                        </h3>
                        
                        <p class="author">
                            By {{ question.author.username|title }}
                            <span class="time-ago">• {{ question.pub_date|timesince }} ago</span>
                        </p>
                        
                        {# Choice count #}
                        {% with choice_count=question.choice_set.count %}
                            <p class="choices">
                                {{ choice_count }} choice{{ choice_count|pluralize }}
                            </p>
                        {% endwith %}
                    </div>
                    
                    <div class="card-footer">
                        <a href="{% url 'polls:detail' question.id %}" class="btn-vote">Vote Now</a>
                        <a href="{% url 'polls:results' question.id %}" class="btn-results">Results</a>
                    </div>
                    
                    {# First/Last indicators #}
                    {% if forloop.first %}
                        <div class="ribbon">Latest</div>
                    {% endif %}
                </article>
                
                {# Ad placeholder every 3 items #}
                {% if forloop.counter|divisibleby:3 and not forloop.last %}
                    <div class="ad-placeholder">
                        <p>Advertisement Space</p>
                    </div>
                {% endif %}
            {% endfor %}
        </div>
        
        {# Pagination placeholder #}
        <div class="pagination">
            <a href="?page=1">Previous</a>
            <span class="current-page">Page 1</span>
            <a href="?page=2">Next</a>
        </div>
    {% else %}
        <div class="empty-state">
            <h3>No Questions Found</h3>
            <p>Be the first to create a question!</p>
        </div>
    {% endif %}
</div>
{% endblock %}

{% block sidebar %}
<aside class="sidebar">
    <div class="widget">
        <h4>Recent Activity</h4>
        <p>Last updated: {% now "F j, Y g:i A" %}</p>
    </div>
</aside>
{% endblock %}

{% block extra_scripts %}
<script>
    console.log('Questions page loaded');
    // Add your JavaScript here
</script>
{% endblock %}
```

### Example 2: Advanced Form with Validation

**polls/templates/polls/vote_form.html**

```django
{% extends "polls/base.html" %}

{% block title %}Vote on {{ question.question_text|striptags }} - Polls App{% endblock %}

{% block content %}
<div class="vote-form-container">
    <h2>{{ question.question_text }}</h2>
    
    {# Error messages #}
    {% if error_message %}
        <div class="alert alert-danger">
            <strong>Error!</strong> {{ error_message }}
        </div>
    {% endif %}
    
    {# Success messages #}
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
    
    <form method="post" action="{% url 'polls:vote' question.id %}" class="vote-form">
        {% csrf_token %}
        
        <fieldset>
            <legend>Select Your Choice</legend>
            
            {% for choice in question.choice_set.all %}
                <div class="radio-group">
                    <input 
                        type="radio" 
                        name="choice" 
                        id="choice-{{ choice.id }}"
                        value="{{ choice.id }}"
                        {% if forloop.first %}checked{% endif %}
                        required
                    >
                    <label for="choice-{{ choice.id }}">
                        <span class="choice-number">{{ forloop.counter }}.</span>
                        <span class="choice-text">{{ choice.choice_text }}</span>
                        <span class="current-votes">
                            {{ choice.votes }} vote{{ choice.votes|pluralize }}
                        </span>
                        
                        {# Visual vote indicator #}
                        {% if choice.votes > 0 %}
                            <span class="vote-bar" style="width: {% widthratio choice.votes 50 100 %}%"></span>
                        {% endif %}
                    </label>
                </div>
            {% empty %}
                <p class="no-choices">No choices available for this question.</p>
            {% endfor %}
        </fieldset>
        
        <div class="form-actions">
            <button type="submit" class="btn btn-primary">
                Submit Vote
            </button>
            <a href="{% url 'polls:results' question.id %}" class="btn btn-secondary">
                View Current Results
            </a>
            <a href="{% url 'polls:index' %}" class="btn btn-link">
                Back to Questions
            </a>
        </div>
    </form>
    
    {# Question metadata #}
    <div class="question-info">
        <h4>Question Information</h4>
        <dl>
            <dt>Author:</dt>
            <dd>{{ question.author.username|title }}</dd>
            
            <dt>Published:</dt>
            <dd>{{ question.pub_date|date:"l, F j, Y \a\t g:i A" }}</dd>
            
            <dt>Time Since:</dt>
            <dd>{{ question.pub_date|timesince }} ago</dd>
            
            <dt>Total Choices:</dt>
            <dd>{{ question.choice_set.count }}</dd>
        </dl>
    </div>
</div>
{% endblock %}

{% block extra_styles %}
<style>
    .vote-form-container {
        max-width: 700px;
        margin: 0 auto;
    }
    
    .alert {
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }
    
    .alert-danger {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    
    .radio-group {
        position: relative;
        margin: 15px 0;
        padding: 15px;
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        transition: all 0.3s;
    }
    
    .radio-group:hover {
        border-color: #3498db;
        background-color: #f8f9fa;
    }
    
    .radio-group input[type="radio"]:checked + label {
        font-weight: bold;
        color: #3498db;
    }
    
    .vote-bar {
        position: absolute;
        bottom: 0;
        left: 0;
        height: 4px;
        background-color: #3498db;
        transition: width 0.3s;
    }
    
    .form-actions {
        margin-top: 30px;
        display: flex;
        gap: 10px;
    }
    
    .btn {
        padding: 12px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    
    .btn-primary {
        background-color: #3498db;
        color: white;
    }
    
    .btn-primary:hover {
        background-color: #2980b9;
    }
    
    .question-info {
        margin-top: 40px;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    
    .question-info dl {
        display: grid;
        grid-template-columns: 150px 1fr;
        gap: 10px;
    }
    
    .question-info dt {
        font-weight: bold;
        color: #666;
    }
</style>
{% endblock %}
```

---

## Best Practices

### 1. Always Use Template Inheritance

```django
{# Good ✓ #}
{% extends "polls/base.html" %}

{# Avoid creating standalone HTML files for every page #}
```

### 2. Use Named URL Patterns

```django
{# Good ✓ #}
<a href="{% url 'polls:detail' question.id %}">Details</a>

{# Bad ✗ - Hard-coded URLs #}
<a href="/polls/1/">Details</a>
```

### 3. Use Filters for Display Logic

```django
{# Good ✓ #}
{{ question.question_text|lower|title }}

{# Avoid processing in views when possible #}
```

### 4. Handle Empty States

```django
{# Good ✓ #}
{% for question in questions %}
    {{ question.question_text }}
{% empty %}
    <p>No questions available.</p>
{% endfor %}
```

### 5. Escape User Input (Django does this by default)

```django
{# Safe - Django auto-escapes #}
{{ user_comment }}

{# Only use |safe when you control the content #}
{{ admin_html_content|safe }}
```

### 6. Use Verbatim for JavaScript Templates

```django
{% verbatim %}
<script>
    var template = '{{ variable }}';  // Won't be processed by Django
</script>
{% endverbatim %}
```

### 7. Keep Templates Clean

```django
{# Good ✓ - Simple logic in template #}
{% if user.is_authenticated %}
    Welcome, {{ user.username }}
{% endif %}

{# Bad ✗ - Complex logic should be in views #}
{# Avoid complex calculations or database queries in templates #}
```

---

## Common Patterns

### Pattern 1: List-Detail Navigation

```django
{# List page #}
{% for item in items %}
    <a href="{% url 'app:detail' item.id %}">{{ item.name }}</a>
{% endfor %}

{# Detail page - back link #}
<a href="{% url 'app:list' %}">← Back to list</a>
```

### Pattern 2: Active Navigation

```django
<nav>
    <a href="{% url 'polls:index' %}" 
       class="{% if request.resolver_match.url_name == 'index' %}active{% endif %}">
        Home
    </a>
</nav>
```

### Pattern 3: Conditional Rendering

```django
{% if user.is_authenticated %}
    {% if user.is_staff %}
        <a href="{% url 'admin:index' %}">Admin Panel</a>
    {% else %}
        <a href="{% url 'polls:index' %}">Polls</a>
    {% endif %}
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

### Pattern 4: Data Tables

```django
<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Question</th>
            <th>Author</th>
            <th>Date</th>
        </tr>
    </thead>
    <tbody>
        {% for question in questions %}
        <tr class="{% cycle 'odd' 'even' %}">
            <td>{{ forloop.counter }}</td>
            <td>{{ question.question_text }}</td>
            <td>{{ question.author.username }}</td>
            <td>{{ question.pub_date|date:"Y-m-d" }}</td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="4">No data available</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

---

## Quick Reference

### Template Syntax Cheat Sheet

| Syntax | Purpose | Example |
|--------|---------|---------|
| `{{ variable }}` | Output variable | `{{ question.text }}` |
| `{{ var\|filter }}` | Apply filter | `{{ name\|upper }}` |
| `{% tag %}` | Template tag | `{% if condition %}` |
| `{# comment #}` | Comment | `{# TODO: fix this #}` |
| `{% extends %}` | Inherit template | `{% extends "base.html" %}` |
| `{% block %}` | Define block | `{% block content %}` |
| `{% include %}` | Include template | `{% include "nav.html" %}` |
| `{% url %}` | Generate URL | `{% url 'polls:index' %}` |
| `{% csrf_token %}` | CSRF protection | In POST forms |
| `{% load %}` | Load template tags | `{% load static %}` |

---

## Conclusion

This guide covered:
- ✅ Template variables and attribute access
- ✅ Template filters (string, number, date, list)
- ✅ Template tags (if, for, with, url, etc.)
- ✅ Template inheritance with base.html
- ✅ URL handling and generation
- ✅ Static files management
- ✅ Complete real-world examples
- ✅ Best practices and patterns

Practice these concepts in your polls app, and you'll master Django templates!

---

**Next Steps:**
1. Create the base.html template
2. Convert existing templates to use inheritance
3. Add styling and JavaScript
4. Implement the detail and results views
5. Test all template operations

Happy templating! 🎉
