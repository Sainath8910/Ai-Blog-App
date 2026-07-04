from django import forms


class BlogGenerationForm(forms.Form):

    TOPIC_MAX_LENGTH = 300

    LENGTH_CHOICES = [
        ("Short", "Short"),
        ("Medium", "Medium"),
        ("Long", "Long"),
    ]

    TONE_CHOICES = [
        ("Professional", "Professional"),
        ("Friendly", "Friendly"),
        ("Technical", "Technical"),
        ("Conversational", "Conversational"),
    ]

    AUDIENCE_CHOICES = [
        ("Beginners", "Beginners"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    topic = forms.CharField(
        max_length=TOPIC_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "Docker"
            }
        )
    )

    content_brief = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
    "rows": 6,
                "placeholder": "Explain Docker from scratch..."
            }
        )
    )

    target_audience = forms.ChoiceField(
        choices=AUDIENCE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none dark:bg-slate-900 dark:border-slate-700",
                "placeholder": "Beginners"
            }
        ),
    )

    tone = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 bg-white focus:ring-2 focus:ring-blue-500",
                "placeholder": "Professional"
            }
        ),
        choices=TONE_CHOICES
    )

    length = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 bg-white focus:ring-2 focus:ring-blue-500",
                "placeholder": "Medium"
            }
        ),
        choices=LENGTH_CHOICES
    )

    keywords = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-xl border border-slate-300 px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:outline-none",
                "placeholder": "keyword1, keyword2, keyword3"
            }
        ),
        required=False,
        help_text="Comma separated keywords"
    )

class BlogEditForm(forms.Form):

    title = forms.CharField(
        max_length=300
    )

    description = forms.CharField(
        widget=forms.Textarea
    )

    category = forms.CharField(
        max_length=100
    )

    tone = forms.CharField(
        max_length=100
    )

    target_audience = forms.CharField(
        max_length=100
    )

    language = forms.CharField(
        max_length=50
    )

    status = forms.ChoiceField(
        choices=[
            ("draft", "Draft"),
            ("published", "Published"),
            ("archived", "Archived"),
        ]
    )