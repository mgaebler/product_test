from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Forum(models.Model):
    title = models.CharField(_(u'title'), max_length=255)
    description = models.TextField(_(u'description'), blank=True, default='')
    updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'creator'),  blank=True, null=True)

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

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return max(0, self.post_set.count() - 1)

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created").last()

    def __unicode__(self):
        return u"{}".format(self.title)


class Post(models.Model):
    title = models.CharField(_(u'title'), max_length=255)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'creator'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    topic = models.ForeignKey(Topic, verbose_name=_(u'topic'))
    body = models.TextField(verbose_name=_(u'body'), max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True


class ProfaneWord(models.Model):
    word = models.CharField(max_length=60)

    def __unicode__(self):
        return self.word
