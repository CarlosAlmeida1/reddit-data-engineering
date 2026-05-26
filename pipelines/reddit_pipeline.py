def reddit_pipeline(filter_name: str, subreddit: str, time_filter='day', limit=None):
    # connect to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    # extraction
    # transform
    # loading to csv