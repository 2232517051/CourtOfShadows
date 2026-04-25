## 游戏基本配置

define config.name = _("权谋之庭 - Court of Shadows")
define config.version = "3.2"

define gui.show_name = True
define gui.about = _p("""
{b}权谋之庭 - Court of Shadows{/b}
一款中世纪宫廷权谋视觉小说。

你是新任艾登堡领主，在贵族、教会与王权的夹缝中求生。
你的每一个选择都将影响权力的天平。

{b}特色：{/b}
· 五章完整剧情，35万字，约8-10小时游戏时长
· 六维属性系统 + 角色好感度
· 多条故事分支，五个独特结局 + 隐藏结局
· 章间过渡、NPC深度支线、治理系统
· 画廊、音乐室、成就、章节选择、收藏品
· 隐藏成就与New Game+
· 油画风格美术，暗黑皇家金主题UI

{b}制作：{/b}
v3.2 — 剧情修正 & Bug修复版

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

## 移动端后台保存：关屏/切后台时自动存档，防止进程被杀后黑屏
define config.save_on_mobile_background = True

## 安卓/iOS返回键 = 打开游戏菜单（而非直接退出）
define config.quit_action = ShowMenu("confirm", _("确定要退出游戏吗？"), MainMenu(), Return())

## 横屏锁定（视觉小说标准，Android + iOS）
define build.android_landscape = True
define build.ios_landscape = True

## 桌面端窗口可自由调整大小
define config.gl2 = True

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

    ## 按平台分类打包
    build.classify('game/**.rpyc', 'all')
    build.classify('game/**.png', 'all')
    build.classify('game/**.webp', 'all')
    build.classify('game/**.jpg', 'all')
    build.classify('game/**.ogg', 'all')
    build.classify('game/**.mp3', 'all')
    build.classify('game/**.ttf', 'all')
    build.classify('game/**.ttc', 'all')
    build.classify('game/**.ico', 'windows')
    build.classify('game/**.icns', 'mac')

    build.documentation('README.txt')

    ## ── Android 配置 ──
    build.android_package = "com.xiaoyiai.courtofshadows"
    build.android_permissions = []
    build.android_target_api = 33

    ## ── iOS 配置 ──
    build.ios_bundle_identifier = "com.xiaoyiai.courtofshadows"
    build.ios_bundle_name = "权谋之庭"

    ## ── 桌面端配置 ──
    ## Windows 可执行文件名
    build.executable_name = "CourtOfShadows"

    ## 支持多架构（含 Apple Silicon）
    build.mac_architectures = "universal"

    ## Google Play（暂不上架）
    build.google_play_key = None
    build.google_play_salt = None
