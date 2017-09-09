from __future__ import unicode_literals

from django.db import models

COPYRIGHT = 'RIG'
COPYLEFT = 'LEFT'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

# Create your models here.
class Photo(models.Model):

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    lisence = models.CharField(max_length=3,choices=LICENSES)