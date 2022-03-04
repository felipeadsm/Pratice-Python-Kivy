from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class aaaa(App):
    def playVideo2(self):
        videoplayer = VideoPlayer(source='videos/video2.mp4')
        videoplayer.state = 'play'
        videoplayer.options = {'eos': 'loop'}
        videoplayer.allow_stretch = True

        return VideoPlayer

aaaa.run()