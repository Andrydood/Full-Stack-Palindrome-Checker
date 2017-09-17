# @Author: andreacasino
# @Date:   2017-09-14T19:03:34+01:00
# @Last modified by:   andreacasino
# @Last modified time: 2017-09-15T19:08:02+01:00


from django.db import models

#Define palindrome class
class Palindrome(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)

    class Meta:
        ordering = ('-created',)
