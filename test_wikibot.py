from wikibot import scrape


def test_scrape():
    assert "Facebook" in scrape("Mircosoft")
