from apiWeb.models.guide import Guide


class UtilGuide:
    @staticmethod
    def get_guide(guide: Guide):
        try:
            home_guide = {"id": int(guide.id),
                          "fa_name": str(guide.fa_name),
                          "image": str(guide.image),
                          "link": str(guide.link)}
            return home_guide
        except Exception as e:
            print("Error guide :", str(e))
            return str(e)

    @staticmethod
    def get_latest_guide():
        try:
            latest_guides = Guide.objects.order_by('-id')[:6]
            result_guides = map(lambda guide: UtilGuide.get_guide(guide), latest_guides) if latest_guides else []
            return result_guides

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_guide():
        try:
            all_guides = Guide.objects.order_by('-id')
            result_guides = map(lambda guide: UtilGuide.get_guide(guide), all_guides) if all_guides else []
            return result_guides

        except Exception as e:
            return [str(e)]
