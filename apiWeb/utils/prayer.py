from apiWeb.models.prayer import Prayer


class UtilPrayer:
    @staticmethod
    def get_prayer(prayer: Prayer):
        try:
            home_prayer = {"id": int(prayer.id),
                           "fa_name": str(prayer.fa_name),
                           "image": str(prayer.image),
                           "link": str(prayer.link)}
            return home_prayer
        except Exception as e:
            print("Error prayer :", str(e))
            return str(e)

    @staticmethod
    def get_latest_prayer():
        try:
            latest_prayers = Prayer.objects.order_by('-id')[:6]
            result_prayers = map(lambda prayer: UtilPrayer.get_prayer(prayer), latest_prayers) if latest_prayers else []
            return result_prayers

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_prayer():
        try:
            all_prayers = Prayer.objects.order_by('-id')
            result_prayers = map(lambda prayer: UtilPrayer.get_prayer(prayer), all_prayers) if all_prayers else []
            return result_prayers

        except Exception as e:
            return [str(e)]
