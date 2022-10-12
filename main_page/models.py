from django.db import models
import uuid
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    ingredients = models.TextField(max_length=1_000, blank=False)
    desc = models.TextField(max_length=1_000, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name}: {self.name}: {self.position}'

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ('position', )


class Gallery(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)


class Events(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    item = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField(verbose_name="Event price")
    description = models.TextField(max_length=1_000, blank=False)
    subtitle1 = models.TextField(blank=True, verbose_name="sub1")
    subtitle2 = models.TextField(blank=True, verbose_name="sub2")
    subtitle3 = models.TextField(blank=True, verbose_name="sub3")
    aftertitle = models.TextField(blank=True, verbose_name="After text")
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.item}: {self.price}'

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class Whuus(models.Model):
    whuus_order = models.SmallIntegerField(unique=True, verbose_name="Position")
    whuus_title = models.CharField(max_length=20, verbose_name="Title")
    whuus_about = models.CharField(max_length=100, verbose_name="Description")

    def __str__(self):
        return self.whuus_title

    class Meta:
        verbose_name = "Why us"
        verbose_name_plural = "Why us"
        ordering = ("whuus_order",)

class MyCarousel(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    carousel_name = models.CharField(max_length=30, verbose_name="name")
    carousel_about = models.TextField(verbose_name="about")
    carousel_image = models.ImageField(upload_to=get_file_name, verbose_name="photo")
    carousel_access = models.BooleanField(default=True, verbose_name="acces")

    def __str__(self):
        return self.carousel_name

    class Meta:
        verbose_name = "MyCarousel"
        verbose_name_plural = "MyCarousel"


class Chefs(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    chefs_order = models.SmallIntegerField(unique=True)
    chefs_name = models.CharField(max_length=30, verbose_name="name")
    chefs_pro = models.CharField(max_length=30, verbose_name="profession")
    chefs_twitter = models.CharField(max_length=50, verbose_name="teitter", blank=True)
    chefs_facebook = models.CharField(max_length=50, verbose_name="facebook", blank=True)
    chefs_instagram = models.CharField(max_length=50, verbose_name="instagram", blank=True)
    chefs_linkedin = models.CharField(max_length=50, verbose_name="linkedin", blank=True)
    chefs_photo = models.ImageField(upload_to=get_file_name, verbose_name="Photo")

    def __str__(self):
        return self.chefs_name

    class Meta:
        verbose_name = "Chefs"
        verbose_name_plural = "Chefs"
        ordering = ("chefs_order",)


class Emotions(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    emotions_order = models.SmallIntegerField(unique=True)
    emotions_name = models.CharField(max_length=30, verbose_name="name")
    emotions_pro = models.CharField(max_length=30, verbose_name="profession")
    emotions_photo = models.ImageField(upload_to=get_file_name, verbose_name="Photo")
    emotions_rating = models.SmallIntegerField(help_text='1-5')
    emotions_message = models.TextField(max_length=500)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.emotions_name

    class Meta:
        verbose_name = "Emotions"
        verbose_name_plural = "Emotions"
        ordering = ("emotions_order",)
