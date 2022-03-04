from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from ffpyplayer.player import MediaPlayer
from kivy.uix.videoplayer import VideoPlayer

import cv2

class Gerenciador(ScreenManager):
    pass

def getVideoSource(source, width, height):
        cap = cv2.VideoCapture(source)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        return cap

class Menu(Screen):
    def playSound(self):
        sound = SoundLoader.load('sounds/rapaz.mp3')
        if sound:
            sound.play()

    def playVideo1(self):
        sourcePath = "videos/video.mp4"
        camera = getVideoSource(sourcePath, 720, 480)
        player = MediaPlayer(sourcePath)

        while True:
            ret, frame = camera.read()
            audio_frame, val = player.get_frame()

            if (ret == 0):
                print("End of video")
                break

            cv2.imshow('Camera', frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

            if val != 'eof' and audio_frame is not None:
                frame, t = audio_frame
                print("Frame:" + str(frame) + " T: " + str(t))

        camera.release()
        cv2.destroyAllWindows()

    def playVideo2(self):
        videoplayer = VideoPlayer(source = 'videos/video2.mp4')
        videoplayer.state = 'play'
        videoplayer.options = {'eos':'loop'}
        videoplayer.allow_stretch = True
        videoplayer.allow_fullscreen = True

        return VideoPlayer


    pass

class Tarefas(Screen):
    def __init__(self, tarefas=[],**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text = tarefa))

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text = texto))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self, text = '',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Gerenciador()

Test().run()

