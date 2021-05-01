from app_config import NUM_OF_TOP_STORIES, logger
from correlation_util import calc_correlation
from stories_util import get_top_stories, print_stories, print_comments


def run():
    print('loading HNShell...')
    top_stories = get_top_stories(NUM_OF_TOP_STORIES)
    if top_stories is None:
        print('Something went wrong getting the stories')
        exit()

    while True:
        print('\nWelcome to HNShell! What can we do for you today?')
        print('[1] show me todays\' 40 top stories')
        print('[2] show me the popularity-posting time correlation')
        try:
            user_choice = int(input())
            if user_choice != 1 and user_choice != 2:
                raise ValueError

            if user_choice == 1:
                print_stories(top_stories)
                print('Insert an articles rank to watch its comments')
                article_rank = int(input())
                if article_rank < 1:
                    raise IndexError

                print_comments(top_stories[article_rank - 1])
            else:
                print('we\'re working on it!')
                coefficient = calc_correlation()
                logger.info(f"current coefficient: {coefficient}")
                print(f"The correlation coefficient between number of comments to publish "
                      f"proximity to 8pm is:\n {coefficient}")

        except ValueError:
            print('The value entered is not a number')
        except IndexError:
            print('Pick a value between 1-40')
        except AssertionError:
            print('Please pick a valid option')


if __name__ == '__main__':
    run()
