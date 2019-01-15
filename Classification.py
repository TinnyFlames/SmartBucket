import config
from libs.filter.classify_filter import filter_data
from libs.factories.cv_factory import CvApiFactory


class Classification:
    def __init__(self, path: str, img_content='', pattern='static'):
        self.img_path = path
        self.img_content = img_content
        self.pattern = pattern
        if self.pattern == 'static':
            self.api = self._set_api_for_static()
        else:
            self.api = self._set_api_for_stream()

    def _set_api_for_static(self):
        """
        注意，本函数在设置cv工厂时，传入的图片格式按照静态自动处理
        若选择自己搭建的远程服务器，应使用流的方式进行传输。

        :return: 本函数返回具体api的实例供构造函数使用
        """
        self.api_name = config.CLASSIFICATION_API_NAME
        cv_factory = CvApiFactory()
        cv_factory.set_img(img_path=self.img_path, pattern=self.pattern)
        return cv_factory.get_instance()

    def _set_api_for_stream(self):
        """
        注意，本函数按流处理照片
        若选择自己搭建的远程服务器，应使用流的方式进行传输。

        :return: 本函数返回具体api的实例供构造函数使用
        """
        self.api_name = config.CLASSIFICATION_API_NAME
        cv_factory = CvApiFactory()
        cv_factory.set_img(img_content=self.img_content, pattern=self.pattern)
        return cv_factory.get_instance()

    def classify(self):
        return filter_data(self.api.classify())
