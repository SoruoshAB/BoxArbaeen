from django.urls import path

from apiWeb.views.guide import guides
from apiWeb.views.home import home_video, home_song, home_prayer, home_map, home_guide
from apiWeb.views.map import maps
from apiWeb.views.prayer import prayers
from apiWeb.views.song import songs
from apiWeb.views.video import videos

urlpatterns = [
    # path('home/cat', home_category.as_view()),
    path('home/videos', home_video.as_view()),
    path('home/songs', home_song.as_view()),
    path('home/prayers', home_prayer.as_view()),
    path('home/maps', home_map.as_view()),
    path('home/guides', home_guide.as_view()),
    #
    path('videos', videos.as_view()),
    path('songs', songs.as_view()),
    path('prayers', prayers.as_view()),
    path('guides', guides.as_view()),
    path('maps', maps.as_view()),

]
