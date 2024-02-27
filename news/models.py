from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractBaseModel):
    name = models.CharField(max_length=28)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class New(AbstractBaseModel):
    title = models.CharField(max_length=125)
    body = models.TextField()
    img = models.ImageField(upload_to="news/")
    category_id = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Author(AbstractBaseUser):
    name = models.CharField(max_length=56)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Comment(AbstractBaseModel):
    body = models.TextField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    news_id = models.ForeignKey(New, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Tag(AbstractBaseModel):
    text = models.TextField()

    def __str__(self):
        return self.text


class New_tag(AbstractBaseModel):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    news_id = models.ForeignKey(New, on_delete=models.CASCADE)


class Contact(AbstractBaseModel):
    name = models.CharField(max_length=56)
    email = models.EmailField()
    message = models.TextField()
