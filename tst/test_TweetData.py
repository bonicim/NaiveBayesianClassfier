import pytest
from os import path


@pytest.fixture
def tweet_data():
    from src.TweetData import TweetData

    return TweetData(
        path.abspath(
            path.join(path.dirname(__file__), "..", "data", "training_data_small.csv")
        )
    )


def test_process(tweet_data):
    expected = [
        (
            "HillaryClinton",
            {
                "question": 1,
                "election": 1,
                "put": 1,
                "plans": 1,
                "action": 1,
                "make": 1,
                "life": 1,
                "better": 1,
                "httpstcoxreey9oicg": 1,
                "nothing": 1,
            },
        ),
        (
            "realDonaldTrump",
            {
                "nothing": 3,
                "emails": 1,
                "corrupt": 1,
                "clinton": 1,
                "foundation": 1,
                "benghazi": 1,
                "debates2016": 1,
                "debatenight": 1,
            },
        ),
    ]

    actual = tweet_data.process()

    assert actual == expected
