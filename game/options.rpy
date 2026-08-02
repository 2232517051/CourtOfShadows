## 游戏基本配置

define config.name = _("权谋之庭 - Court of Shadows")
define config.version = "3.9.2"

define gui.show_name = True
define gui.about = _p("""
{b}权谋之庭 - Court of Shadows{/b}

父亲骤逝后，你继承艾登堡，成为这里的新领主。他的死因仍是一桩疑案，而贵族、教会与王权已经各自登门。

全篇共五章，包含九个主线结局与一个隐藏尾声。你的选择会关上一些道路，也会打开另一些道路。

{b}版本：{/b}v3.9.2

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
    build.android_target_api = 36

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
