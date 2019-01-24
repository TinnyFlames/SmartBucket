import config
from libs.factories.speaker_factory import SpeakFactory


class Speaker:
    def __init__(self):
        self.message = None
        self.str_to_voice_api = None

    def set_message(self, msg: str):
        """
        本函数用于给API传递msg信息，在设置的同时，也会将相应的API进行设定
        -- ！ --  本函数必须在执行transform函数之前被调用
        :param msg: 需要调用的信息，长度不超过150个字符
        :return:
        """
        self.message = msg
        self._set_api_for_str2voice(self.message)

    @staticmethod
    def _set_api_for_str2voice(msg: str):
        """
        本函数用于调用相关的API工厂，生成语音合成的API对象
        :param msg: 需要调用的信息，长度不超过150个字符
        :return: 语音合成API
        """
        speaker_factory = SpeakFactory()
        speaker_factory.set_message(msg)
        return speaker_factory.get_instance()

    def set_new_message(self, msg: str):
        """
        为API设置新的信息，设置完成后需要再次调用transform函数
        -- ！ -- 信息需小于150字，否则会抛出异常
                如信息大于150字，请在外层手动切分，多次调用
        :param msg:
        :return:
        """
        if msg and 0 < len(msg) < config.SPEAKER_SPEAK_MAX_LEN[config.SPEAKER_API_NAME]:
            self.str_to_voice_api.speak_message = msg
        else:
            raise Exception("msg length not match Exception")

    def transform(self):
        """
        本函数将会执行文本到语音的转换,并将返回的MP3文件生成到指定的目录
        Notice：本函数设计时，只是用来执行并执行一次识别
                这意味着语音文件只能同时存在一份
                如果有一次识别超过150字的需求，需自行改写相关函数
        :return:
        """
        return self.str_to_voice_api.get_audio_file()

