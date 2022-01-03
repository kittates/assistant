import pygame


def play():
    pygame.mixer.init()  # 初始化混音器模块（pygame库的通用做法，每一个模块在使用时都要初始化pygame.init()为初始化所有的pygame模块，可以使用它也可以单初始化这一个模块）
    pygame.mixer.music.load("audio/audio.mp3")  # 加载音乐 ######大坑，注意这里需要使用绝对路径（就是不是默认当前路径，我恶补一下绝对路径和相对路径）
    pygame.mixer.music.set_volume(0.5)  # 设置音量大小0~1的浮点数
    pygame.mixer.music.play()  # 播放音频
    while pygame.mixer.music.get_busy():  # 在音频播放未完成之前不退出程序
        pass
    pygame.mixer.music.unload()  # 停止加载音频


#play()
