import config
from libs.factories.base import FactoryBase
from speaker_lib.Baidu_api import BaiduApi


class SpeakFactory(FactoryBase):
    def __init__(self):
        super().__init__()
        self.message = None

    def get_instance(self):
        instance = {
            'baidu': BaiduApi
        }[config.SPEAKER_API_NAME]()

        if self.message is None:
            raise Exception("message must be set before run get_instance()")

        instance.set_speak_message(self.message)
        return instance

    def set_message(self, msg: str):
        """
        本函数用于设置speaker所需要的信息
        此函数必须在调用get_instance()函数前得到调用，否则会在获取实例时抛出异常

        :param msg:需要转换成语音的相关信息，长度需符合配置文件中规定要求，否则抛出异常
        :return:
        """
        if msg and 0 < len(msg) < config.SPEAKER_SPEAK_MAX_LEN[config.SPEAKER_API_NAME]:
            self.message = msg
        else:
            raise Exception("message is None or message Len is too long")
