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

    def clip_video(self, start_time, end_time):
        self.video = self.video.subclip(start_time, end_time)

    def edit_volume(self, volume_factor):
        self.audio = self.audio.volumex(volume_factor)

    def paiting_effect(self, factor):
        self.video = self.video.fx(mpe.vfx.painting, factor)

    def modify_brightness(self, factor):
        self.video = self.video.fx(mpe.vfx.colorx, factor)

    def modify_contrast(self, factor):
        self.video = self.video.fx(mpe.vfx.lum_contrast, lum=factor)

    def modify_speed(self, factor):
        self.video = self.video.fx(mpe.vfx.speedx, factor)

    def invert_color(self):
        # Inverter as cores do vídeo
        self.video = self.video.fx(mpe.vfx.invert_colors)

    def save_video(self, output_path='./results/modified_video.mp4'):
        self.video.write_videofile(output_path)

# Exemplo de uso
video_editor = Editor("./videos/bigbuckbunny.mp4")

# Clipando o vídeo
video_editor.clip_video(3, 5)

# Modificando o volume
video_editor.edit_volume(1.5)

# Efeito de pintura
video_editor.paiting_effect(1.3)

# Modificando Contraste
video_editor.modify_contrast(1.2)

# Modifica Velocidade do Vídeo
video_editor.modify_speed(1.5)

# Modificando Brilho
video_editor.modify_brightness(0.7)

# Invertendo cores
#video_editor.invert_color()

# Salvando o vídeo modificado
video_editor.save_video()
