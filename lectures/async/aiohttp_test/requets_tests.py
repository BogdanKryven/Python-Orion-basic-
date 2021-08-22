import requests
import time


def get_file(url):
    return requests.get(url, allow_redirects=True)


def write_file(response):
    file_name = response.url.split("/")[-1]
    with open(f"response_test/{file_name}", "wb") as file:
        file.write(response.content)


def main():
    url = "https://loremflickr.com/320/240"
    t0 = time.time()
    for i in range(20):
        response = get_file(url)
        print(response.status_code)
        # write_file(response)
    print(time.time() - t0)


if __name__ == '__main__':
    main()
