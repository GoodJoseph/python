class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self): 
        """The Television Attributes"""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__mutedvolume = None

    def power(self): 
        """Turns on/off the television"""
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self): 
        """Will turn on/off the volume"""
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__mutedvolume = self.__volume
                self.__volume = self.MIN_VOLUME
            if self.__muted == False:
                self.__volume = self.__mutedvolume

    def channel_up(self): 
        """Moves up a channel"""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self): 
        """Moves Down a Channel"""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self): 
        """Increases the volume by one, unless its at max volume"""
        if self.__status and not self.__muted:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__mutedvolume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decreases the volume by 1 unless its at minimum volume"""
        if self.__status and not self.__muted:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume = self.__mutedvolume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Explains the current status, channel, and volume of the Television"""
        return f"Power - [{self.__status}], Channel - [{self.__channel}], Volume - [{self.__volume}]"

