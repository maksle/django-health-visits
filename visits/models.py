from django.db import models

class Visit(models.Model):
    date = models.DateTimeField('Date of visit')
    location = models.CharField(max_length=255, blank=True)
    notes = models.TextField()

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return self.date.strftime("%m-%d-%Y")

class Provider(models.Model):
    visits = models.ManyToManyField(Visit)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.last_name + ", " + self.first_name[0]
