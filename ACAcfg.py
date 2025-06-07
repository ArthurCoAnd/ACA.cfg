import os
import platform
import shutil

def ACAcfg():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("    _    ____    _           __       ")
    print("   / \  / ___|  / \     ___ / _| __ _ ")
    print("  / _ \| |     / _ \   / __| |_ / _` |")
    print(" / ___ \ |___ / ___ \ | (__|  _| (_| |")
    print("/_/   \_\____/_/   \_(_)___|_|  \__, |")
    print("                                |___/ ")

    dir_aca = os.path.dirname(os.path.realpath(__file__))
    
    dir_linux = 'SteamLibrary/steamapps/common/Counter-Strike Global Offensive/game/csgo/cfg'
    dir_macos = '~/Library/Application Support/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/cfg'
    dir_windows = 'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg'
    
    # Definir qual o sistema e pasta do jogo
    os_type = platform.system()
    if os_type == 'Windows':
        print("Sistema: Windows")
        dir_cs2 = dir_windows
    elif os_type == 'Linux':
        print("Sistema: Linux")
        dir_cs2 = dir_linux
    elif os_type == 'Darwin':
        print("Sistema: MacOS")
        dir_cs2 = dir_macos
    else:
        print("ERRO: Sistema incompatível!!!")
        return
    
    # Verificar se existe pasta do jogo
    if not os.path.isdir(dir_cs2):
        print('NÃO ESTÁ INSTALADO!!!')
        return
    
    # Copiar arquivo ACA.cfg
    arq_aca = os.path.join(dir_aca, 'ACA.cfg')
    arq_cs2 = os.path.join(dir_cs2, 'ACA.cfg')
    shutil.copy(arq_aca, arq_cs2)

if __name__ == '__main__':
    ACAcfg()