import wikipedia
import concurrent.futures
import time

def download_wiki_page(topic):
    page = wikipedia.page(topic)
    file_name = f"{topic}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(page.content)

start_time = time.time()

search_results = wikipedia.search("generative artificial intelligence")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_wiki_page, search_results)

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

