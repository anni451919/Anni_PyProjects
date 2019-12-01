from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://cn.nytimes.com/")
driver.maximize_window()
print(driver.title)
ref_text = str(input("enter field which you want to click :"))
for i in range(1, 16):
    #ref_text = "商业与经济"
    main_path = "//div[@class='cf no-content'][1]/ul[1]/li[replace_val]/a"
    ref_path = main_path.replace("replace_val", str(i))
    act_path = driver.find_element_by_xpath(ref_path)
    print(act_path.text)
    time.sleep(3)
    if act_path.text == ref_text:
        print("got element")
        driver.find_element_by_xpath(ref_path).click()
        break
    else:
        print("not got element")
    #continue
