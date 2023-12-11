class Cache:
    def __init__(self, user_id):
        self.cache_global = dict()
        self.user_id = user_id

    def add_request(self, datetime_now):
        self.cache_global[self.user_id]
