import logging
import requests
from http.client import HTTPException
from requests.exceptions import SSLError
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
from app_config import HN_BASE_URL, TITLE_KEY, COMMENTS_IDS_KEY, COMMENT_CONTENT_KEY, ID_KEY, logger

# As all requests are made to the same host, using session improves performance
session = requests.Session()


def get_top_stories(num_of_stories):
    top_stories_ids = _get_stories_ids_()
    if top_stories_ids is None:
        return None

    if num_of_stories is not None:
        top_stories_ids = top_stories_ids[:num_of_stories]

    top_stories = []
    # process multiple requests concurrently
    with FuturesSession() as future_session:
        futures = [future_session.get(f"{HN_BASE_URL}item/{story_id}.json") for story_id in top_stories_ids]
        for future in as_completed(futures):
            response = future.result()
            top_stories.append(response.json())

    # as stories aren't ordered due to concurrent fetching, sort them by the ids order in the original HN response
    top_stories.sort(key=lambda story: top_stories_ids.index(story[ID_KEY]))

    return top_stories


def print_stories(stories):
    for i, story in enumerate(stories):
        print(f"{i + 1}. {story.get(TITLE_KEY)}")


def print_comments(story):
    _print_comments_helper_(story, -1)


def _get_stories_ids_():
    url = f"{HN_BASE_URL}topstories.json"
    try:
        return session.get(url).json()
    except Exception as e:
        logger.error(e)
        return None


def _get_story_(story_id):
    url = f"{HN_BASE_URL}item/{story_id}.json"
    try:
        return session.get(url).json()
    except Exception as e:
        logger.error(e)
        return None


def _print_comments_helper_(story, indentation_level):
    # recursively traverse the comments- first print a comment and all its sub-comments,
    # then move to next comment in line
    if story is not None:
        text = story.get(COMMENT_CONTENT_KEY)
        if text is not None:
            print('\t' * indentation_level, '•', text)

        comments_ids = story.get(COMMENTS_IDS_KEY)
        if comments_ids is not None:
            for comment_id in comments_ids:
                _print_comments_helper_(_get_story_(comment_id), indentation_level + 1)

    return
