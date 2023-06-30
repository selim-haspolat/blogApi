from django.db import models
from django.contrib.auth.models import User

# ---------- CategoryModel ----------
class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ---------- CommentModel ----------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Blog', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.user} {self.post}'


# ---------- LikeModel ----------
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Blog', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} {self.post}'

# ---------- BlogModel ----------
class Blog(models.Model):

    STATUS = (
        ('d', 'draft'),
        ('p', 'published'),
    )

    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.URLField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=1, default='p')

    def __str__(self):
        return self.title
