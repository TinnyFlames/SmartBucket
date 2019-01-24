import config


class SpeakerBase:
    def __init__(self):
        self.api_name = config.SPEAKER_API_NAME
        self.speak_message = None

    def set_speak_message(self, msg: str):
        self.speak_message = msg

    def get_audio_file(self):
        return
