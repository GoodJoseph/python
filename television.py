class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self): #OK
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__mutedvolume = None

    def power(self): #OK
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self): #OK
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__mutedvolume = self.__volume
                self.__volume = self.MIN_VOLUME
            if self.__muted == False:
                self.__volume = self.__mutedvolume

    def channel_up(self): #OK
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self): #OK
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self): #OK
        if self.__status and not self.__muted:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__mutedvolume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__mutedvolume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f"Power - [{self.__status}], Channel - [{self.__channel}], Volume - [{self.__volume}]"

