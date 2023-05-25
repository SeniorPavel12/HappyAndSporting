class RequestEvent:

    def __init__(self, type, workout):
        self.workout = workout
        self.type = type
        all_request_event_name = {'SW', 'EN', 'NT'}
        if self.type not in all_request_event_name:
            raise KeyError('name объекта RequestEvent неправильное')


class ResponseEvent:
    def __init__(self, type, data, other_data=None):
        if other_data is None:
            other_data = {}
        if type not in ['break', 'approach', 'end']:
            raise KeyError
        self.type = type
        self.data = data
        self.other_data = other_data
