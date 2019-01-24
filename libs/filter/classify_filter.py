import config


class BaiduFilter:
    result = dict()

    @classmethod
    def get_highest_result(cls, array: list)->dict:
        """
        因为API默认降序排列所有的识别结果，所以取第一个元素既为最高值

        :param array: 所有识别结果的列表
        :return: 返回得分最高的字典
        """
        return array[0]

    @classmethod
    def get_filtered_data(cls, raw_data: dict):
        """
        本函数用于过滤返回数据中无用的部分，仅保存识别的score 与 keyword
        若判断时发现，识别失败，将会返回空字典

        :param raw_data:百度api返回的原始数据，默认为字典形式
        :return: 返回一个字段过滤后的字典
        """
        if 'result_num' in raw_data.keys() and int(raw_data['result_num']) > 0:
            result_array = raw_data['result']
            highest_result = cls.get_highest_result(result_array)
            cls.result['score'] = highest_result['score']
            cls.result['keyword'] = highest_result['keyword']

        return cls.result


"""
本字典用于映射所有的filter类，新增API时应在此文件新建相关的filter_class并在本字典下注册
"""
filter_type = {
    'baidu': BaiduFilter,
}


def filter_data(raw_data):
    """

    外部调用此函数完成过滤的功能，修改配置文件可以方便的改变filter类

    """
    return filter_type[config.CLASSIFICATION_API_NAME]().get_filtered_data(raw_data)
