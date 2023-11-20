# video-editor
Video Editor usign Python, with [MoviePy](https://zulko.github.io/moviepy/index.html) and []

## Table of Contents
- [About](#about)
- [Setup](#setup)
- [Functionalities](#functionalities)
  - [Clip Video](#clip-video)
  - [Brightness](#brightness)
  - [Contrast](#contrast)
  - [Volume](#volume)
  - [Speed](#speed)
  - [Invert Color](#invert-color)
  - [Paiting effect](#paiting-effect)
- [Results](#results)

## About
This project is developed for the Computer Graphics and Multimedia lectures (C209). It provides a simple video editor implemented in Python using the MoviePy library. The editor offers various functionalities to clip, modify brightness, contrast, volume, speed, invert colors, and apply a painting effect to videos.


## Setup
1. Create Virtual Enviroment and activate it

        python3 -m venv venv
        source venv/bin/activate

2. Install the requirements

        pip install -r requirements.txt

3. Modify the function parameters accordinly to your needs and set the video path

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
        video_editor.invert_color()

        # Salvando o vídeo modificado
        video_editor.save_video()

4. Run the Application

        python editor.py

## Functionalities
### Clip Video
The `clip_video` function allows you to trim a video by specifying the start and end times.

### Brightness
The `modify_brightness` function adjusts the brightness of the video using the `gamma_corr` effect in MoviePy.

### Contrast
The `modify_contrast` function changes the contrast of the video using the `lum_contrast` effect in MoviePy.

### Volume
The `edit_volume` function modifies the volume of the video by applying a volume factor.

### Speed
The `modify_speed` function alters the speed of the video by multiplying it by a speed factor.

### Invert Color
The `invert_color` function inverts the colors of the video using the `invert_colors` effect in MoviePy.

### Painting Effect
The `painting_effect` function transforms the video into a painting using the `painting` effect in MoviePy.

### Chrome Key
The `chroma_key` function applies an image background to replace a given RGB value in the original video

## Results
The result from the modifications are saved in the `/results` folder