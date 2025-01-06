from playwright_toolbox.undetected_browser.browser import setup_browser
from patchright.sync_api import expect
import time


def fingerprint_com():
    browser = setup_browser()

    page = browser.pages[0]
    page.goto("https://fingerprint.com/products/bot-detection/")

    # Wait for the bot detection result to appear
    expect(page.locator(".HeroSection-module--botSubTitle--2711e")).not_to_have_text(
        "Bot detection in progress...", timeout=30000
    )

    # Get the bot detection result text
    bot_result = page.locator(".HeroSection-module--botSubTitle--2711e").inner_text()

    # Get automation tool and search engine detection status
    automation_status = page.locator(
        ".HeroSection-module--card--bd7d2 >> nth=0 >> .HeroSection-module--detected--06b7d"
    ).inner_text()
    search_engine_status = page.locator(
        ".HeroSection-module--card--bd7d2 >> nth=1 >> .HeroSection-module--detected--06b7d"
    ).inner_text()

    # Close browser
    browser.close()

    print(f"Bot detection result: {bot_result}")
    print(f"Automation status: {automation_status}")
    print(f"Search engine status: {search_engine_status}")


if __name__ == "__main__":
    fingerprint_com()
