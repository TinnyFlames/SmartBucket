import config
import cv2


class Camera:
    """
    本类负责完成摄像头的相关工作，包括摄像头的开启，拍照，读取视频流与关闭清理的工作。
    为了方便起见，本类直接包装opencv相关的方法，如果需要对访问底层摄像头的类库进行
    更换，则需要使用新类继承本类并重写相关的方法
    """
    def __init__(self):
        """
        cap: 读取视频流的句柄，本类包装的核心变量
        _camera_flag: 摄像头开启的标志位，可以随时
                     访问本变量拿到摄像头的状态
                     需要注意的是，本类负责维护标志位状态，
                     任何情况下不得在外部改写标志位，此标志位仅设为
                     只读项
        image: 用于在内存中存储读取到的图像信息，不过本变量不对外提供访问权限
        """
        self.cap = cv2.VideoCapture()
        self._camera_flag = False
        self._image = None

    def open_camera(self):
        """
        本函数用于打开摄像机
        默认打开0号摄像机位置，如果需要修改，可以在配置文件中进行
        :return: 返回摄像机状态的标志位
        """
        self._camera_flag = self.cap.open(config.CAMERA_NUM)
        return self._camera_flag

    def _check_status(self)->bool:
        """
        检查摄像头的状态，可以用来检查摄像头是否开启或者是否成功开启
        :return:
        """
        return self._camera_flag

    def take_picture(self):
        """
        保存图片并在指定位置存储

        在保存图片时，函数会判断摄像头是否处在开启状态
        如果摄像头开启，将会从视频流中读取的图像直接写入
        相反的，如果摄像头关闭，函数将会主动打开摄像头并写入相关信息

        值得注意的是，在这里开启摄像头时，函数并没有改写摄像头的标志位
        一般情况下，应该不会出现问题，但是如果发现在关闭时出现一些问题，
        可以检查本函数执行是否被中断。
        :return:
        """
        if self._check_status():
            cv2.imwrite(config.IMG_PATH, self._image)
        else:
            self.cap.open(config.CAMERA_NUM)
            flag, frame = self.cap.read()
            cv2.imwrite(config.IMG_PATH, frame)
            self.cap.release()

    def get_instant_frame(self):
        """
        本函数负责返回提供给GUI荧幕显示的图像
        原始的图像就会被缩放成在配置文件中规定的大小
        原始图像的色彩通道也会转换为PyQT显示需要的格式
        :return:
        """
        flag, self._image = self.cap.read()
        show = cv2.resize(self._image, config.IMAGE_SIZE_FOR_SCREEN)
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        return show

    def close(self):
        """
        释放摄像头的相关资源
        <!> 注意，不可以多次释放资源，否则会抛出相应的异常
        :return:
        """
        if self._check_status():
            self.cap.release()
            self._camera_flag = False
        else:
            raise Exception("multi closed!")

