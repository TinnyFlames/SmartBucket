import os
import config


class EduInfo:
    def __init__(self, label):
        self._label = label
        self.cache = []
        self.result = dict()

    def set_tag(self, tag: str):
        if len(self._label) > 0:
            self._label = tag
        else:
            raise Exception("Invalid tag length")

    def _add_to_cache(self, element: dict):
        if len(self.cache) >= config.MAX_CACHE_NUM:
            # 注意 此处因为时间问题，没有实现性能更优化的cache替换策略
            # 如果时间充足，应该将此处改为LRU替换算法，可以达到最佳性能
            # 当用此算法发现速度慢时，可以适当增加cache容量缓解问题
            self.cache[config.MAX_CACHE_NUM - 1] = element
        else:
            self.cache.append(element)

    def _search_cache(self):
        for saved_dicts in self.cache:
            if saved_dicts['garbage_tag'] == self._label:
                return True, saved_dicts
        return False, dict()

    def _get_video_or_text(self) -> dict:
        video_path = os.path.join(config.STATIC_FILE_PATH, 'video')
        text_path = os.path.join(config.STATIC_FILE_PATH, 'video')
        print(video_path)
        for file_names in os.listdir(video_path):
            if file_names == self._label:
                result = {
                    'success_flag': True,
                    'garbage_label': self._label,
                    'edu_resource_type': 'video',
                    'edu_resource_content': os.path.join(video_path, file_names)
                }
                self._add_to_cache(result)
                return result

        for file_names in os.listdir(text_path):
            if file_names == self._label:
                with open(os.path.join(text_path, file_names), 'r') as f:
                    content = f.read()

                result = {
                    'success_flag': True,
                    'garbage_label': self._label,
                    'edu_resource_type': 'text',
                    'edu_resource_content': content,
                }
                self._add_to_cache(result)
                return result

        return {
            'success_flag': False,
            'garbage_label': self._label,
            'edu_resource_type': '',
            'edu_resource_content': '',
        }

    def get_info(self):
        is_in_cache, result = self._search_cache()
        if is_in_cache:
            return result
        else:
            return self._get_video_or_text()


if __name__ == '__main__':
    e = EduInfo("apple")
    print(e.get_info())
