# video-editor
Video Editor usign Python

## Table of Contents
- [About](#about)
- [Setup](#setup)
- [Functionalities](#functionalities)
- [Results](#results)

## About

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
### Modify Volume
### Apply Paiting effect
### Modify Contrast
### Modify Speed
### Modify Brightness
### Invert Color

## Results