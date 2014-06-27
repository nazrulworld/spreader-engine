from django.db import models
from django.conf import settings


class PostCategoryModel(models.Model):
    """
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField(serialize=False, null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        db_constraint=False,
        db_column='parent_id',
        null=True,
        blank=False
    )
    seo_attributes = models.TextField(serialize=False, blank=True, null=True)
    thumbnail = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(null=False, default=True)

    class Meta:
        app_label = "blog"
        db_table = "%s_post_categories" % app_label
        verbose_name = "post category"
        verbose_name_plural = 'post categories'

    def __unicode__(self):
        return self.name


class PostModel(models.Model):
    """
    """
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    summary = models.TextField(null=True, blank=False)
    mime_type = models.CharField(max_length=127, null=True, blank=True)
    type = models.CharField(max_length=16, null=False, blank=True, choices=(
        ('text', 'Text Post'),
        ('photo', 'Photo Post'),
        ('audio', 'Audio Post'),
        ('video', 'Video Post')
    ))
    accessibility = models.CharField(max_length=8, null=False, default='public', choices=(
        ('public', 'Public'),
        ('protected', 'Protected'),
        ('private', 'Private'),
        ('restricted', 'Restricted')
    ))
    is_published = models.BooleanField(null=False, default=True)
    is_active = models.BooleanField(null=False, default=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_constraint=False,
        related_name='post_author',
        db_column='author_id',
        on_delete=models.CASCADE,
        null=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_constraint=False,
        related_name='post_owner',
        db_column='owner_id',
        on_delete=models.CASCADE,
        null=True,
    )
    parent = models.ForeignKey(
        'self',
        db_constraint=False,
        db_column='parent_id',
        null=True,
        blank=True,
    )

    thumbnail = models.URLField(null=True, blank=False,)
    uri = models.URLField(null=True, blank=False)
    general_attributes = models.TextField(serialize=False, null=True, blank=True)
    meta_attributes = models.TextField(serialize=False, null=True, blank=True)
    seo_attributes = models.TextField(serialize=False, null=True, blank=True)
    settings_attributes = models.TextField(serialize=False, null=True, blank=True)
    revision_logs = models.TextField(serialize=False, null=True, blank=True)
    comments_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    created_on = models.DateTimeField(auto_now=False, null=True, blank=True)

    categories = models.ManyToManyField('blog.PostCategoryModel', db_constraint=False, null=True, blank=True)
    tags = models.ManyToManyField('blog.TagModel', db_constraint=False, null=True, blank=True)

    class Meta:
        app_label = "blog"
        db_table = "%s_posts" % app_label
        verbose_name = "blog post"
        verbose_name_plural = 'blog posts'

    def __unicode__(self):
        return self.title


class CommentModel(models.Model):
    """
    """
    message = models.TextField(serialize=False, blank=False, null=False)
    is_anonymous = models.BooleanField(null=False, default=False)
    commentator = models.ForeignKey(settings.AUTH_USER_MODEL, db_constraint=False, null=True, blank=True)
    commentator_meta = models.TextField(serialize=False, null=True, blank=True)
    avator = models.URLField(null=True, blank=True)
    replies_count = models.PositiveIntegerField(null=True, default=0)
    report_flags_count = models.PositiveIntegerField(null=True, default=0)
    is_published = models.BooleanField(null=False, default=True)
    is_approved = models.BooleanField(null=False, default=True)
    revision_logs = models.TextField(serialize=False, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=False)

    parent = models.ForeignKey(
        'self',
        db_constraint=False,
        null=True,
        blank=False,
        db_column='parent_id',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey('blog.PostModel', db_constraint=False, db_column='post_id', null=False)

    class Meta:
        app_label = "blog"
        db_table = "%s_comments" % app_label
        verbose_name = "post comment"
        verbose_name_plural = 'post comments'

    def __unicode__(self):
        return self.message


class TagModel(models.Model):
    """

    """
    name = models.CharField(max_length=127, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=127, null=True, blank=True, unique=True)
    is_active = models.BooleanField(null=False, default=True)

    class Meta:
        app_label = "blog"
        db_table = "%s_tags" % app_label
        verbose_name = "post tag"
        verbose_name_plural = 'post tags'

    def __unicode__(self):
        return self.name