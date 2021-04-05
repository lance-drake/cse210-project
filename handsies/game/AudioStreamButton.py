import arcade

class AudioStreamButton():
    """ Button, click-for-streaming-sound """

    def __init__(self, sound_file, pan, volume):
        self.sound = arcade.Sound(sound_file, streaming=True)
        self.pan = pan
        self.volume = volume

    def play(self):
        self.sound.play(volume=self.volume, pan=self.pan)

    def volume_up(self):
        vol = self.sound.get_volume()
        self.sound.set_volume(vol + 0.1)
        print(f"Volume: {self.sound.get_volume()}")

    def volume_down(self):
        vol = self.sound.get_volume()
        self.sound.set_volume(vol - 0.1)
        print(f"Volume: {self.sound.get_volume()}")

    def stream_position(self):
        print(f"Current position: {self.sound.get_stream_position()}")