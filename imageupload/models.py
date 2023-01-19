from django.db import models
from PIL import Image

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Images(models.Model):
    title = models.CharField(
        max_length=80, blank=False, null=False)
    width = models.IntegerField()
    height = models.IntegerField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image_url.path)
        img.thumbnail((self.width, self.height))
        self.width = img.width
        self.height = img.height
        img.save(self.image_url.path)


