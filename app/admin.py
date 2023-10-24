from django.contrib import admin
from app.models import User, Product, Comment, Message
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Message)
