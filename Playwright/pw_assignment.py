import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)  # set True for headless mode
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # Navigate directly to gold rate site
            await page.goto("https://24kgoldrate.com/?city=chennai")

            # Wait for the gold rate table to appear
            await page.wait_for_selector("table", timeout=7000)

            # Extract 24K and 22K gold rates using CSS selectors
            rate_24k = await page.text_content("table tr:nth-child(2) td:nth-child(2)")
            rate_22k = await page.text_content("table tr:nth-child(3) td:nth-child(2)")

            # Screenshot of the page
            await page.screenshot(path="goldrate.png", full_page=True)

            # Export data to text file
            output = f"Gold Rate Today in Chennai:\n\n24K: {rate_24k}\n22K: {rate_22k}"
            with open("goldrate.txt", "w", encoding="utf-8") as f:
                f.write(output)

            print("✅ Data extracted and saved to goldrate.txt")

        except Exception as e:
            print("⚠️ Error occurred:", e)

        finally:
            await browser.close()

# Run the async function
asyncio.run(run())