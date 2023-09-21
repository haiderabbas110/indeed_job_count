from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Replace with the path to your ChromeDriver executable
# chrome_driver_path = './chromedriver-win64/chromedriver-win64/chromedriver.exe'
service = Service(executable_path='./chromedriver-win64/chromedriver-win64/chromedriver.exe')

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
# Open the Indeed applied jobs page
indeed_url = 'https://myjobs.indeed.com/applied'
driver.get(indeed_url)

# Wait for the page to load (you might need to adjust the time if necessary)
driver.implicitly_wait(10)

# Find job entries using XPath
job_entries = driver.find_elements(By.XPATH, "//div[contains(@class, 'application-card')]")

# Count the number of job entries
num_jobs = len(job_entries)
print(f"Number of applied job entries: {num_jobs}")

# Close the browser
# driver.quit()