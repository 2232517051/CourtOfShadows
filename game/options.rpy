## 游戏基本配置

define config.name = _("权谋之庭 - Court of Shadows")
define config.version = "3.10"

define gui.show_name = True
define gui.about = _p("""
{b}权谋之庭 - Court of Shadows{/b}

父亲骤逝后，你继承艾登堡，成为这里的新领主。他的死因仍是一桩疑案，而贵族、教会与王权已经各自登门。

全篇共五章，包含九个主线结局与一个隐藏尾声。你的选择会关上一些道路，也会打开另一些道路。

{b}版本：{/b}v3.10

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

    ## Release packaging only; source files stay in the repository.
    build.classify('game/test_game.rpyc', None)
    build.classify('game/audio/music/*_alt.mp3', None)
    build.classify('game/audio/music/test3.wav', None)
    build.classify('game/audio/narration/test_guy.mp3', None)
    build.classify('game/audio/narration/voice_test/**', None)
    build.classify('game/images/hd/**', None)
    build.classify('game/images/backup_sd/**', None)
    build.classify('game/images/webp_backup/**', None)
    build.classify('store_assets/**', None)
    build.classify('tests/**', None)
    build.classify('docs/**', None)
    build.classify('Tools/**', None)
    build.classify('AGENTS.md', None)
    build.classify('_speaker_report.txt', None)
    build.classify('_ui_wiring_review.png', None)
    build.classify('all_chars.txt', None)
    build.classify('bgm_suno_progress.json', None)
    build.classify('CANON.md', None)
    build.classify('CHANGELOG.txt', None)
    build.classify('CHANGELOG_v3.0.md', None)
    build.classify('CLAUDE.md', None)
    build.classify('combat_ui_mockup.png', None)
    build.classify('cover_horizontal.png', None)
    build.classify('cover_vertical.png', None)
    build.classify('crisis_check_proposal.md', None)
    build.classify('DESCRIPTION.txt', None)
    build.classify('DEVELOPER_NOTE.txt', None)
    build.classify('first_meet_report.txt', None)
    build.classify('game_icon_256.jpg', None)
    build.classify('game_icon_256.png', None)
    build.classify('logo.png', None)
    build.classify('logo_gold.png', None)
    build.classify('long_dialogue.txt', None)
    build.classify('missing_portraits_A.txt', None)
    build.classify('missing_portraits_B.txt', None)
    build.classify('missing_portraits_full.json', None)
    build.classify('promo_horizontal.png', None)
    build.classify('promo_vertical.png', None)
    build.classify('sfx_elevenlabs_progress.json', None)
    build.classify('taptap_promo.png', None)
    build.classify('TapTap_v3.5.1_hotfix.md', None)
    build.classify('TapTap_v3.5_更新公告.md', None)
    build.classify('TapTap_v3.6_更新公告.md', None)
    build.classify('TapTap_v3.7_更新公告.md', None)
    build.classify('TapTap_v3.8_更新公告.md', None)
    build.classify('TapTap_v3.9_更新公告.md', None)
    build.classify('TapTap_v3.10_更新公告.md', None)
    build.classify('TapTap_回归声明.md', None)
    build.classify('ui_icons_progress.json', None)
    build.classify('voice_mapping.json', None)
    build.classify('wallpaper_library.png', None)
    build.classify('事件时间线审计报告.md', None)

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

    build.classify('README.txt', 'windows')
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
