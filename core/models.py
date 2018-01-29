from django.db import models


class Card(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    detail = models.CharField(max_length=1000, blank=False)
    relevance = models.SmallIntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='cards', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('relevance',)
