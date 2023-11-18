import moviepy.editor as mpe
import numpy as np

class Editor():
    def __init__(self, path_to_video: str) -> None:
        self.video = mpe.VideoFileClip(path_to_video) # .mp4 video
        self.audio = self.video.audio

        print('Tamanho:', self.video.size) ## ou video.h e video.w
        print('FPS:', self.video.fps)
        print('Duração:', self.video.duration, 'segundos')
        print('Número de frames:', self.video.reader.nframes)
        print('Taxa de amostragem:', self.audio.fps, 'Hz')

    def clip_video(self, interval: tuple):
        pass

    def edit_volume(self):
        pass

    def apply_filter(self):
        pass

    def invert_color(self):
        pass

    def save_video(self):
        self.video.write_videofile('./results/modified_video.mp4')


video_editor = Editor("./videos/bigbuckbunny.mp4")