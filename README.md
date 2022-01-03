# AI-assistant
***
#简介：
<p>本项目类似于手机上的语音助手，你对他说话，他回复你,也可以控制电脑上的一些程序，如打开QQ，音乐，睡眠，计算器等。项目分为六个模块,第一模块one_luyin.py是采集音频并保存以wav格式。第二模块识别所录音频，这期间会用到百度语音识别技术。第三模块接入图灵机器人，并将识别内容传送到图灵机器人，得到回复内容。第四模块将图灵机器人回复内容通过百度语音合成音频，第五模块就是简单的播放操作了。</p>

#运行：
该项目中有两个运行文件，一个是run.py,通过该文件运行时，对话内容会显示在命令行中，并未用到GUI画面；另一个是RUN_GUI.py，该文件通过GUI画面运行，但在命令行中仍会显示对话内容。以上两种运行方式是在编译器中运行的，若想生成独立的exe文件，也可在pycharm终端进行如下命令：  
<code>pip install pyinstaller</code>  
<code>pyinstall -F RUN_GUI.py</code>  

<p>生成exe文件打开后可能出现 cmd一闪而过，而程序并没有正常运行，这个原因可能是pygame包与exe文件没有在同一文件夹下，建议将exe文件与pygame包放到与模块源文件同一文件夹下</p>

#运行界面
![img.png](img/img.png)


<p>这个背景透明度可以自行更改的哈，在RUN_GUI.py中<code>myWindow.attributes('-alpha',0.9)   #设置透明度</code>即可设置</p>

#联系作者
<p>如有错误，可发送内容至3342726501@qq.com,也可加QQ:3342726501</p>
