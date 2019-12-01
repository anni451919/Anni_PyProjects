from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://mail.google.com/mail")
driver.maximize_window()
driver.find_element_by_id("identifierId").send_keys("annipremadp@gmail.com")
# driver.find_element_by_id("identifierId").send_keys("anni.dp94@gmail.com")
driver.find_element_by_xpath("//span[text()='Next']").click()
'''
varif = driver.find_element_by_xpath("//spam")
val = varif.is_selected()
if val:
    attachment = driver.find_element_by_xpath("//*[@class='yE']/../../td[5]/div[1]/span[1]")
    size = attachment.size
    print(size)
else:
    print("plz enter val")'''

sleep(3)
driver.find_element_by_xpath("//input[@type='password']").send_keys("8310156917")
driver.find_element_by_xpath("//span[text()='Next']").click()

sleep(3)
# to find out number of mail which is having attachment
attachment = driver.find_elements_by_xpath("//*[@class='yE']")
size = len(attachment)
print(size)

# to get the text or name of the sent person in the attachment mail
for i in range(1, size + 1):
    ref_xpath = "(//*[@class='yE']/../../td[5]/div[2]/span/span[1])[replace_value]"
    act_xpath = ref_xpath.replace('replace_value', str(i))
    print(act_xpath)
    element = driver.find_element_by_xpath(act_xpath)
    print(element.text)
    continue
# to logout Gmail
driver.find_element_by_xpath("//span[@class='gb_Ea gbii']").click()
driver.find_element_by_xpath("//a[text()='Sign out']").click()
# to close browser
driver.close()
