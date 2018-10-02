from django.http import HttpResponse
from reply_comment_facebook.reply_script.autoresponder import monitor_fb_comments

def index(request):
    monitor_fb_comments()
    return HttpResponse("Hello, world. You're at the polls index.")