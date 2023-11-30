# video-editor
Video Editor usign Python, with [MoviePy](https://zulko.github.io/moviepy/index.html)

## Table of Contents
- [About](#about)
- [Setup](#setup)
- [Project Structure](#project-structure)
- [Functionalities](#functionalities)
  - [Clip Video](#clip-video)
  - [Brightness](#brightness)
  - [Contrast](#contrast)
  - [Volume](#volume)
  - [Speed](#speed)
  - [Invert Color](#invert-color)
  - [Paiting effect](#paiting-effect)
- [Contributors](#contributors)
- [License](#license)

## About
This project is developed for the Computer Graphics and Multimedia lecture (C209). It provides a simple video editor implemented in Python using the MoviePy library. The editor offers several functionalities to clip, modify brightness, contrast, volume, speed, invert colors, and apply a painting effect to manipulate the video.


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


## Project Structure
The project's folder structure is the following:

        /video-editor
        │   .gitignore
        │   commands.py
        │   editor.py
        │   LICENSE
        │   main.py
        │   README.md
        │   requirements.txt
        │
        │─── /images
        │    └── [Images for Chroma Key]
        │─── /results
        │    └── [Final Video]
        │─── /videos
        │    └── [Video Files to be edited]


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
The `save` command saves the video and stores it in the `/results` folder

## Contributors
This project was developed by [Arthur Assis](https://github.com/Arthur521), [Isaque Hollanda](https://github.com/Isaquehg) and [Vitor Pestalozi]()

## License
MIT License

Copyright (c) 2023 Isaque Hollanda Gonçalves

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
