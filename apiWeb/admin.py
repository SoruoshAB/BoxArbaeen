from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models.cat import Category
from .models.guide import Guide
from .models.map import Map
from .models.prayer import Prayer
from .models.song import Song
from .models.video import Video

admin.site.site_header = "Arbaeen Admin Panel"

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Category)
admin.site.register(Guide)
admin.site.register(Map)
admin.site.register(Prayer)
admin.site.register(Song)
admin.site.register(Video)
