import asyncio
import os
from collections.abc import Coroutine

from aiohttp import ClientSession, ClientTimeout


BASE_DIR = "source"
HEADERS = {
    "cookie": (
        f"LEETCODE_SESSION={os.getenv('LEETCODE_SESSION')}; "
        f"csrftoken={os.getenv('LEETCODE_CSRF_TOKEN')}"
    ),
    "referer": "https://leetcode.com/",
}


async def fetch_problem_description(session: ClientSession, slug: str) -> str:
    slug = (
        slug.replace("_", "-")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace("'", "")
    )
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
    timeout = ClientTimeout(total=10)

    async with session.post(
        url, json=data, headers=HEADERS, timeout=timeout
    ) as response:
        response_json = await response.json()
        return response_json["data"]["question"]["content"]


async def create_readme_and_init() -> None:
    async with ClientSession() as session:
        tasks: list[Coroutine] = []

        for problem_slug in os.listdir(BASE_DIR):
            problem_dir = os.path.join(BASE_DIR, problem_slug)
            readme_path = os.path.join(problem_dir, "README.md")
            init_path = os.path.join(problem_dir, "__init__.py")
            tasks.append(fetch_problem_description(session, problem_slug))

            if not os.path.exists(init_path):
                with open(init_path, "w", encoding="utf-8") as file:
                    pass

        descriptions = await asyncio.gather(*tasks)
        for problem_slug, description in zip(
            os.listdir(BASE_DIR), descriptions
        ):
            problem_dir = os.path.join(BASE_DIR, problem_slug)
            readme_path = os.path.join(problem_dir, "README.md")

            with open(readme_path, "w", encoding="utf-8") as file:
                file.write(description)


if __name__ == "__main__":
    asyncio.run(create_readme_and_init())
