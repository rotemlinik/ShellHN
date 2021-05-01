from datetime import datetime, timedelta
from app_config import SECONDS_IN_HOUR, HOUR_FOR_CALC, MIDNIGHT, PROXIMITY_COLUMN, COMMENTS_AMOUNT_COLUMN, \
    COMMENTS_AMOUNT_KEY, PUBLISH_TIME_KEY
from stories_util import get_top_stories
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np


def calc_correlation():
    data = _create_data_()
    df = pd.DataFrame(data, columns=[PROXIMITY_COLUMN, COMMENTS_AMOUNT_COLUMN])
    sn.scatterplot(data=df, x=PROXIMITY_COLUMN, y=COMMENTS_AMOUNT_COLUMN)
    plt.show()

    return np.corrcoef(data[PROXIMITY_COLUMN], data[COMMENTS_AMOUNT_COLUMN])[0][1]


def _create_data_():
    stories = get_top_stories(None)
    if stories is not None:
        publish_proximity_to_8pm = []
        comments_amount = []
        for story in stories:
            publish_proximity_to_8pm.append(_calc_proximity_(story.get(PUBLISH_TIME_KEY)))
            comments_count = story.get(COMMENTS_AMOUNT_KEY)
            comments_amount.append(comments_count if comments_count is not None else 0)

        return {PROXIMITY_COLUMN: publish_proximity_to_8pm, COMMENTS_AMOUNT_COLUMN: comments_amount}


def _calc_proximity_(epoch_time):
    publish_time = datetime.fromtimestamp(epoch_time).time()
    delta1 = abs(timedelta(hours=publish_time.hour, minutes=publish_time.minute, seconds=publish_time.second) -
                 timedelta(hours=HOUR_FOR_CALC))
    delta2 = timedelta(hours=MIDNIGHT) - delta1
    proximity = min(delta1, delta2)

    # convert the delta to a float between 0-1
    return proximity.seconds / SECONDS_IN_HOUR
