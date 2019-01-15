# 此项配置用于设置图像识别接口API
CLASSIFICATION_API_NAME = 'baidu'
# 此项配置用于设置图片的编码方式，根据不同调用api的要求进行改写
IMG_ENCODING_PATTERN = 'base64'
# 此项配置用于设置静态图片的路径
IMG_PATH = 'test/1.jpg'
# 此项配置用于设置图片识别的模式，static指通过读取图片文件的形式识别，stream指通过二进制流进行识别
CLASSIFIER_PATTERN = 'static'
# 此项配置数据库的搜索模式，默认为db，其他方式暂未开发
SEARCH_TYPE = 'db'