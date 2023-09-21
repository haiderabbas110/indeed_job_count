from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from collections import defaultdict
from datetime import datetime
import time

# Set the path to your Chrome WebDriver executable
# chrome_driver_path = Service(executable_path='./chromedriver_win32/chromedriver.exe')

# Initialize the Chrome browser
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

service = Service(
    executable_path='./chromedriver-win64/chromedriver-win64/chromedriver.exe')

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# Open the Indeed applied jobs page
# driver.get('https://myjobs.indeed.com/applied')
driver.get('file:///E:/indeed/indeed.html')

# Wait for user to log in manually if required
input('Press Enter after logging in and navigating to the applied jobs page...')


# application_entries = driver.find_elements(By.CLASS_NAME, "application")
application_entries = driver.find_elements(
    By.XPATH, "//div[contains(@class, 'atw-AppCard-mainContainer')]")


# Create a dictionary to store the total jobs applied per day
jobs_per_day = defaultdict(int)
# date_element = driver.find_elements("xpath", "//div[contains(@class, 'esbq1260')]")
div_elements = driver.find_elements(
    By.XPATH, "//span[contains(@class, 'atw-AppCardJobInfo-userJobStatus')]")

job_count = len(application_entries)
text_counts = {}

# print(application_entries)
for div_element in div_elements:
    text = div_element.text
    if text in text_counts:
        text_counts[text] += 1
    else:
        text_counts[text] = 1

# print(div_element.text, " in ", count)
for text, count in text_counts.items():
    print(f"{text} ({count})")

print("Total", job_count, "applied")
# num_jobs_element = entry.find_element(By.XPATH, "application-count")

# date_str = date_element.text
# num_jobs = len(application_entries)
# num_jobs = int(num_jobs_element.text.strip())

# date = datetime.strptime(date_str, "%Y-%m-%d").date()
# jobs_per_day[date] += num_jobs

# Find the elements containing job entries
# job_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'atw-AppCard-mainContainer')]")

# # Count the number of job entries
# job_count = len(job_elements)
# print(f"Total Jobs Applied: {job_count}")

# # Calculate the total using a simple example
# total = job_count * 5 # Assuming $5 per job
# print(f"Total Amount Earned: ${total}")


# Print the resultsa
# print("Date\t\tTotal Jobs Applied")
# print("-" * 30)
# for date, total_jobs in sorted(jobs_per_day.items()):
#     print(f"{date}\t{total_jobs}")

# Close the browser
driver.quit()
