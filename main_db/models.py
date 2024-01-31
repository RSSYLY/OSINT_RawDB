from django.db import models


# Create your models here.
class RawArticlesData(models.Model):
    date = models.DateTimeField()
    content = models.CharField(max_length=4096)
    word_cloud_img = models.ImageField(upload_to='word_cloud/', null=True, blank=True)

    class Meta:
        db_table = "raw_articles_data"
