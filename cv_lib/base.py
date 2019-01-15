"""
This is the base class for all the cv_apis
"""
import config


class Base:
    def __init__(self):
        self.img = None

    def classify(self):
        return

    def set_img(self, img: str):
        self.img = img

    def _img_encode(self, img_content: str, coding=config.IMG_ENCODING_PATTERN):
        """
        本函数用于处理图像的编码方式与压缩方式，具体实现由具体的子类根据API接口要求设定
        :param img_content:  图片的二进制流
        :param coding:       二进制流的编码方式
        :return:             编码后的二进制流
        """
        return
