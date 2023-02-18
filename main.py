import requests
import json
from pprint import pprint
SECRET_KEY = "secret_WjYOjOKpFQRFD4idYSHMJFOpYyDB7vEbAIu94whOkcy"


def func():
    NOTION_API_KEY = SECRET_KEY

    # Define the Notion database ID and page properties
    database_id = "208f8545f2874fe5b8465f968e445fba"
    page_properties = {
        "Name": {"title": "hello world"},
        "Tasks": {"text": "fuck off"}
    }

    # Create the Notion page
    notion_url = f"https://www.notion.so/hub-4b22f08bcdb34d9684f0c8daac18fc8d?pvs=4"
    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NOTION_API_KEY}"
    }
    print("made it here 1")
    data = {
        "parent": {"database_id": database_id},
        "properties": page_properties
    }
    print("made it here 2")
    response = requests.post(
        notion_url, headers=headers, data=json.dumps(data))
    print(response.json())


def main():
    func()


main()
