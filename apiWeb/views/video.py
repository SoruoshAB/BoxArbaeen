from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from apiWeb.utils.general import Util
from apiWeb.utils.video import UtilVideo


class videos(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilVideo.get_all_videos())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})
