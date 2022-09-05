from apiWeb.models.video import Video


class UtilVideo:

    @staticmethod
    def get_video(video: Video):
        try:
            home_video = {"id": int(video.id),
                          "fa_name": str(video.fa_name),
                          "image": str(video.image),
                          "type": str(video.get_type_display()),
                          "link": str(video.link)}
            return home_video
        except Exception as e:
            print("Error video :", str(e))
            return str(e)

    @staticmethod
    def get_new_videos():
        try:
            videos = Video.objects.order_by(
                'id')[:5]
            home_videos = map(lambda video: UtilVideo.get_video(video), videos) if videos else []
            return home_videos
        except Exception as e:
            print("Error new video :", str(e))
            return str(e)

    @staticmethod
    def get_all_videos():
        try:
            all_videos = Video.objects.order_by('id')
            result_videos = map(lambda video: UtilVideo.get_video(video), all_videos) if all_videos else []
            return result_videos
        except Exception as e:
            print("Error all video :", str(e))
            return str(e)
