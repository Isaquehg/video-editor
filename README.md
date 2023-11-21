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

3. Run the Application

        python main.py

4.Use the commands

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


