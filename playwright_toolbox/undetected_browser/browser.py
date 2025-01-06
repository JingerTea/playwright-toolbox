# patchright here!
from patchright.sync_api import sync_playwright

def setup_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch_persistent_context(
        user_data_dir="./user_data",
        channel="chrome",
        headless=False,
        no_viewport=True,
    )
    return browser