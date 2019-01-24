from aip import AipSpeech
import secure
from speaker_lib.base import SpeakerBase
import config


class BaiduApi(SpeakerBase):
    def __init__(self):
        super().__init__()
        self.APP_ID = secure.DU_AUDIO_API_ID
        self.API_KEY = secure.DU_AUDIO_API_KEY
        self.SECRET_KEY = secure.DU_AUDIO_SECRET_KEY
        self.baidu_client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def get_audio_file(self):
        """
        本函数用于将文本文件转换成本地的mp3格式的文件，
        并将相应的mp3文件存储在配置文件设置的路径中
        :return: 如果获取音频文件成功，返回True 失败则返回False
        """
        result = self.baidu_client.synthesis(self.speak_message, 'zh', 1, {
            "vol": config.SPEAKER_SPEAK_VOL,
            "spd": config.SPEAKER_SPEAK_SPEED,
            "pit": config.SPEAKER_SPEAK_TONE,
            "per": config.SPEAKER_SPEAK_PERSON
        })
        print(result)
        if not isinstance(result, dict):
            with open(config.AUDIO_FILE_PATH, 'wb') as f:
                f.write(result)
            return True
        else:
            return False


if __name__ == '__main__':
    bs = BaiduApi()
    bs.set_speak_message('你好现在开始测试')
    print(bs.get_audio_file())
