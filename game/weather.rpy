## ============================================================
## 天气 & 氛围特效系统
## weather.rpy — 雨/雪/雾/雷电/萤火虫
## ============================================================

################################################################################
## 1. 雨天效果
################################################################################

init python:
    import random as _random

    class RainParticle(object):
        def __init__(self):
            self.reset()

        def reset(self):
            self.x = _random.randint(0, 1280)
            self.y = _random.randint(-100, -10)
            self.speed = _random.uniform(600, 900)
            self.length = _random.randint(10, 25)
            self.alpha = _random.uniform(0.15, 0.4)

    class SnowParticle(object):
        def __init__(self):
            self.reset()

        def reset(self):
            self.x = _random.randint(0, 1280)
            self.y = _random.randint(-50, -10)
            self.speed = _random.uniform(30, 80)
            self.drift = _random.uniform(-20, 20)
            self.size = _random.randint(2, 5)
            self.alpha = _random.uniform(0.3, 0.7)


## ── 雨滴 Screen ──
screen weather_rain(intensity="normal"):
    zorder 90
    $ _rain_count = 30 if intensity == "light" else (60 if intensity == "normal" else 100)

    ## 雨天色调滤镜
    add Solid("#0a0a1808")

    for i in range(_rain_count):
        $ _rx = renpy.random.randint(0, 1280)
        $ _ry = renpy.random.randint(-200, -10)
        $ _rspeed = renpy.random.uniform(0.3, 0.6)
        $ _ralpha = renpy.random.uniform(0.15, 0.35)

        add Solid("#8899bb"):
            xpos _rx
            ypos _ry
            xsize 1
            ysize renpy.random.randint(12, 25)
            alpha _ralpha
            at rain_fall(_rspeed, _rx)

    ## 闪电（暴雨时偶尔触发）
    if intensity == "heavy":
        timer renpy.random.uniform(8.0, 20.0) action [Show("flash_white"), Play("sound", "audio/sfx/thunder.ogg")] repeat True


transform rain_fall(duration=0.5, start_x=0):
    ypos -30
    alpha 0.3
    parallel:
        linear duration ypos 750
    parallel:
        linear duration xoffset renpy.random.randint(-10, 10)
    alpha 0.0
    ypos renpy.random.randint(-200, -10)
    xpos renpy.random.randint(0, 1280)
    repeat


## ── 雪花 Screen ──
screen weather_snow(intensity="normal"):
    zorder 90
    $ _snow_count = 20 if intensity == "light" else (40 if intensity == "normal" else 70)

    ## 冬天色调
    add Solid("#e8eef808")

    for i in range(_snow_count):
        $ _sx = renpy.random.randint(0, 1280)
        $ _ssize = renpy.random.randint(2, 6)
        $ _sspeed = renpy.random.uniform(4.0, 8.0)

        $ _salpha = renpy.random.uniform(0.3, 0.7)
        $ _scolor = "#ffffff%02x" % int(_salpha * 255)
        text "•":
            xpos _sx
            ypos renpy.random.randint(-50, -10)
            size _ssize
            color _scolor
            at snow_drift(_sspeed)


transform snow_drift(duration=6.0):
    ypos -30
    parallel:
        linear duration ypos 750
    parallel:
        block:
            ease (duration/4) xoffset 20
            ease (duration/4) xoffset -15
            ease (duration/4) xoffset 10
            ease (duration/4) xoffset -10
    ypos renpy.random.randint(-50, -10)
    xpos renpy.random.randint(0, 1280)
    repeat


## ── 雾气 Screen ──
screen weather_fog(density="normal"):
    zorder 85
    $ _fog_alpha = 0.15 if density == "light" else (0.3 if density == "normal" else 0.45)

    ## 两层雾，不同速度移动
    add Solid("#c8c8c8"):
        alpha _fog_alpha * 0.5
        at fog_layer_1

    add Solid("#a0a8b0"):
        alpha _fog_alpha * 0.3
        at fog_layer_2


transform fog_layer_1:
    alpha 0.15
    block:
        ease 8.0 alpha 0.25 xoffset 30
        ease 8.0 alpha 0.15 xoffset -20
        ease 6.0 alpha 0.2 xoffset 10
        repeat

transform fog_layer_2:
    alpha 0.1
    block:
        ease 10.0 alpha 0.18 xoffset -25
        ease 12.0 alpha 0.1 xoffset 35
        ease 8.0 alpha 0.14 xoffset -15
        repeat


## ── 萤火虫 Screen（夜间花园等）──
screen weather_fireflies(count=15):
    zorder 95

    for i in range(count):
        $ _fx = renpy.random.randint(50, 1230)
        $ _fy = renpy.random.randint(100, 650)

        text "·":
            xpos _fx
            ypos _fy
            size renpy.random.randint(3, 6)
            color "#aadd44"
            at firefly_float(_fx, _fy, renpy.random.uniform(3.0, 7.0))


transform firefly_float(sx, sy, dur):
    pos (sx, sy)
    alpha 0.0
    ease 1.0 alpha 0.8
    block:
        ease dur xoffset renpy.random.randint(-40, 40) yoffset renpy.random.randint(-30, 30) alpha renpy.random.uniform(0.2, 0.9)
        ease dur xoffset renpy.random.randint(-30, 30) yoffset renpy.random.randint(-20, 20) alpha renpy.random.uniform(0.1, 0.8)
        repeat


################################################################################
## 2. 天气控制函数
################################################################################

init python:
    _current_weather = None

    def set_weather(weather_type, intensity="normal"):
        """设置天气效果。
        weather_type: "rain", "snow", "fog", "fireflies", None(清除)
        intensity: "light", "normal", "heavy"
        用法: $ set_weather("rain", "heavy")
        """
        global _current_weather
        ## 先清除旧天气
        clear_weather()
        _current_weather = weather_type
        if weather_type == "rain":
            renpy.show_screen("weather_rain", intensity=intensity)
        elif weather_type == "snow":
            renpy.show_screen("weather_snow", intensity=intensity)
        elif weather_type == "fog":
            renpy.show_screen("weather_fog", density=intensity)
        elif weather_type == "fireflies":
            renpy.show_screen("weather_fireflies")

    def clear_weather():
        """清除所有天气效果"""
        global _current_weather
        for w in ["weather_rain", "weather_snow", "weather_fog", "weather_fireflies"]:
            if renpy.get_screen(w):
                renpy.hide_screen(w)
        _current_weather = None

    def get_weather():
        return _current_weather
