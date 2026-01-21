import asyncio
from playwright.async_api import async_playwright

async def get_cricket_updates():
    # 1. Start Playwright using 'async with'
    async with async_playwright() as p:
        # 2. Launch browser with 'await'
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("Navigating to Google...")
        await page.goto("https://www.google.com")

        # 3. Handle search query
        search_bar = page.get_by_role("combobox")
        await search_bar.fill("Donald Trump updates")
        await search_bar.press("Enter")

        # 4. Wait for results
        await page.wait_for_load_state("networkidle")
        
        # Get headlines
        headlines = await page.locator("h3").all()
        print(f"\nFound {len(headlines)} headlines:")
        for i, headline in enumerate(headlines[:5]):
            print(f"{i+1}: {await headline.inner_text()}")

        await browser.close()

# 5. Correct way to run an async function in Python
if __name__ == "__main__":
    asyncio.run(get_cricket_updates())