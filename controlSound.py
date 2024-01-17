import pygame


class SoundController:
    """
        Class for controlling music playback using the Pygame library.

        Methods:
        - __init__: Initializes the sound controller and loads the sound file.
        - play_sound: Starts playing music with the set volume.
        - stop_sound: Stops the music playback.
        - pause_music: Pauses the music playback.
        - volume_up_music: Increases the volume of the playing music.
        - volume_down_music: Decreases the volume of the playing music.
        - unpause_music: Resumes music playback after a pause.

        Notes:
        - Ensure that the sound file is in the same directory as the script,
          or provide the full path to the file during initialization.
        - Methods related to volume adjustment assume values in the range
          from 0.0 to 1.0, where 0.0 means muted and 1.0 means full volume.
        """
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("lobby-classic-game.mp3")

    def play_sound(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def stop_sound(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def volume_up_music(self):
        pygame.mixer.music.set_volume(0.7)

    def volume_down_music(self):
        pygame.mixer.music.set_volume(0.2)

    def unpause_music(self):
        pygame.mixer.music.unpause()
