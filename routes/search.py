import requests

def expand_context(query):
    """
    Uses DuckDuckGo Instant Answer API for lightweight context.
    No API key needed.
    """
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_html": "1",
        "no_redirect": "1"
    }

    try:
        r = requests.get(url, params=params).json()

        abstract = r.get("AbstractText") or ""

        related = " ".join(
            topic.get("Text", "")
            for topic in r.get("RelatedTopics", [])
            if isinstance(topic, dict)
        )

        combined = f"{abstract}\n{related}".strip()
        return combined if combined else "No additional context found."
    except:
        return "No context found."

