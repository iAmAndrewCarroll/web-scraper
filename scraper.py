from playwright.sync_api import sync_playwright

def init_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    return browser

def citation_count(browser, url):
    page = browser.new_page()
    page.goto(url)
    citations_needed = page.query_selector_all('sup[class="nonprint Inline-Template Template-Fact"]')
    count = len(citations_needed)
    page.close()
    return count

def citation_report(browser, url):
    page = browser.new_page()
    page.goto(url)
    citations_needed = page.query_selector_all('sup[class="nonprint Inline-Template Template-Fact"]')

    report = ""
    for citation in citations_needed:
        passage = citation.inner_text()
        report += f"Citation needed for \"{passage}\"\n"

    page.close()
    return report

def main():
    url = "https://en.wikipedia.org/wiki/Timohty_Leary"
    browser = init_browser()
    citations_needed_count = citation_count(browser, url)
    print(f"Number of citations needed: {citations_needed_count}")
    citations_needed_report = citation_report(browser, url)
    print(citations_needed_report)
    browser.close()

if __name__ == "__main__":
    main()
