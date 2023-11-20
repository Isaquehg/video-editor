import moviepy.editor as mpe

class Editor():
    def __init__(self, path_to_video: str) -> None:
        self.video = mpe.VideoFileClip(path_to_video) # .mp4 video
        self.audio = self.video.audio
        self.duration = self.video.duration

        print('Size:', self.video.size) ## or video.h and video.w
        print('FPS:', self.video.fps)
        print('Duration:', self.video.duration, 'seconds')
        print('Amount of Frames:', self.video.reader.nframes)
        #print('Sampling Rate:', self.audio.fps, 'Hz')

    def clip_video(self, start_time, end_time):
        self.video = self.video.subclip(start_time, end_time)
        self.duration = self.video.duration

    def volume(self, volume_factor):
        self.audio = self.audio.volumex(volume_factor)

    def brightness(self, factor):
        self.video = self.video.fx(mpe.vfx.colorx, factor)

    def contrast(self, factor):
        self.video = self.video.fx(mpe.vfx.lum_contrast, contrast=factor)

    def speed(self, factor):
        self.video = self.video.fx(mpe.vfx.speedx, factor)
        self.duration = self.video.duration

    def invert_color(self):
        # Inverter as cores do vídeo
        self.video = self.video.fx(mpe.vfx.invert_colors)

    def paiting_effect(self, factor):
        self.video = self.video.fx(mpe.vfx.painting, factor)

    def chroma_key(self, color_rgb, background_image_path):
        background = mpe.ImageClip(background_image_path)

        masked_clip = self.video.fx(mpe.vfx.mask_color, color=color_rgb, thr=100, s=5)

        self.video = mpe.CompositeVideoClip([
            background,
            masked_clip
        ]).set_duration(self.duration)

    def save_video(self, output_path='./results/modified_video.mp4'):
        self.video.write_videofile(output_path, fps=24)

# Usage Example
video_editor = Editor("./videos/windmill.mp4")
#video_editor = Editor("./videos/bigbuckbunny.mp4") -> use this one to test the volume modifications

# Clipping the video
video_editor.clip_video(3, 5)

# Modifying the Volume
#video_editor.volume(1.5)

# Modifying Contrast
video_editor.contrast(1.5)

# Modifying Video Speed
video_editor.speed(1.5)

# Modifying Brightness
video_editor.brightness(0.7)

# Inverting Colours
video_editor.invert_color()

# Efeito de pintura
video_editor.paiting_effect(1.3)

# Applying Chroma Key
video_editor.chroma_key([4,179,68], "images/nature_grass.png")

# Saving Video to /results
video_editor.save_video()
