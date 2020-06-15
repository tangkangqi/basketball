from selenium import webdriver
import time

# chromedriver所在目录
driver_path = r'/Users/vivo/Desktop/Install/chrome/chromedriver'
def func():
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://www.douban.com/')

    # 找到登陆框架
    iframe = driver.find_element_by_tag_name('iframe')
    # 跳转到登陆框架
    iframe = driver.switch_to.frame(iframe)

    # 定位并点击【密码登陆】
    psw_botton = driver.find_element_by_xpath('//li[contains(@class,"account-tab-account")]')
    psw_botton.click()

    # 定位并输入用户名
    input1 = driver.find_element_by_name('username')
    input1.send_keys('输入你的手机号或邮箱***')

    # 定位并输入密码
    input2 = driver.find_element_by_name('password')
    input2.send_keys('输入你的密码***')

    # 定位并点击【下次自动登录】
    remember_botton = driver.find_element_by_id('account-form-remember')
    remember_botton.click()

    # 登陆
    login_botton = driver.find_element_by_xpath('//a[contains(@class,"btn-account")]')
    time.sleep(10)
    login_botton.click()


if __name__ == '__main__':
    func()