import config
from Classification import Classification
from HardWare.Camera import Camera
from Model.edu_info import EduInfo
from Model.type import Search


class Application:
    def __init__(self, classifier_pattern=config.CLASSIFIER_PATTERN, img_content=''):
        if classifier_pattern == 'static':
            self.classifier = Classification(config.IMG_PATH)
        else:
            self.classifier = Classification(config.IMG_PATH, img_content=img_content)

        self.search_engine = Search()

        self.camera = Camera()

        self.speaker = None

        self.led_device = None

        self.rotate = None

        self.classify_result = None

        self.garbage_tag = None

        self.try_time = 0

    def set_speaker(self, speaker):
        self.speaker = speaker

    def set_led_device(self, led):
        self.led_device = led

    def set_rotate(self, rotate):
        self.rotate = rotate

    @staticmethod
    def _check_score(score):
        return float(score) > config.CLASSIFIER_THRESHOULD

    def _take_picture_and_classify(self):
        self.camera.take_picture()
        self.classify_result = self.classifier.classify()

    def _get_final_result(self):
        self.garbage_tag = self.search_engine.search(self.classify_result['keyword'])
        self.e = EduInfo(self.classify_result['keyword'])
        result = self.e.get_info()
        result['garbage_tag'] = self.garbage_tag
        return result

    def classify_simple_edition(self):
        self._take_picture_and_classify()

        if self._check_score(self.classify_result['score']):
            result = self._get_final_result()
        else:
            while self.try_time < config.MAX_ROTATE_TIME:
                print('旋转台第{}次转动'.format(str(self.try_time)))
                print("此处省略一些代码")

                """TO DO LIST
                此处应该实现旋转台旋转代码
                """

                self._take_picture_and_classify()
                self.try_time += 1
                if self._check_score(self.classify_result['score']):
                    break
            if self._check_score(self.classify_result['score']):
                result = self._get_final_result()

        self.try_time = 0
        return result


if __name__ == '__main__':
    app = Application()
    print(app.classify_simple_edition())
