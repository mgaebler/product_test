from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Forum(models.Model):
    STATE_PUBLISHED = 'published'
    STATE_PREVIEW = 'preview'
    STATE_DEACTIVATED = 'deactivated'
    STATES = (
        (STATE_PUBLISHED, _(u'published')),
        (STATE_PREVIEW, _(u'preview')),
        (STATE_DEACTIVATED, _(u'deactivated')),
    )
    title = models.CharField(_(u'title'), max_length=255)
    description = models.TextField(_(u'description'), blank=True, default='')
    updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'creator'), blank=True, null=True)

    state = models.CharField(max_length=24, choices=STATES, default=u'published',
        help_text=u"""
            Draft: The product test is not visible to everyone.
            Published: The Product test is visible if the 'published at' date is arrived.
            Preview: The Product is visible to every staff member independently of the 'publishing at' date.
        """
)

    def __unicode__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.topic_set.all()])

    def last_post(self):
        return self.topic_set.all().last()


class Topic(models.Model):
    title = models.CharField(_(u'title'), max_length=255)
    description = models.TextField(_(u'description'), max_length=10000, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'creator'), blank=True, null=True)
    created = models.DateField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    closed = models.BooleanField(blank=True, default=False)

    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['position']

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return max(0, self.post_set.count() - 1)

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created").last()

    def __unicode__(self):
        return u"{}".format(self.title)


class PostBase(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'creator'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    body = models.TextField(verbose_name=_(u'body'), max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        abstract = True

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True


class Post(PostBase):
    title = models.CharField(_(u'title'), max_length=255)
    topic = models.ForeignKey(Topic, verbose_name=_(u'topic'))

    def __unicode__(self):
        return u"{}".format(self.title)


class Answer(PostBase):
    post = models.ForeignKey(Post, verbose_name=_(u'post'), related_name="answers")

    class Meta:
        ordering = ("created", )


class ProfaneWord(models.Model):
    word = models.CharField(max_length=60)

    def __unicode__(self):
        return self.word
