from langchain_community.tools.tavily_search import TavilySearchResults


class TavilyTools:
    @staticmethod
    def get_profile_url_tavily(name: str):
        """searches for linkedin url"""
        search = TavilySearchResults()
        res = search.run(f"{name}")
        return res[0]["url"]
