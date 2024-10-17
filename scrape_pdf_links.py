# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# def scrape_pdf_links(report_link):
#     """
#     Scrape PDF links from the given report link.

#     Args:
#         report_link (str): The URL of the report page.

#     Returns:
#         list: A list of PDF links found on the page.
#     """
#     try:
#         # Send a GET request to the report link
#         response = requests.get(report_link)
#         response.raise_for_status()  # Raise an error for bad responses

#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')
#         print(soup)
#         # Find all <a> tags with the PDF links
#         pdf_links = []
#         for a_tag in soup.find_all('a', href=True):
#             if a_tag['href'].endswith('.pdf'):
#                 pdf_links.append(a_tag['href'])

#         return pdf_links
#     except Exception as e:
#         print(f"Error scraping {report_link}: {e}")
#         return []

# # Path to your CSV file containing report links
# csv_file_path = "/home/shubh/project/companies_links.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Check if the 'report link' column exists
# if 'report link' in df.columns:
#     all_pdf_links = []
    
#     # Loop through each report link and scrape PDF links
#     for index, row in df.iterrows():
#         report_link = row['report link']
#         # print(f"Scraping PDF links from: {report_link}")
#         pdf_links = scrape_pdf_links(report_link)
        
#         # Store the scraped links with the corresponding report link
#         for pdf_link in pdf_links:
#             all_pdf_links.append({'report_link': report_link, 'pdf_link': pdf_link})

#     # Create a DataFrame from the scraped PDF links
#     pdf_links_df = pd.DataFrame(all_pdf_links)

#     # Save the scraped PDF links to a new CSV file
#     output_pdf_links_file_path = "/home/shubh/project/annual_report.csv"
#     pdf_links_df.to_csv(output_pdf_links_file_path, index=False)

#     print(f"Scraped PDF links saved to {output_pdf_links_file_path}")
# else:
#     print("The CSV file must contain a 'report link' column.")
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# def scrape_pdf_links(report_link):
#     """
#     Scrape PDF links from the given report link.

#     Args:
#         report_link (str): The URL of the report page.

#     Returns:
#         list: A list of PDF links found on the page.
#     """
#     try:
#         # Set the user-agent to mimic a real browser
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
#         }
        
#         # Send a GET request to the report link with headers
#         response = requests.get(report_link, headers=headers)
#         response.raise_for_status()  # Raise an error for bad responses

#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find all <td> tags with class 'tdcolumn' containing <a> tags for PDF links
#         pdf_links = []
        
#         # Debugging: Print the HTML content to see what's being returned
#         print(f"Scraping URL: {report_link}")
#         print("HTML Content:", soup.prettify()[:1000])  # Print the first 1000 characters for inspection

#         # Find all <td> elements with the class 'tdcolumn'
#         for td in soup.find_all('td', class_='tdcolumn'):
#             a_tag = td.find('a', href=True)
#             if a_tag and 'pdf' in a_tag['href']:
#                 pdf_links.append(a_tag['href'])

#         return pdf_links
#     except requests.exceptions.HTTPError as e:
#         # Handle specific HTTP errors
#         if response.status_code == 404:
#             print(f"404 Not Found for: {report_link}. Skipping this link.")
#         else:
#             print(f"HTTP Error {response.status_code} for: {report_link}.")
#         return []
#     except Exception as e:
#         print(f"Error scraping {report_link}: {e}")
#         return []

# # Path to your CSV file containing report links
# csv_file_path = "/home/shubh/project/companies_links.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Check if the 'report link' column exists
# if 'report link' in df.columns:
#     all_pdf_links = []
    
#     # Loop through each report link and scrape PDF links
#     for index, row in df.iterrows():
#         report_link = row['report link']
        
#         # Scrape PDF links
#         pdf_links = scrape_pdf_links(report_link)
#         print(pdf_links)
#         # Store the scraped links with the corresponding report link
#         for pdf_link in pdf_links:
#             all_pdf_links.append({'report_link': report_link, 'pdf_link': pdf_link})

#     # Create a DataFrame from the scraped PDF links
#     pdf_links_df = pd.DataFrame(all_pdf_links)

#     # Save the scraped PDF links to a new CSV file
#     output_pdf_links_file_path = "/home/shubh/project/scraped_pdf_links.csv"
#     pdf_links_df.to_csv(output_pdf_links_file_path, index=False)

#     print(f"Scraped PDF links saved to {output_pdf_links_file_path}")
# else:
#     print("The CSV file must contain a 'report link' column.")


# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# def scrape_pdf_links(report_link):
#     """
#     Scrape PDF links from the given report link using Selenium.

#     Args:
#         report_link (str): The URL of the report page.

#     Returns:
#         list: A list of PDF links found on the page.
#     """
#     pdf_links = []
#     options = Options()
#     options.headless = True  # Run in headless mode
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     try:
#         driver.get(report_link)
        
