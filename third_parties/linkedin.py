import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LinkedIn:

    @staticmethod
    def scrap_linkedin_profile(linked_profile_url: str, mock: bool = False):
        """
        scrape information of LinkedIn profile.
        :param linked_profile_url: Url of a profile
        :param mock: used for local development
        :return:
        """
        if mock:
            linked_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
            response = requests.get(linked_profile_url, timeout=10)
        else:
            api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
            headers = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
            response = requests.get(
                api_endpoint,
                params={"url": linked_profile_url},
                headers=headers,
                timeout=10,
            )

        response = response.json()
        data = {
            k: v
            for k, v in response.items()
            if v not in ([], "", " ", None) and k not in ["people_also_viewed", "certifications"]
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")
        return data
