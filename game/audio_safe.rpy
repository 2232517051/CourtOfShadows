## ============================================================
## 音频安全封装 - 缺少音频文件时不崩溃 + 日志记录
## ============================================================

init python:

    ## 记录缺失的音频文件（避免重复警告）
    _missing_audio_warned = set()

    def _audio_warn(filename):
        """记录缺失音频文件的警告"""
        if filename not in _missing_audio_warned:
            _missing_audio_warned.add(filename)
            renpy.log("! 音频文件缺失: %s" % filename)

    def play_music(filename, fadein=0.0, fadeout=0.0, loop=True):
        if renpy.loadable(filename):
            renpy.music.play(filename, channel="music", fadein=fadein, fadeout=fadeout, loop=loop, if_changed=True)
        else:
            _audio_warn(filename)

    def play_sound(filename):
        if renpy.loadable(filename):
            renpy.sound.play(filename, channel="sound")
        else:
            _audio_warn(filename)

    def stop_music(fadeout=1.0):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def play_sfx_safe(filename, channel="sound"):
        """安全播放音效（指定频道）"""
        if renpy.loadable(filename):
            renpy.sound.play(filename, channel=channel)
        else:
            _audio_warn(filename)