#         # Wait for the <td> elements with the class 'tdcolumn' to be visible
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_all_elements_located((By.CLASS_NAME, 'tdcolumn'))
#         )

#         # Scroll down to ensure all content is loaded
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         # Optionally wait for a moment to allow content to load after scrolling
#         time.sleep(2)

#         # Find all <td> elements with the class 'tdcolumn'
#         td_elements = driver.find_elements(By.CLASS_NAME, 'tdcolumn')

#         for td in td_elements:
#             try:
#                 a_tag = td.find_element(By.TAG_NAME, 'a')
#                 if a_tag and 'pdf' in a_tag.get_attribute('href'):
#                     pdf_links.append(a_tag.get_attribute('href'))
#             except Exception as inner_exception:
#                 print(f"Error finding <a> tag in <td>: {inner_exception}")

#     except Exception as e:
#         print(f"Error scraping {report_link}: {e}")
#         print("Page source for debugging:")
#         print(driver.page_source)  # Print the page source to help with debugging

#     finally:
#         driver.quit()
    
#     return pdf_links


# # Path to your CSV file containing report links
# csv_file_path = "/home/shubh/project/companies_links.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Check if the 'report link' column exists
# if 'report link' in df.columns:
#     all_pdf_links = []
    
#     # Loop through each report link and scrape PDF links
#     for index, row in df.iterrows():
#         report_link = row['report link']
        
#         # Scrape PDF links
#         pdf_links = scrape_pdf_links(report_link)

#         # Store the scraped links with the corresponding report link
#         for pdf_link in pdf_links:
#             all_pdf_links.append({'report_link': report_link, 'pdf_link': pdf_link})

#     # Create a DataFrame from the scraped PDF links
#     pdf_links_df = pd.DataFrame(all_pdf_links)

#     # Save the scraped PDF links to a new CSV file
#     output_pdf_links_file_path = "/home/shubh/project/scraped_pdf_links.csv"
#     pdf_links_df.to_csv(output_pdf_links_file_path, index=False)

#     print(f"Scraped PDF links saved to {output_pdf_links_file_path}")
# else:
#     print("The CSV file must contain a 'report link' column.")


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# def scrape_pdf_links(report_link):
#     pdf_links = []
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     try:
#         driver.get(report_link)
        
#         # Print page source for debugging
#         print(driver.page_source)
        
#         # Wait for up to 20 seconds for PDF links to become visible
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_all_elements_located((By.XPATH, "//td[@class='tdcolumn']//a[contains(@href, '.pdf')]"))
#         )

#         # Scroll down in increments to ensure all content loads
#         for i in range(3):  # Scroll 3 times, adjust as needed
#             driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
#             time.sleep(2)

#         # Find all PDF links
#         pdf_elements = driver.find_elements(By.XPATH, "//td[@class='tdcolumn']//a[contains(@href, '.pdf')]")
#         pdf_links = [elem.get_attribute('href') for elem in pdf_elements]
        
#     except Exception as e:
#         print(f"Error scraping {report_link}: {e}")

#     finally:
#         driver.quit()
    
#     return pdf_links


# # Path to your CSV file containing report links
# csv_file_path = "/home/shubh/project/annual_report.csv"
# output_pdf_links_file_path = "/home/shubh/project/scraped_pdf_links.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Create or open the CSV file where scraped PDF links will be saved
# with open(output_pdf_links_file_path, 'a') as output_file:
#     # Check if the 'report link' column exists
#     if 'report link' in df.columns:
#         # Loop through each report link and scrape PDF links
#         for index, row in df.iterrows():
#             report_link = row['report link']
#             company_name = row['Security Name']
#             company_code = row['Security Code']

            
#             # Scrape PDF links
#             pdf_links = scrape_pdf_links(report_link)
#             print('shyam')
#             print(pdf_links)
#             # Check if any PDF links were found for this report link
#             if pdf_links:
#                 # Store the scraped links with the corresponding report link
#                 pdf_links_df = pd.DataFrame([{'company_name': company_name, 'security_code': company_code, 'pdf_link': link} for link in pdf_links])

#                 # Append to CSV file immediately after each company is processed
#                 pdf_links_df.to_csv(output_pdf_links_file_path, mode='a', header=not output_file.tell(), index=False)
#                 print(f"PDF links for {report_link} saved to {output_pdf_links_file_path}")

#     else:
#         print("The CSV file must contain a 'report link' column.")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# import time

# def scrape_pdf_links(report_link):
#     pdf_data = []
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     try:
#         driver.get(report_link)
        
#         # Print page source for debugging
#         print(driver.page_source)
        
#         # Wait for up to 20 seconds for the rows with report data to be present
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@ng-repeat, 'report in annreportData.Table')]"))
#         )

#         # Scroll down in increments to ensure all content loads
#         for i in range(3):
#             driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
#             time.sleep(2)

#         # Find all report rows
#         rows = driver.find_elements(By.XPATH, "//tr[contains(@ng-repeat, 'report in annreportData.Table')]")
        
