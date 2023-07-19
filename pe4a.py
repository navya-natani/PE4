import wikipedia
import time


def extract_content(topic_new):
    try:
        page = wikipedia.page(topic_new, auto_suggest=False)
        file_name = f"{page.title}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(page.content)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError: {e}")


start_time = time.time()

search_results = wikipedia.search("generative artificial intelligence")

for topic in search_results:
    extract_content(topic)

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")
