from django.db import models

class Notes(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def short_body(self):
        return self.body[:300]+' ...'

    def date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')
    #to return title name and date to admin-notes page
    def __str__(self):
        return self.title + ", "+ self.date_pretty()
