from django.contrib import admin
from .models import (
    Blog,
    Category,
    Comment,
    Like,
)

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)