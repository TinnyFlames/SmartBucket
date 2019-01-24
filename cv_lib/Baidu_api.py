from aip import AipImageClassify

import config
import secure
from cv_lib.base import Base


class BaiduApi(Base):
    def __init__(self):
        super().__init__()
        self.APP_ID = secure.DU_CV_API_ID
        self.API_KEY = secure.DU_CV_API_KEY
        self.SECRET_KEY = secure.DU_CV_SECRET_KEY
        # this is the source object to be wrapped
        self.baidu_client = AipImageClassify(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def classify(self):
        self.img = self._img_encode(self.img)
        return self.baidu_client.advancedGeneral(self.img)

    def _img_encode(self, img_content: str, coding=config.IMG_ENCODING_PATTERN):
        """
        百度的sdk包含了对图片进行处理的相关代码，此处图片编码不做实现
        :param img_content:
        :param coding:
        :return:
        """
        return self.img
