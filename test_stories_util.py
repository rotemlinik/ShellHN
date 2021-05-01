import pytest
from unittest.mock import patch
from app_config import TEST_OUTPUT_SIZE, ID_KEY
from stories_util import _get_stories_ids_, get_top_stories, _get_story_


class TestStoriesUtil:
    # normal cases tests
    def test_get_stories(self):
        # test size of output
        stories = get_top_stories(TEST_OUTPUT_SIZE)
        assert len(stories) == TEST_OUTPUT_SIZE

        # test order of output
        stories_ids = _get_stories_ids_()[:TEST_OUTPUT_SIZE]
        ids = []
        for story in stories:
            ids.append(story[ID_KEY])
        assert ids == stories_ids

    def test_get_story(self):
        story_id = self.get_single_key()
        story = _get_story_(story_id)
        assert story_id == story[ID_KEY]

    # exception cases tests
    def test_get_story_exception(self):
        with patch('stories_util.session.get', side_effect=Exception()):
            with pytest.raises(Exception):
                story = _get_story_(self.get_single_key())
                assert story is None

    def test_get_stories_ids_exception(self):
        with patch('stories_util.session.get', side_effect=Exception()):
            with pytest.raises(Exception):
                ids = _get_stories_ids_()
                assert ids is None

    @staticmethod
    def get_single_key():
        return _get_stories_ids_()[:1][0]
