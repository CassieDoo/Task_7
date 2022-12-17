import requests
from pprint import pprint


class YaUploader:
    files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self, token: str):
        self.token = token

    @property
    def headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_upload_link(self, file_path: str) -> dict:
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(self.upload_url, params=params, headers=self.headers)
        if response.status_code == 200:
            print(f"Получена ссылка на загрузку файла: {response.json()['href']}")
            return response.json()
        print("Ссылка на загрузку файла не выдана, потому что", response.status_code)
        return False


    def upload(self, file_path: str):
        href = self.get_upload_link(file_path).get("href")
        if not href:
            return

        with open(file_path, "rb") as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print("Файл загружен")
                return True
            print("Файл не загружен, потому что", response.status_code)
            return False


def get_token():
    with open("token.txt", "r") as file:
        return file.readline()


ya_client = YaUploader(get_token())
ya_client.upload("file1.txt")
