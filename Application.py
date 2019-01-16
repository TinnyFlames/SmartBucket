import config
from Classification import Classification
from Model.type import Search


class Application:
    def __init__(self, classifier_pattern=config.CLASSIFIER_PATTERN, img_content=''):
        if classifier_pattern == 'static':
            self.classifier = Classification(config.IMG_PATH)
        else:
            self.classifier = Classification(config.IMG_PATH, img_content=img_content)

        self.search_engine = Search()

        self.speaker = None

        self.led_device = None

        self.rotate = None

        self.camera = None

    def set_speaker(self, speaker):
        self.speaker = speaker

    def set_led_device(self):
        pass

    def set_rotate(self):
        pass

    def set_camera(self):
        pass
