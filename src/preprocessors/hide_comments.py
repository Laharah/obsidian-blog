from src.dataclasses.content_data import ContentData
import regex as re

COMMENT_REGEX = re.compile(r"%%.*?%%(\r?\n)?", re.DOTALL)


class HideCommentsPreprocessor:
    comment_regex = COMMENT_REGEX

    @classmethod
    def process_page(cls, page):
        cls.process_entity(page)

    @classmethod
    def process_entity(cls, entity):
        data: ContentData = entity.data
        if not cls.is_supported_content(data):
            return
        re.sub
        prev = data.content
        data.content = cls.comment_regex.sub("", data.content)
        if prev != data.content:
            print(f'  - [PREPROCESS] removed comments in "{data.title}"')
        else:
            print(f'  - [PREPROCESS] no comments to remove for "{data.title}"')

    @classmethod
    def is_supported_content(cls, data: ContentData):
        if not isinstance(data, ContentData):
            return False
        if data.content == "":
            return False
        return True
