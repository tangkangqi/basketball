# 通过WebDriver操作进行查找
# 无头浏览器，支持无浏览器操作

from selenium import webdriver
import time
driver_path = r'/Users/vivo/Desktop/Install/chrome/chromedriver'

def get_city_map(driver, city_name, fout_name):
    # id='kw'是百度的输入框
    element1 = driver.find_element_by_id('sole-input')
    element1.clear()
    element1.send_keys(city_name)

    # id='su'是百度搜索的按钮，百度一下，click模拟点击
    driver.find_element_by_id('search-button').click()
    element1.clear()

    # 搜索需要时间，等待一下再截图
    time.sleep(5)
    driver.save_screenshot(fout_name)

def main():
    # 创建浏览器实例
    driver = webdriver.Chrome(executable_path=driver_path)
    url = 'http://map.baidu.com/'
    driver.get(url)

    # 打印出HTML页面的标题
    print(driver.title)

    # 得到页面的快照，得到百度首页的的截图
    driver.save_screenshot('baidumap.png')

    city_names = [v.strip() for v in open('city_names.txt','r').readlines()]
    for i, v in enumerate(city_names):
        fout_name = "%s_%s.png"%("{:0>3d}".format(i+1), v)
        get_city_map(driver, city_name=v, fout_name = fout_name)



    time.sleep(120)
    # 关闭浏览器
    driver.close()


if __name__ == '__main__':
    main()