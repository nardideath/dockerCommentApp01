import requests
import os


def fetch_comments():
    comments_url = os.getenv("COMMENTS_URL")
    print(f"Fetching data from remote API... ({comments_url})")

    response = requests.get()
    response.raise_for_status()

    data = response.json()

    print(f"Fetched {len(data)} comments.")
    return data



def group_by_post_id(comments):
    print("Grouping data by postId...")

    result = {}

    for c in comments:
        post_id = c["postId"]

        if post_id in result:
            result[post_id] += 1
        else:
            result[post_id] = 1

    return result



def save_results(data):
    result_file = os.getenv("RESULT_FILE")
    print(f"Saving results to file... ({result_file})")

    os.makedirs("/storage", exist_ok=True)

    with open(result_file, "w") as f:
        f.write("Comments grouped by postId\n")
        f.write("---------------------------\n")

        for post_id in sorted(data.keys()):
            f.write(f"postId {post_id}: {data[post_id]} comments\n")

    print("File saved.")