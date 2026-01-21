import asyncio
from playwright.async_api import async_playwright

async def playwright_function():
    # Use async_playwright as a context manager
    async with async_playwright() as AP:
        # Launch the browser (added .launch())
        browser = await AP.chromium.launch(headless=False)
        
        # Create a new page
        page = await browser.new_page()

        # Navigation
        print("Navigating...")
        await page.goto("https://www.google.com")
        
        # Corrected method name: wait_for_timeout
        await page.wait_for_timeout(3000) 
        
        await browser.close()
        print("Browser closed successfully.")

# Main entry point
if __name__ == "__main__":
    asyncio.run(playwright_function())