from django.conf import settings # type: ignore
from django.db import models # type: ignore
from django.utils import timezone # type: ignore

from django.urls import reverse # type: ignore

from taggit.managers import TaggableManager # type: ignore



class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'





    class Effectiveness(models.TextChoices):
        GD = 'GD', 'Good'
        OK = 'OK', 'May be'
        IDK = 'IDK', 'Idk'
        NG = 'NG', 'Not good'
        DN = 'DN', 'Dangerous'

    #tags = TaggableManager()    

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    hack_image = models.TextField(max_length=60, default='images/pool_noodle.webp')
    body_hack = models.TextField(default='No hack')
    comment_image = models.TextField(max_length=60, default='images/pexels-yankrukov_smaller.jpg')
    body_comment = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

   

    effectiveness = models.CharField(
        max_length=3,
        choices=Effectiveness,
        default=Effectiveness.IDK
    )




    tags = TaggableManager() 

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.





    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[               
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
                
            ]
        )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
        models.Index(fields=['created']),
        ]
        
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'