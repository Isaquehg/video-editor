from editor import Editor

class Commands:
    def __init__(self):
        self.commands = {}
        self.selecionado = False

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print()
            print("-" * 40)

            command = input("Comando: ")
            print("-" * 40)

            if command == "sair":
                print()
                print("-" * 40)
                print("Tchau tchau!")
                print("-" * 40)
                break
            elif command in self.commands:
                print()
                print("-" * 40)
                self.commands[command]()
                print("-" * 40)
            else:
                print()
                print("-" * 40)
                print("Comando errado, tente denovo!")
                print("-" * 40)


class Entradas(Commands):
    
    def __init__(self):
        super().__init__()
        self.add_command("select", self.select)
        self.add_command("chromakey", self.chromakey)
        self.add_command("clip", self.clip)
        self.add_command("volume", self.volume)
        self.add_command("contrast", self.contrast)
        self.add_command("speed", self.speed)
        self.add_command("brightness", self.brightness)
        self.add_command("invertColor", self.invertColor)
        self.add_command("painting", self.painting)
        self.add_command("save", self.save)

        
    def select(self):
        if self.selecionado == False:
            video = input("Entre com o endereço do seu vídeo: ")
            print("-" * 40)
            self.video_editor = Editor(video)
            self.selecionado = True
        else:
            print("Você já selecionou o vídeo!")
            print("-" * 40)

    def clip(self):
        start = input("Entre com o segundo que começa o corte: ")
        end = input("Entre com o segundo que termina o corte: ")
        self.video_editor.clip_video(start, end)

    def chromakey(self):
        video_back = input("Entre com o endereço do fundo: ")
        self.video_editor.chroma_key([4,179,68], video_back)
    
    def volume(self):
        vol = float(input("Entre com um valor decimal de 0 a 2.5: "))
        self.video_editor.volume(vol)
    
    def contrast(self):
        cont = float(input("Entre com um valor decimal de 0 a 2.5: "))
        self.video_editor.contrast(cont)
    
    def speed(self):
        spd = float(input("Entre com um valor decimal de 0 a 2.5: "))
        self.video_editor.speed(spd)
    
    def brightness(self):
        bt = float(input("Entre com um valor decimal de 0 a 2.5: "))
        self.video_editor.brightness(bt)

    def painting(self):
        pt = float(input("Entre com um valor decimal de 0 a 2.5: "))
        self.video_editor.paiting_effect(pt)
    
    def invertColor(self):
        self.video_editor.invert_color()
        print("Ta invertido")

    def save(self):
        self.video_editor.save_video()
        print("Ta salvo")

    def run(self):
        print()
        print()
        print()
        print("-" * 40)
        print("Seja bem-vindo ao EDITOR SEM UI!")
        print("Digite os seguintes comandos para editar seu vídeo:")
        print("'select' - Para selecionar o vídeo e o seu caminho")
        print("'clip' - Para cortar partes do vídeo")
        print("chromakey - Para substituir um fundo verde por outro vídeo")
        print("volume - Para alterar o volume do áudio")
        print("contrast - Para alterar o contraste do vídeo")
        print("speed - Para alterar a velocidade do vídeo")
        print("brightness - Para alterar o vrilho do vídeo")
        print("invertColor - Para inverter cores dos vídeos")
        print("'painting' - Para efeito de pintura")
        print("save - Para salvar o vídeo")
        print("-" * 40)
        super().run()