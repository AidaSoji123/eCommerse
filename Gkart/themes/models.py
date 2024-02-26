from django.db import models

class SiteSetting(models.Model):
    banner = models.ImageField(upload_to='site/', verbose_name="Banner Image")
    caption = models.TextField(verbose_name="Caption")

    def __str__(self) -> str:
        return "Site Setting"
