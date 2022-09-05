from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from apiWeb.utils.general import Util
from apiWeb.utils.guide import UtilGuide
from apiWeb.utils.map import UtilMap
from apiWeb.utils.prayer import UtilPrayer
from apiWeb.utils.song import UtilSong
from apiWeb.utils.video import UtilVideo


class home_video(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilVideo.get_new_videos())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_song(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilSong.get_latest_songs())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_prayer(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilPrayer.get_latest_prayer())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_map(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilMap.get_latest_map())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_guide(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilGuide.get_latest_guide())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})
