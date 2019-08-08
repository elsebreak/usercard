from django.db import models
from django.shortcuts import reverse
from time import time

from django.utils.text import slugify

def gen_uniq(s):
    new_uniq = slugify(s, allow_unicode=True)
    return new_uniq + '-' + str(int(time()))

class Card(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    uniq = models.SlugField(blank=True, max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='cards')
    date_cr = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('card_read_url', kwargs={'uniq': self.uniq})

    def get_update_url(self):
        return reverse('card_update_url', kwargs={'uniq': self.uniq})

    def get_delete_url(self):
        return reverse('card_delete_url', kwargs={'uniq': self.uniq})

    def save(self, *args, **kwargs):
        if not self.id:
            self.uniq = gen_uniq(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    uniq = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_read_url', kwargs={'uniq': self.uniq})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'uniq': self.uniq})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'uniq': self.uniq})

    def __str__(self):
        return '{}'.format(self.title)
