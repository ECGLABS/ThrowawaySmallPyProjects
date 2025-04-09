from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure ChromeDriver
options = Options()
options.add_argument('--headless')  # Comment this out if you want to see the browser
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

print("Loading Mac.Bid...")
driver.get('https://www.mac.bid/ending-soon')

# Wait for auction cards to appear
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-grid-card'))
    )
    print("Auction items loaded successfully.")
except Exception as e:
    print("❌ Timed out waiting for auctions to load:", e)
    driver.quit()
    exit()

# Scroll once to load more if needed
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Find items
items = driver.find_elements(By.CLASS_NAME, 'product-grid-card')
print(f"✅ Found {len(items)} auction items.")

# Print some of them
for i, item in enumerate(items[:10]):
    try:
        title = item.find_element(By.CLASS_NAME, 'product-title').text
        price = item.find_element(By.CLASS_NAME, 'product-price').text
        time_left = item.find_element(By.CLASS_NAME, 'auction-countdown').text
        link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')

        print(f"\n#{i+1}")
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Time Left: {time_left}")
        print(f"Link: {'https://www.mac.bid' + link if link.startswith('/') else link}")
    except Exception as e:
        print("❌ Error reading item:", e)

driver.quit()
