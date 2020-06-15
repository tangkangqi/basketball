
from PIL import Image
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Spider(object):
    def __init__(self):
        driver_path = r'/Users/vivo/Desktop/Install/chrome/chromedriver'
        self.browser = webdriver.Chrome(executable_path=driver_path)
        # 最大等待时间
        self.wait = WebDriverWait(self.browser, 10)
        self.url = 'https://blog.csdn.net/gklcsdn/article/details/103659429'

    def view_page(self):
        """
        访问页面
        :return:
        """
        self.browser.get(self.url)

        # 窗口最大化
        self.browser.maximize_window()

    def get_full_image(self):
        """
        截取整页图片并转换成二进制格式数据
        :return:
        """
        complete_image = self.browser.get_screenshot_as_png()

        # 转换成二进制数据格式
        bytes_data = Image.open(BytesIO(complete_image))
        return bytes_data

    def get_logo(self, bytes_data):
        """
        定位到主要获取的图片, 并保存
        :return:
        """

        '''
        logo = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_content"]/div[1]/a/img')))

        # 图片左上角坐标
        x, y = logo.location.values()

        # 图片大小
        logo_size = logo.size

        # logo 大小
        height = logo_size.get('height')
        width = logo_size.get('width')
        '''
        x , y = 0, 0
        height, width = 500, 500
        # 裁剪目标位置
        target_picture = bytes_data.crop((x, y, x + width, y + height))
        target_picture.show()
        target_picture.save('logo.png')

    def __call__(self, *args, **kwargs):
        """
        运行逻辑(类的实例可调用)
        :param args:
        :param kwargs:
        :return:
        """
        self.view_page()
        bytes_data = self.get_full_image()
        self.get_logo(bytes_data)
        self.browser.quit()


if __name__ == '__main__':
    s = Spider()
    s()

