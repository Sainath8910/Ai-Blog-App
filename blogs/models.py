from django.db import models
import uuid

class Blog(models.Model):
    """
    Main Blog model.

    Stores blog metadata in normal columns.

    Stores rich AI-generated content as JSON.
    """

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    PROCESSING_STATUS = [
        ("queued", "Queued"),
        ("generating", "Generating"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    id = models.BigAutoField(primary_key=True)

    # --------------------------------------------------
    # Owner
    # --------------------------------------------------

    user_id = models.UUIDField(
        db_index=True
    )
    generation_uuid = models.UUIDField(
    default=uuid.uuid4,
    unique=True,
    editable=False,
    db_index=True,
    )
    # --------------------------------------------------
    # Blog Information
    # --------------------------------------------------

    topic = models.CharField(
        max_length=300
    )

    language = models.CharField(
        max_length=50,
        default="English"
    )

    tone = models.CharField(
        max_length=100,
        default="Professional"
    )

    blog_type = models.CharField(
        max_length=100,
        default="Educational"
    )

    target_audience = models.CharField(
        max_length=100,
        default="General"
    )

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    title = models.CharField(
        max_length=300
    )

    slug = models.SlugField(
        unique=True,
        max_length=350
    )

    description = models.TextField()

    category = models.CharField(
        max_length=100
    )

    keywords = models.JSONField(
        default=list,
        blank=True
    )

    tags = models.JSONField(
        default=list,
        blank=True
    )

    # --------------------------------------------------
    # Rich Sections
    # --------------------------------------------------

    hero = models.JSONField()

    key_takeaways = models.JSONField(
        default=list,
        blank=True
    )

    faq = models.JSONField(
        default=list,
        blank=True
    )

    resources = models.JSONField(
        null=True,
        blank=True
    )

    call_to_action = models.JSONField(
        null=True,
        blank=True
    )

    conclusion = models.JSONField()

    # --------------------------------------------------
    # Generation
    # --------------------------------------------------

    processing_status = models.CharField(
        max_length=20,
        choices=PROCESSING_STATUS,
        default="queued",
        db_index=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
        db_index=True
    )

    generation_version = models.PositiveIntegerField(
        default=1
    )

    llm_provider = models.CharField(
        max_length=50,
        default="gemini"
    )

    image_provider = models.CharField(
        max_length=50,
        default="pollinations"
    )

    generation_time = models.FloatField(
        default=0
    )

    error_message = models.TextField(
        blank=True
    )

    # --------------------------------------------------
    # Soft Delete
    # --------------------------------------------------

    is_deleted = models.BooleanField(
        default=False
    )

    # --------------------------------------------------
    # Timestamps
    # --------------------------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "-created_at"
        ]

        indexes = [

            models.Index(
                fields=["user_id"]
            ),

            models.Index(
                fields=["user_id", "status"]
            ),

            models.Index(
                fields=["slug"]
            ),

            models.Index(
                fields=["category"]
            ),

            models.Index(
                fields=["processing_status"]
            ),
        ]

    def __str__(self):
        return self.title


class BlogChapter(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="chapters",
    )

    order = models.PositiveIntegerField()

    purpose = models.CharField(max_length=50)

    title = models.CharField(max_length=255)

    paragraphs = models.JSONField(default=list)

    bullet_points = models.JSONField(default=list)

    numbered_steps = models.JSONField(default=list)

    tips = models.JSONField(default=list)

    warnings = models.JSONField(default=list)

    notes = models.JSONField(default=list)

    examples = models.JSONField(default=list)

    quotes = models.JSONField(default=list)

    code_examples = models.JSONField(default=list)

    tables = models.JSONField(default=list)

    image = models.JSONField(default=dict)

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["blog", "order"],
                name="unique_blog_chapter_order",
            )
        ]

    def __str__(self):
        return f"{self.order}. {self.title}"