from firecrawl import FirecrawlApp, JsonConfig, ScrapeOptions
from pydantic import BaseModel

class ExtractSchema(BaseModel):
    person_name: str
    grade: str
    is_boy: bool
    is_girl: bool

def load_scrape(url):
    app = FirecrawlApp()
    json_config = JsonConfig(schema=ExtractSchema)
    scrape_result = app.scrape_url(url=url,
                                    formats=["json"],
                                    json_options=json_config,
                                    only_main_content=False,
                                    timeout=120000,
                                    max_age=3600_000)
    return scrape_result

def load_crawl(url):
    app = FirecrawlApp()
    options = ScrapeOptions(formats=["markdown", "html"], onlyMainContent=False, timeout=120000, maxAge=3600_000)
    crawl_result = app.crawl_url(url=url,
                                    limit=10,
                                    scrape_options=options,
                                    crawl_entire_domain=True,
                                    allow_subdomains=True)
    return crawl_result

def load_search(search: str):
    app = FirecrawlApp()
    options = ScrapeOptions(formats=["markdown", "html"],
                            onlyMainContent=False,
                            timeout=120000,
                            maxAge=100_000_000)
    search_result = app.search(query=search,
                                    limit=3,
                                    scrape_options=options)
    return search_result
        

