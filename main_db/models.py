from django.db import models


# Create your models here.
class RawArticlesData(models.Model):
    date = models.DateTimeField()
    content = models.CharField(max_length=4096)

    class Meta:
        db_table = "raw_articles_data"
