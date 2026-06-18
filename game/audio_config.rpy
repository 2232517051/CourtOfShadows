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
define audio.tavern_lively = "audio/music/tavern_lively.ogg"
define audio.forest_ambient = "audio/music/forest_ambient.ogg"
define audio.rain_storm = "audio/music/rain_storm.ogg"
define audio.market_bustle = "audio/music/market_bustle.ogg"
define audio.church_choir = "audio/music/church_choir.ogg"
define audio.dungeon_drip = "audio/music/dungeon_drip.ogg"
define audio.harbor_waves = "audio/music/harbor_waves.ogg"
define audio.campfire = "audio/music/campfire.ogg"
define audio.war_drums = "audio/music/war_drums.ogg"
define audio.coronation = "audio/music/coronation.ogg"
define audio.conspiracy = "audio/music/conspiracy.ogg"
define audio.chase = "audio/music/chase.ogg"
define audio.romance = "audio/music/romance.ogg"
define audio.grief = "audio/music/grief.ogg"
define audio.revelation = "audio/music/revelation.ogg"
define audio.betrayal = "audio/music/betrayal.ogg"
define audio.hope = "audio/music/hope.ogg"
define audio.winter_wind = "audio/music/winter_wind.ogg"
define audio.dawn = "audio/music/dawn.ogg"
define audio.ritual = "audio/music/ritual.ogg"

## 音效定义
define audio.sfx_door_knock = "audio/sfx/door_knock.ogg"
define audio.sfx_sword_draw = "audio/sfx/sword_draw.ogg"
define audio.sfx_fire_crackle = "audio/sfx/fire_crackle.ogg"
define audio.sfx_horse_gallop = "audio/sfx/horse_gallop.ogg"
define audio.sfx_crowd_murmur = "audio/sfx/crowd_murmur.ogg"
define audio.sfx_bell_toll = "audio/sfx/bell_toll.ogg"

## 主菜单背景音乐
## (2026-06-05 玩家"大制图家"反馈 main_theme 太亢奋且循环 → 换庄严王座主题)
define config.main_menu_music = "audio/music/throne.ogg"

## 音乐频道设置
init python:
    # 默认音乐音量
    config.default_music_volume = 0.7
    # 音乐淡入淡出时间（秒）
    config.fade_music = 1.0
