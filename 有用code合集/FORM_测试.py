# 通过WebDriver操作进行查找
# 无头浏览器，支持无浏览器操作

from selenium import webdriver
import time
driver_path = r'/Users/vivo/Desktop/Install/chrome/chromedriver'


def main():
    # 创建浏览器实例
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://map.baidu.com/'
    driver.get(url)

    # 打印出HTML页面的标题
    print(driver.title)

    # 得到页面的快照，得到百度首页的的截图
    driver.save_screenshot('baidumap.png')

    # id='kw'是百度的输入框
    element1 = driver.find_element_by_id('sole-input')
    element1.send_keys(u'上海')


    # id='su'是百度搜索的按钮，百度一下，click模拟点击
    driver.find_element_by_id('search-button').click()
    element1.clear()

    # 搜索需要时间，等待一下再截图
    time.sleep(5)
    driver.save_screenshot('上海.png')

    time.sleep(120)
    # 关闭浏览器
    driver.close()


if __name__ == '__main__':
    main()