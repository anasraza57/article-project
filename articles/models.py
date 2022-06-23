import base64
from io import BytesIO

from PIL import Image
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='images/')
    thumbnail = models.CharField(max_length=10000, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.image:
            self.thumbnail = None
        else:
            thumbnail_size = 50, 50
            data_img = BytesIO()
            tiny_img = Image.open(self.image)
            tiny_img.thumbnail(thumbnail_size)
            tiny_img.save(data_img, format="BMP")
            tiny_img.close()
            try:
                self.thumbnail = "data:image/jpg;base64,{}".format(
                    base64.b64encode(data_img.getvalue()).decode("utf-8")
                )
            except UnicodeDecodeError:
                self.blurred_image = None

        super(Article, self).save(force_insert, force_update, using, update_fields)
