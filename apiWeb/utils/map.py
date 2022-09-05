from apiWeb.models.map import Map


class UtilMap:
    @staticmethod
    def get_map(map: Map):
        try:
            home_map = {"id": int(map.id),
                        "fa_name": str(map.fa_name),
                        "image": str(map.image),
                        "link": str(map.link)}
            return home_map
        except Exception as e:
            print("Error map :", str(e))
            return str(e)

    @staticmethod
    def get_latest_map():
        try:
            latest_maps = Map.objects.order_by('-id')[:6]
            result_maps = map(lambda map: UtilMap.get_map(map), latest_maps) if latest_maps else []
            return result_maps

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_map():
        try:
            all_maps = Map.objects.order_by('-id')
            result_maps = map(lambda map: UtilMap.get_map(map), all_maps) if all_maps else []
            return result_maps

        except Exception as e:
            return [str(e)]