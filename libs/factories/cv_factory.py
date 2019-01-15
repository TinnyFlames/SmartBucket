import config
from cv_lib.Baidu_api import BaiduApi
from libs.factories.base import FactoryBase


class CvApiFactory(FactoryBase):
    """
    本类属于抽象工厂模式中的具体工厂，负责生产与视觉相关的API对象
    在调用工厂方法get_instance前，必须调用set_img函数对图片信息进行设置，
    """
    def __init__(self):
        super().__init__()
        self.img = None

    def set_img(self, img_path='', img_content='', pattern='static'):
        """
        此函数用于向工厂对象中添加图片的相关信息，可以处理图片存储在静态文件夹下和二进制流的情形
        默认使用static模式对图片进行处理
        Notice: 图片的压缩方式与编码方式在本函数中均不处理，延迟到具体API子类中进行

        :param img_path: 图片的路径
        :param img_content: 图片的二进制内容
        :param pattern:  读取图片的方式 static代表图片文件存在于目录下，stream则代表图片
                         用流的形式传递
        :return:
        """
        if pattern == 'static':
            with open(img_path, 'rb') as fp:
                self.img = fp.read()
        elif pattern == 'stream':
            self.img = img_content
        else:
            raise Exception('argument : pattern wrong!')

    def get_instance(self, api_name=config.CLASSIFICATION_API_NAME):
        """
        本函数用于生产对应的工厂对象，instance字典中记录了系统支持的全部api类型
        可以在需要时注册加入相应的类
        默认使用百度API

        :param api_name: 需要调用api的名字
        :return: 具体api的对象实例
        """
        instance = {
            'baidu': BaiduApi,
        }[api_name]()
        instance.set_img(self.img)
        return instance
