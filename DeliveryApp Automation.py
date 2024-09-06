import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up desired capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RMX3834"
options.app_package = "com.bykea.pk"
options.app_activity = ".screens.activities.SplashActivity"
options.no_reset = True

# Initialize the driver
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=options
)

# Set global implicit wait time
driver.implicitly_wait(20)  # Global implicit wait of 20 seconds

def click_menu_button():
    wait = WebDriverWait(driver, 20)
    menu_button = wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='BYKEA']")
    ))
    menu_button.click()

def click_home_button():
    home_button = driver.find_element(AppiumBy.XPATH,
                                      '//android.widget.TextView[@resource-id="com.bykea.pk:id/tvNavTitle" and @text="Home"]')
    home_button.click()

def type_text_in_one_go(element, text):
    """
    Types text into an element all at once.
    """
    element.clear()  # Clear the field first
    element.send_keys(text)  # Type the entire text all at once
    time.sleep(1)  # Wait to ensure the text is fully entered

try:
    click_menu_button()

    profile_text_view = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Profile']")
    profile_text_view.click()

    right_iv_button = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.bykea.pk:id/rightIv']")
    right_iv_button.click()

    edit_text_element = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.bykea.pk:id/tvName']")
    edit_text_element.clear()
    edit_text_element.send_keys("Abyeskhan")

    save_button = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.bykea.pk:id/rightIv']")
    save_button.click()

    click_menu_button()
    click_home_button()

    carpool = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                  'new UiSelector().resourceId("com.bykea.pk:id/rlServiceIcon").instance(0)')
    carpool.click()

    one_way = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.bykea.pk:id/tvOneWay"]')

    clock = driver.find_element(AppiumBy.XPATH,
                                '//android.widget.TextView[@resource-id="com.bykea.pk:id/tvPickUpTime"]')
    clock.click()

    time_three = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("3")')
    time_three.click()

    ok_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
    ok_button.click()

    pick_up_location_button = driver.find_element(AppiumBy.XPATH,
                                                  '//android.widget.TextView[@resource-id="com.bykea.pk:id/tvPickUpLocation"]')
    pick_up_location_button.click()

    auto_complete_text_view = driver.find_element(AppiumBy.XPATH,
                                                  '//android.widget.AutoCompleteTextView[@resource-id="com.bykea.pk:id/autocomplete_places"]')

    # Type the entire text "Gulshan" at once
    type_text_in_one_go(auto_complete_text_view, 'Gulshan')

    # Additional action to prompt the dropdown display
    auto_complete_text_view.click()  # Simulate click to force dropdown to appear
    time.sleep(1)  # Wait for the dropdown to appear

    # Explicit wait for the dropdown items to be present
    wait = WebDriverWait(driver, 10)
    dropdown_items = wait.until(
        EC.presence_of_all_elements_located(
            (AppiumBy.XPATH,
             "//androidx.viewpager.widget.ViewPager[@resource-id='com.bykea.pk:id/vpFragments']/android.widget.LinearLayout/android.widget.RelativeLayout")
        )
    )

    # Click the first item in the dropdown
    if dropdown_items:
        first_item = dropdown_items[0]
        first_item.click()
    else:
        print("No items found in the dropdown.")
    driver.find_element(AppiumBy.XPATH,
                        "//android.widget.FrameLayout[@resource-id='com.bykea.pk:id/confirmBtn']").click()
    edit_text_element = driver.find_element(AppiumBy.XPATH,
                                            "//android.widget.EditText[@resource-id='com.bykea.pk:id/etEditedName']")
    edit_text_element.click()
    edit_text_element.send_keys("abyes")
    driver.hide_keyboard()
    confirm_button = driver.find_element(AppiumBy.ID, "com.bykea.pk:id/confirmBtn")
    confirm_button.click()
    drop_off_location_button = driver.find_element(AppiumBy.XPATH,
                                                   '//android.widget.TextView[@resource-id="com.bykea.pk:id/tvDropOffLocation"]')
    drop_off_location_button.click()
    search_icon = driver.find_element(AppiumBy.XPATH,
                                      '//android.widget.LinearLayout[@resource-id="com.bykea.pk:id/llSearch"]')
    search_icon.click()
    # Click on the search field to force the dropdown to appear
    search_field = driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.AutoCompleteTextView[@resource-id="com.bykea.pk:id/autocomplete_places"]')
    search_field.click()

    # Type "North" into the search field
    search_field.send_keys("North")

    # Simulate another click to ensure the dropdown appears
    search_field.click()
    time.sleep(1)  # Wait for the dropdown to appear

    # Wait for the dropdown to be present and visible
    wait = WebDriverWait(driver, 10)
    dropdown_items = wait.until(
        EC.presence_of_all_elements_located(
            (AppiumBy.XPATH,
             '//androidx.viewpager.widget.ViewPager[@resource-id="com.bykea.pk:id/vpFragments"]/android.widget.LinearLayout/android.widget.RelativeLayout')
        )
    )

    # Click on the first value from the dropdown
    if dropdown_items:
        dropdown_items[0].click()
    else:
        print("No dropdown items found")
    # Click on the confirm button
    confirm_button = driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.FrameLayout[@resource-id="com.bykea.pk:id/confirmBtn"]')
    confirm_button.click()
    # Click on the EditText field
    edit_text_field = driver.find_element(AppiumBy.XPATH,
                                          '//android.widget.EditText[@resource-id="com.bykea.pk:id/etEditedName"]')
    edit_text_field.click()

    # Send keys to the field
    edit_text_field.send_keys('khan/')

    # Hide the keyboard
    driver.hide_keyboard()
    # Click on the confirm button
    confirm_button = driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.ImageView[@resource-id="com.bykea.pk:id/confirmBtn"]')
    confirm_button.click()
    # Click on the button with the specified resource-id
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.bykea.pk:id/ivPlusMale"]').click()
    # Click on the button with the specified resource-id












except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'driver' in locals():
        driver.quit()
