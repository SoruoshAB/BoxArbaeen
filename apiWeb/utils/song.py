from apiWeb.models.song import Song


class UtilSong:
    @staticmethod
    def get_song(song: Song):
        try:
            home_song = {"id": str(song.id),
                         "fa_name": str(song.fa_name),
                         "image": str(song.image),
                         "singer": str(song.singer),
                         "link": str(song.link),
                         }
            return home_song
        except Exception as e:
            print("Error song :", str(e))
            return str(e)

    @staticmethod
    def get_latest_songs():
        try:
            latest_songs = Song.objects.order_by('-id')[:10]
            result_songs = map(lambda song: UtilSong.get_song(song), latest_songs) if latest_songs else []
            return result_songs

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_songs():
        try:
            all_songs = Song.objects.order_by('-id')
            result_songs = map(lambda song: UtilSong.get_song(song), all_songs) if all_songs else []
            return result_songs

        except Exception as e:
            return [str(e)]
