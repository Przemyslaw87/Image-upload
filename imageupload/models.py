from django.db import models
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO


class Images(models.Model):
    """
    A model representing an image, including its title, original file name, dimensions, and a URL to the image file.

    Attributes:
        title (str): The title of the image.
        original_name_file (str): The original file name of the image.
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        image_url (ImageField): The URL of the image file.
    """
    title = models.CharField(max_length=80, blank=False, null=False)
    original_name_file = models.TextField(default='example_image')
    width = models.IntegerField()
    height = models.IntegerField()
    image_url = models.ImageField()

    def upload_resize(self):
        """
        Resizes the image file associated with the current instance of the Images model and updates the width, height,
         and original file name fields.

        This function uses the PIL library to open the image file, resize it and save it to the server.
        It also updates the original_name_file, width, height and image_url fields of the current instance.
        """
        memfile = BytesIO()

        img = Image.open(self.image_url)
        img.thumbnail((self.width, self.height))
        img.save(memfile, img.format)
        file_name = f'{self.id}.{img.format.lower()}'
        default_storage.save(file_name, memfile)
        self.original_name_file = self.image_url
        self.width = img.width
        self.height = img.height
        self.image_url = file_name
        memfile.close()
        img.close()
        super().save()

    def save(self, *args, **kwargs):
        """
        Saves the current instance of the Images model to the database and calls the upload_resize method to resize the
        image file.

        This method overrides the default save method of the Model class and calls the upload_resize method to resize
        the image file before saving the instance to the database.
        """
        super().save(*args, **kwargs)
        self.upload_resize()
