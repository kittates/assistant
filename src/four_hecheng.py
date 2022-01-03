from aip import AipSpeech

APP_ID = '25233505'
API_KEY = 'm8wVLmUw7GleBNO3AqwlaELr'
SECRET_KEY = 'iFFhWbdlj1GcNA6XHGRfuY9cybkzByUO'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def speak(text=""):
    result = client.synthesis(text, 'zh', 1, {  # 这里的参数可以调   zh表示中文
        'spd': 5,  # 语速
        'vol': 5,  # 音量
        'per': 4,  # 类型
    })

    if not isinstance(result, dict):
        with open('audio/audio.mp3', 'wb') as f:  # 保存为当前目录下mp3格式的音频：audio.mp3，不建议用wav格式，wav格式后面我用的是pagame播放无法识别
            f.write(result)
            f.close()


#speak('你好啊！')  # 运行speak函数,把机器人回复的文字转换成语音
