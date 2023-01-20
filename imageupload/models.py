from django.db import models
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO


class Images(models.Model):
    title = models.CharField(
        max_length=80, blank=False, null=False)
    width = models.IntegerField()
    height = models.IntegerField()
    image_url = models.ImageField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        memfile = BytesIO()

        img = Image.open(self.image_url)
        img.thumbnail((self.width, self.height))
        img.save(memfile, img.format)
        file_name = f'{self.id}.{img.format.lower()}'
        default_storage.save(file_name, memfile)
        self.width = img.width
        self.height = img.height
        self.image_url = file_name
        memfile.close()
        img.close()
        super().save()

