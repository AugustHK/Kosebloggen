from django.db import models
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # thumbnail
    # author

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) < 51:
            return self.body
        else:
            return self.body[:50] + "..."