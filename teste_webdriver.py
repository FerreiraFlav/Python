from selenium import webdriver

# fazendo instalação do ChromeDriver na variavel service
driver  = webdriver.Chrome(service=driver)
driver.get('https://www.google.com')
driver.quit()
