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

    INPUT_CLASS = """
    w-full
    rounded-2xl

    border
    border-slate-300
    dark:border-slate-700

    bg-white
    dark:bg-slate-900

    text-slate-900
    dark:text-white

    placeholder:text-slate-400
    dark:placeholder:text-slate-500

    px-5
    py-4

    transition-all
    duration-200

    focus:outline-none
    focus:ring-4
    focus:ring-blue-500/20
    focus:border-blue-500
    """

    SELECT_CLASS = """
    w-full
    rounded-2xl

    border
    border-slate-300
    dark:border-slate-700

    bg-white
    dark:bg-slate-900

    text-slate-900
    dark:text-white

    px-5
    py-4

    transition-all
    duration-200

    focus:outline-none
    focus:ring-4
    focus:ring-blue-500/20
    focus:border-blue-500
    """

    TEXTAREA_CLASS = """
    w-full
    rounded-2xl

    border
    border-slate-300
    dark:border-slate-700

    bg-white
    dark:bg-slate-900

    text-slate-900
    dark:text-white

    placeholder:text-slate-400
    dark:placeholder:text-slate-500

    px-5
    py-4

    min-h-[180px]

    resize-y

    transition-all
    duration-200

    focus:outline-none
    focus:ring-4
    focus:ring-blue-500/20
    focus:border-blue-500
    """

    topic = forms.CharField(
        max_length=TOPIC_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={
                "class": INPUT_CLASS,
                "placeholder": "e.g. Future of Artificial Intelligence in Healthcare",
                "autocomplete": "off",
            }
        ),
    )

    content_brief = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": TEXTAREA_CLASS,
                "rows": 8,
                "placeholder": "Describe what you want the AI to write. Include important points, goals, audience and anything you want covered...",
            }
        )
    )

    target_audience = forms.ChoiceField(
        choices=AUDIENCE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": SELECT_CLASS,
            }
        ),
    )

    tone = forms.ChoiceField(
        choices=TONE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": SELECT_CLASS,
            }
        ),
    )

    length = forms.ChoiceField(
        choices=LENGTH_CHOICES,
        widget=forms.Select(
            attrs={
                "class": SELECT_CLASS,
            }
        ),
    )

    keywords = forms.CharField(
        required=False,
        help_text="Separate keywords with commas.",
        widget=forms.TextInput(
            attrs={
                "class": INPUT_CLASS,
                "placeholder": "AI, SEO, Django, Python, Machine Learning",
                "autocomplete": "off",
            }
        ),
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