from django.db import models


class articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
