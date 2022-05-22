from serpapi import GoogleSearch

params = {
  "api_key": "YOUR_API_KEY",
  "engine": "google",
  "q": "gta san andreas",
  "gl": "us",
  "tbm": "nws"
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results['news_results']:
    print(result)
