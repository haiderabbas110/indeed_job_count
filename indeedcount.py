from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from collections import defaultdict
from datetime import datetime
import time

try:
    service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")  # Set the log level to suppress warnings and errors
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('file:///C:/xampp/htdocs/indeed_job_count/downloaded-jobs/My jobs _ Indeed.html')
    #driver.get('https://myjobs.indeed.com/applied')

except Exception as e:
    print(e)

# Initialize earliest_date as a future date
earliest_date = datetime.now()

while True:
    get_date = input('Please Enter Date ')

    application_entries = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'atw-AppCard-mainContainer')]")

    jobs_per_day = defaultdict(int)

    div_elements = driver.find_elements(
        By.XPATH, "//span[contains(@class, 'atw-AppCardJobInfo-userJobStatus')]")

    job_count = len(application_entries)
    text_counts = {}
    total_jobs = 0
    date_found = False

    for div_element in div_elements:
        text = div_element.text

        if text in text_counts:
            text_counts[text] += 1
        else:
            text_counts[text] = 1

        if get_date in text:
            date_found = True
            break
        else:
            # Extract date from the text, assuming it's in 'MM/DD/YYYY' format
            try:
                job_date = datetime.strptime(text, '%m/%d/%Y')
                if job_date < earliest_date:
                    earliest_date = job_date
            except ValueError:
                pass

    if date_found:
        for text, count in text_counts.items():
            total_jobs += count
            print(f"{text} ({count})")

        print(f"Total {total_jobs} applied")
    else:
        print(f"No new jobs have been applied to since'{get_date}'")

        # If no jobs are found for the provided date, search for jobs on or after the earliest date
        if earliest_date < datetime.now():
            # print(f"Searching for jobs since {earliest_date.strftime('%m/%d/%Y')}")
            get_date = earliest_date.strftime('%m/%d/%Y')

    # Ask the user if they want to search for another date
    repeat_search = input('Do you want to search for another date? (yes/no): ')
    if repeat_search.lower() != 'yes':
        break  # Exit the loop if the user doesn't want to search again

# Close the browser after all date searches are done
driver.quit()

# Add a while loop to keep the script running
while True:
    pass  # This will keep the script running until manually stopped
