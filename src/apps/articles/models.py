from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(_('Created'), auto_created=True)
    text = models.CharField(_('Text'), max_length=1024, null=False, blank=False)
    image = models.ImageField(_('Image'), upload_to='img_articles', null=True, blank=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return '{}/{}'.format(str(self.id), self.author.username)