class State(object):
    def __init__(self):
        self._state = None

    def set_state(self, value):
        self._state = value

    def __getattr__(self, name):
        return getattr(self._state, name)

state = State()
