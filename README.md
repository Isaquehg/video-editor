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

4. Use the commands

        # Using example:

        
        ----------------------------------------
        Seja bem-vindo ao EDITOR SEM UI!
        Digite os seguintes comandos para editar seu vídeo:
        'select' - Para selecionar o vídeo e o seu caminho 
        'clip' - Para cortar partes do vídeo
        chromakey
        volume
        contrast
        speed
        brightness
        invertColor
        'painting' - Para efeito de pintura
        save
        ----------------------------------------

        ----------------------------------------
        Comando: select
        ----------------------------------------

        ----------------------------------------
        Entre com o endereço do seu vídeo: ./videos/bigbuckbunny.mp4
        ----------------------------------------
        Size: [1280, 720]
        FPS: 25.0
        Duration: 5.31 seconds
        Amount of Frames: 133
        ----------------------------------------

        ----------------------------------------
        Comando: speed
        ----------------------------------------

        ----------------------------------------
        Entre com um valor decimal de 0 a 2.5: 2
        ----------------------------------------

        ----------------------------------------
        Comando: save
        ----------------------------------------

        ----------------------------------------
        Moviepy - Building video ./results/modified_video.mp4.
        MoviePy - Writing audio in modified_videoTEMP_MPY_wvf_snd.mp3
        MoviePy - Done.
        Moviepy - Writing video ./results/modified_video.mp4

        Moviepy - Done !
        Moviepy - video ready ./results/modified_video.mp4
        Ta salvo
        ----------------------------------------

        ----------------------------------------
        Comando: sair
        ----------------------------------------

        ----------------------------------------
        Tchau tchau!
        ----------------------------------------



## Functionalities

### Select
The `select` command allows you to identify the video that will be edited.

### Clip
The `clip` command allows you to trim a video by specifying the start and end times.

### Brightness
The `brightness` command adjusts the brightness of the video using the `gamma_corr` effect in MoviePy.

### Contrast
The `contrast` command changes the contrast of the video using the `lum_contrast` effect in MoviePy.

### Volume
The `volume` command modifies the volume of the video by applying a volume factor.

### Speed
The `speed` command alters the speed of the video by multiplying it by a speed factor.

### Invert Color
The `invertColor` command inverts the colors of the video using the `invert_colors` effect in MoviePy.

### Painting Effect
The `painting` command transforms the video into a painting using the `painting` effect in MoviePy.

### Chrome Key
The `chromakey` command applies an image background to replace a given RGB value in the original video

### Save
The 'save' command saves the video and stores it in the `/results` folder

