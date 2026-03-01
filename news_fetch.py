import requests

# NOTE: storing API keys in code is insecure; consider using an environment
# variable instead. For example:
# import os
# API_KEY = os.getenv("NEWSAPI_KEY")
# and then set NEWSAPI_KEY in your system or virtual environment.

API_KEY = "6ad462549321421ab34e68ea3f9d23fd"  # provided by user

def fetch_news(query="technology", page_size=5):
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&sortBy=publishedAt&apiKey={API_KEY}"
    res = requests.get(url)
    try:
        response = res.json()
    except ValueError:
        print("news_fetch: failed to parse JSON", res.text[:500])
        return []

    if res.status_code != 200:
        print(f"news_fetch: HTTP {res.status_code}")
        print("Response:", response)
        return []

    articles = response.get("articles", [])
    return [{"title": a.get("title"), "description": a.get("description")} for a in articles]


if __name__ == "__main__":
    print("Querying NewsAPI for 'technology'...")
    result = fetch_news("technology", 1)
    print(f"Got {len(result)} articles")
    print(result)
    