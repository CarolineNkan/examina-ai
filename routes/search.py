from duckduckgo_search import DDGS

def expand_context(user_notes):
    """Uses DuckDuckGo search to add context without needing an API key."""

    query = f"explain this topic for students: {user_notes}"

    # Perform the search
    results = DDGS().text(query, max_results=5)

    # Extract the text snippets
    snippets = [r.get("body", "") for r in results]

    # Return combined context
    return "\n".join(snippets[:3])
