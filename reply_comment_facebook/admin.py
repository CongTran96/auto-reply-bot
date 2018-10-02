from django.contrib import admin
from reply_comment_facebook.models import Distributor, Device, Comment

# Register your models here.
admin.site.register([Distributor, Device, Comment])