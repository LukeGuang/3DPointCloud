class Line:
    def __init__(self, ori, direction):
        self._ori = ori
        self._direction = direction

    @property
    def ori(self):
        return self._ori

    @property
    def direction(self):
        return self._direction

    @ori.setter
    def ori(self, ori):
        self._ori = ori

    @direction.setter
    def direction(self, direction):
        self._direction = direction