#         for row in rows:
#             try:
#                 # Extract the year from the first <td> element
#                 year = row.find_element(By.XPATH, ".//td[@class='tdcolumn ng-binding']").text
                
#                 # Look for the PDF link in the row
#                 a_tag = row.find_element(By.XPATH, ".//td[@class='tdcolumn']//a[contains(@href, '.pdf')]")
#                 pdf_link = a_tag.get_attribute('href')
                
#                 if year and pdf_link:
#                     pdf_data.append({'year': year, 'pdf_link': pdf_link})
            
#             except Exception as inner_exception:
#                 print(f"Error processing row: {inner_exception}")

#     except Exception as e:
#         print(f"Error scraping {report_link}: {e}")

#     finally:
#         driver.quit()
    
#     return pdf_data


# # Path to your CSV file containing report links
# csv_file_path = "/home/shubh/project/annual_report.csv"
# output_pdf_links_file_path = "/home/shubh/project/scraped_pdf_links.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Create or open the CSV file where scraped PDF links will be saved
# with open(output_pdf_links_file_path, 'a') as output_file:
#     # Check if the 'report link' column exists
#     if 'report link' in df.columns:
#         # Loop through each report link and scrape PDF links
#         for index, row in df.iterrows():
#             report_link = row['report link']
#             company_name = row['Security Name']
#             company_code = row['Security Code']

#             # Scrape PDF links and years
#             pdf_data = scrape_pdf_links(report_link)
            
#             # Check if any PDF links were found for this report link
#             if pdf_data:
#                 # Create a DataFrame from the scraped data
#                 pdf_data_df = pd.DataFrame([{
#                     'company_name': company_name,
#                     'security_code': company_code,
#                     'year': item['year'],
#                     'pdf_link': item['pdf_link']
#                 } for item in pdf_data])

#                 # Append to CSV file immediately after each company is processed
#                 pdf_data_df.to_csv(output_pdf_links_file_path, mode='a', header=not output_file.tell(), index=False)
#                 print(f"PDF links and years for {report_link} saved to {output_pdf_links_file_path}")

#     else:
#         print("The CSV file must contain a 'report link' column.")
import os

def scrape_pdf_links(report_link):
    pdf_data = []
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(report_link)
        
        # Print page source for debugging
        print(driver.page_source)
        
        # Wait for up to 20 seconds for the rows with report data to be present
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@ng-repeat, 'report in annreportData.Table')]"))
        )

        # Scroll down in increments to ensure all content loads
        for i in range(3):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
            time.sleep(2)

        # Find all report rows
        rows = driver.find_elements(By.XPATH, "//tr[contains(@ng-repeat, 'report in annreportData.Table')]")
        
        for row in rows:
            try:
                # Extract the year from the first <td> element
                year = row.find_element(By.XPATH, ".//td[@class='tdcolumn ng-binding']").text
                
                # Look for the PDF link in the row
                a_tag = row.find_element(By.XPATH, ".//td[@class='tdcolumn']//a[contains(@href, '.pdf')]")
                pdf_link = a_tag.get_attribute('href')
                
                if year and pdf_link:
                    pdf_data.append({'year': year, 'pdf_link': pdf_link})
            
            except Exception as inner_exception:
                print(f"Error processing row: {inner_exception}")

    except Exception as e:
        print(f"Error scraping {report_link}: {e}")

    finally:
        driver.quit()
    
    return pdf_data


# Path to your CSV file containing report links
csv_file_path = "/home/shubh/project/MarketWatch.csv"
output_pdf_links_file_path = "/home/shubh/project/scraped_pdf_links.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Check if the output file exists and if it’s empty to write header
file_exists = os.path.exists(output_pdf_links_file_path)

with open(output_pdf_links_file_path, 'a') as output_file:
    # Write the header only if the file is empty or does not exist
    if not file_exists or os.stat(output_pdf_links_file_path).st_size == 0:
        output_file.write("company_name,security_code,year,pdf_link\n")
    
    # Check if the 'report link' column exists
    if 'report link' in df.columns:
        # Loop through each report link and scrape PDF links
        for index, row in df.iterrows():
            report_link = row['report link']
            company_name = row['Security Name']
            company_code = row['bse_code']

            # Scrape PDF links and years
            pdf_data = scrape_pdf_links(report_link)
            
            # Check if any PDF links were found for this report link
            if pdf_data:
                # Create a DataFrame from the scraped data
                pdf_data_df = pd.DataFrame([{
                    'company_name': company_name,
                    'security_code': company_code,
                    'year': item['year'],
                    'pdf_link': item['pdf_link']
                } for item in pdf_data])

                # Append to CSV file immediately after each company is processed
                pdf_data_df.to_csv(output_pdf_links_file_path, mode='a', header=False, index=False)
                print(f"PDF links and years for {report_link} saved to {output_pdf_links_file_path}")

    else:
        print("The CSV file must contain a 'report link' column.")