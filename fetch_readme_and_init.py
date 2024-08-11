import os

import requests


BASE_DIR = "source"
HEADERS = {
    "cookie": (
        f"LEETCODE_SESSION={os.getenv('LEETCODE_SESSION')}; "
        f"csrftoken={os.getenv('LEETCODE_CSRF_TOKEN')}"
    ),
    "referer": "https://leetcode.com/",
    "x-csrftoken": os.getenv("LEETCODE_CSRF_TOKEN"),
}


def fetch_problem_description(slug: str) -> str:
    slug = slug.replace("_", "-")
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content
        }
    }
    """
    variables = {"titleSlug": slug}
    data = {"query": query, "variables": variables}
    response = requests.post(url, json=data, headers=HEADERS, timeout=10)
    return response.json()["data"]["question"]["content"]


def create_readme_and_init() -> None:
    for problem_slug in os.listdir(BASE_DIR):
        problem_dir = os.path.join(BASE_DIR, problem_slug)

        readme_path = os.path.join(problem_dir, "README.md")
        description = fetch_problem_description(problem_slug)
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(description)

        init_path = os.path.join(problem_dir, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w", encoding="utf-8") as file:
                pass


if __name__ == "__main__":
    create_readme_and_init()
