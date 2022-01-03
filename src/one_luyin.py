import speech_recognition as sr  # pyaudio SpeechRecognition模块


def rec(rate=16000):  # 从系统麦克风拾取音频数据，采样率为 16000
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")  # 这里会打印please say something，提示你说话进行录音
        audio = r.listen(source)

    with open("audio/recording.wav", "wb") as f:  # 把采集到的音频数据以 wav 格式保存在当前目录下的recording.wav 文件
        f.write(audio.get_wav_data())
    # return 1
