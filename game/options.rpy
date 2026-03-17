## 游戏基本配置

define config.name = _("权谋之庭 - Court of Shadows")
define config.version = "2.1"

define gui.show_name = True
define gui.about = _p("""
{b}权谋之庭 - Court of Shadows{/b}
一款中世纪宫廷权谋视觉小说。

你是新任艾登堡领主，在贵族、教会与王权的夹缝中求生。
你的每一个选择都将影响权力的天平。

{b}特色：{/b}
· 五章完整剧情，约3-4小时游戏时长
· 六维属性系统 + 角色好感度
· 多条故事分支，五个独特结局
· 23+游戏系统：画廊、音乐室、成就、章节选择等
· 隐藏成就、收藏品与New Game+
· 油画风格美术，暗黑皇家金主题UI

{b}制作：{/b}
v2.0 — 完整版

基于 Ren'Py 引擎制作
""")

define build.name = "CourtOfShadows"

## 窗口设置
define config.screen_width = 1280
define config.screen_height = 720

define config.save_directory = "CourtOfShadows-save"

define config.window_icon = "gui/window_icon.png"

## 存档数量
define config.has_autosave = True
define config.autosave_slots = 5

## 安卓返回键 = 打开游戏菜单（而非直接退出）
define config.quit_action = ShowMenu("confirm", _("确定要退出游戏吗？"), MainMenu(), Return())

## 横屏锁定（视觉小说标准）
define build.android_landscape = True

## 构建配置
init python:
    ## 源文件不打包
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.py', None)
    build.classify('game/**.rpyc', 'all')
    build.classify('game/**.png', 'all')
    build.classify('game/**.webp', 'all')
    build.classify('game/**.jpg', 'all')
    build.classify('game/**.ogg', 'all')
    build.classify('game/**.mp3', 'all')
    build.classify('game/**.ogg', 'all')
    build.classify('game/**.ttf', 'all')
    build.classify('game/**.ttc', 'all')

    build.documentation('README.txt')

    ## Android 包名 — TapTap 上架必须唯一
    build.android_package = "com.xiaoyiai.courtofshadows"

    ## Android 权限（视觉小说不需要额外权限）
    build.android_permissions = []

    ## 目标 API（TapTap 要求 API 30+）
    build.android_target_api = 33
