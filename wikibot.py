import wikipedia

def scrape(name="Microsoft", length=10):
    result = wikipedia.summary(name, sentences=length)
    return result


print(scrape("Wikipedia"))