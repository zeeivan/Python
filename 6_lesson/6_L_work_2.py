class Road:
       def __init__ (self, _length, _width, _volume):
            self._length = _length
            self._width = _length
            self._volume = _volume
       def mass(self):
            return int(self._length) * int(self._width) * int(self._volume)
wheight = Road (15, 3000, 10)
print(wheight.mass())

