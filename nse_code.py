import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# def scrape_pdf_links(report_link):
#     pdf_links = []
#     options = Options()
#     options.headless = True  # Run in headless mode
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     try:
#         driver.get(report_link)

#         # Wait for the page to load
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.TAG_NAME, "body"))
#         )

#         # Click on the "Annual Reports" tab using JavaScript to ensure it works
#         try:
#             print("inside scrape try before annual report tab")
#             annual_reports_tab = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.ID, "annualReports"))
#             )
#             driver.execute_script("arguments[0].scrollIntoView(true);", annual_reports_tab)
#             time.sleep(1)
#             print("inside the try after annual reports")
#             driver.execute_script("arguments[0].click();", annual_reports_tab)  # Using JavaScript to click
#             print("after the execute")
#             # Wait for the data to load after clicking
#             time.sleep(15)  # Adjust this value if needed to allow data to load
            
#             # Wait for the annual reports section to be visible
#             WebDriverWait(driver, 10).until(
#                 EC.visibility_of_element_located((By.ID, "annualReports"))  # Ensure this ID matches the actual section ID
#             )

#         except Exception as e:
#             print(f"Error clicking on Annual Reports tab: {e}")

#         # Scroll down in increments to load more content
#         last_height = driver.execute_script("return document.body.scrollHeight")
#         scroll_increment = last_height // 10

#         while True:
#             # Scroll down
#             driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
#             time.sleep(1)

#             # Check for PDF links
#             pdf_elements = driver.find_elements(By.XPATH, "//td[@class='text-center']//a[contains(@href, '.pdf')]")
#             if pdf_elements:
#                 for element in pdf_elements:
#                     pdf_link = element.get_attribute('href')
#                     if pdf_link and pdf_link not in pdf_links:
#                         pdf_links.append(pdf_link)

#             # Check if the height of the page has changed
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:  # No new content
#                 break
#             last_height = new_height

#     except Exception as e:
#         print(f"Error scraping {report_link}: {e}")

#     finally:
#         driver.quit()
    
#     return pdf_links

# scrape_pdf_links("https://www.nseindia.com/get-quotes/equity?symbol=LAWSIKHO")



# # Path to your CSV file containing report links
# csv_file_path = "/home/shubh/project/nse_links1.csv"
# output_pdf_links_file_path = "/home/shubh/project/nse_pdfs.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Check if the output file exists and if it’s empty to write header
# file_exists = os.path.exists(output_pdf_links_file_path)

# with open(output_pdf_links_file_path, 'a') as output_file:
#     # Write the header only if the file is empty or does not exist
#     if not file_exists or os.stat(output_pdf_links_file_path).st_size == 0:
#         output_file.write("pdf_link\n")
    
#     # Check if the 'report link' column exists
#     if 'report link' in df.columns:
#         # Loop through each report link and scrape PDF links
#         for index, row in df.iterrows():
#             report_link = row['report link']

#             # Scrape PDF links
#             pdf_links = scrape_pdf_links(report_link)
            
#             # Check if any PDF links were found for this report link
#             if pdf_links:
#                 # Append PDF links to CSV file
#                 for pdf_link in pdf_links:
#                     output_file.write(f"{pdf_link}\n")
#                 print(f"PDF links for {report_link} saved to {output_pdf_links_file_path}")

#     else:
#         print("The CSV file must contain a 'report link' column.")

pdf_links = []
options = Options()
options.headless = True  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print(1)
driver.get("https://www.bseindia.com/stock-share-price/tata-elxsi-ltd/tataelxsi/500408/financials-annual-reports/")

# time.sleep(15)
# WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.TAG_NAME, "body"))
# )