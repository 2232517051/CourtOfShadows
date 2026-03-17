## ============================================================
## 音频配置 - 背景音乐 & 音效
## ============================================================

## 背景音乐定义
define audio.main_theme = "audio/music/main_theme.ogg"
define audio.castle_calm = "audio/music/castle_calm.ogg"
define audio.great_hall = "audio/music/great_hall.ogg"
define audio.tension = "audio/music/tension.ogg"
define audio.battle_prepare = "audio/music/battle_prepare.ogg"
define audio.night_mystery = "audio/music/night_mystery.ogg"
define audio.victory = "audio/music/victory.ogg"
define audio.sad = "audio/music/sad.ogg"

## 音效定义
define audio.sfx_door_knock = "audio/sfx/door_knock.ogg"
define audio.sfx_sword_draw = "audio/sfx/sword_draw.ogg"
define audio.sfx_fire_crackle = "audio/sfx/fire_crackle.ogg"
define audio.sfx_horse_gallop = "audio/sfx/horse_gallop.ogg"
define audio.sfx_crowd_murmur = "audio/sfx/crowd_murmur.ogg"
define audio.sfx_bell_toll = "audio/sfx/bell_toll.ogg"

## 音乐频道设置
init python:
    # 默认音乐音量
    config.default_music_volume = 0.7
    # 音乐淡入淡出时间（秒）
    config.fade_music = 1.0
