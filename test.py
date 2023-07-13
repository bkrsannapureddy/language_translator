import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()  # Replace with the actual path to the ChromeDriver executable

# Test Case 1: Selecting English as the Source Language and Entering Text
def test_select_source_language_and_enter_text():
    driver.get("file:///E:/project/index.html")  # Replace with the actual file path

    # Wait for the source language select element to be present
    time.sleep(2)  # Wait for 2 seconds (adjust as needed)

    source_language_select = driver.find_element(By.CSS_SELECTOR, ".controls .row.from select")
    source_text_area = driver.find_element(By.CSS_SELECTOR, ".text-input .from-text")

    # Select English as the source language
    source_language_code = "en"  # Replace with the desired source language code, for example, "en-GB" for English
    source_language_select.click()  # Open the select dropdown

    time.sleep(2)  # Wait for 1 second (adjust as needed)

    source_language_option = driver.find_element(By.CSS_SELECTOR, f".controls .row.from select option[value='{source_language_code}']")
    source_language_option.click()
    time.sleep(2)
    # Verify the selected language by checking the selected option's value
    selected_option = source_language_select.find_element(By.CSS_SELECTOR, "option:checked")
    assert selected_option.get_attribute("value") == source_language_code
    time.sleep(2)
    # Enter text in the source text area
    text_to_translate = "Hello, how are you?"  # Replace with the desired text to translate
    source_text_area.clear()
    source_text_area.send_keys(text_to_translate)

    # Additional test steps for Test Case 1
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)

    target_language_select = driver.find_element(By.CSS_SELECTOR, ".controls .row.to select")
    translate_btn = driver.find_element(By.CSS_SELECTOR, "button")

    # Select Spanish as the target language
    target_language_code = "es"  # Replace with the desired target language code, for example, "es-ES" for Spanish
    target_language_select.click()  # Open the select dropdown

    time.sleep(2)  # Wait for 1 second (adjust as needed)

    target_language_option = driver.find_element(By.CSS_SELECTOR, f".controls .row.to select option[value='{target_language_code}']")
    target_language_option.click()
    time.sleep(2)  
    # Verify the selected language by checking the selected option's value
    selected_option = target_language_select.find_element(By.CSS_SELECTOR, "option:checked")
    assert selected_option.get_attribute("value") == target_language_code

    # Click the translate button
    translate_btn.click()

    # Additional test steps for Test Case 2
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)


    from_audio_icon = driver.find_element(By.CSS_SELECTOR, ".controls .row.from .icons i:first-child")
     
    to_audio_icon = driver.find_element(By.CSS_SELECTOR, ".controls .row.to .icons i:first-child")
    
    copy_icons = driver.find_elements(By.CSS_SELECTOR, ".controls .row i.fa-copy")

    # Click the audio icons to trigger the Chrome permissions dialog
    from_audio_icon.click()
    time.sleep(5) 
    to_audio_icon.click()

    # Wait for the Chrome permissions dialog to appear
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)

    # Click the copy icons
    for copy_icon in copy_icons:
        copy_icon.click()

    # Additional test steps for Test Case 3
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)

# Run all the test cases
test_select_source_language_and_enter_text()

# Close the WebDriver
driver.quit()
