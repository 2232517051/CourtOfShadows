## ============================================================
## 第三章·尾声 —— 格伦瓦德村外 (3.9.3 玩家反馈·晨曦: "男爵应该提前收拾了，当前期小boss")
## 文案: claude-opus-4-6 最小约束生成 (docs/superpowers/specs/2026-08-05-raw-opus-copy-generation-design.md)。
##       接入时仅删去结尾"门房两封信"两段(与后续北疆信使/王后旨意场景冲突), 未改写正文。
## 触发: ch3_end 袭击善后之后、北疆议会信使之前; 盟约线(alliance_baron)跳过。
## 结果: baron_checked_early(A/B) → ch5 前哨战"乘胜追击"门槛前移 + 坎贝尔/莫林/瓦特三家援兵 + 战力分。
## 资源: 背景 bg_grenwald_standoff 专属(codex/gpt-image); 配乐复用 battle_prepare(对峙语境成立);
##       音效复用 horse_gallop / sword_draw; 立绘复用 baron / captain / elena / aldric / soldier_generic。
## ============================================================

default baron_checked_early = False   # 格伦瓦德对峙: 逼退(A)/智退(B)男爵 → 北境小领主记住艾登堡
default baron_clash_choice = ""       # "stand" / "scheme" / "yield" / ""(盟约线未发生)

label ch3_baron_clash:
    if alliance_baron:
        return
    $ set_mood("battle")
    $ play_music("audio/music/battle_prepare.ogg", fadein=2.0)
    scene bg grenwald_standoff with dissolve
    $ unlock_gallery("bg_grenwald_standoff")
    $ set_weather("snow", "light")
    $ play_sound("audio/sfx/horse_gallop.ogg")

    "风从北境山口灌下来，带着初冬头一场雪的腥味。你策马登上矮丘，格伦瓦德村的石顶屋舍便铺展在坡下。"
    "村口竖着三面黑狼旗。旗下是密密排开的骑兵，暗绿披风，银边在灰天里闪着冷光。你粗略一数——至少三百骑。"
    "雷恩勒住缰绳，目光钉在那面旗上。他没说话，但你看到他右手不自觉地握紧了刀柄，手背上的旧鞭痕因用力而泛白。"
    "艾琳娜策马靠过来，压低声音。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "他征了村里四成存粮，二十匹马。放话说要借隘口\"追剿匪徒\"。"
    hide elena_img
    $ hide_all_chars("aldric_img")
    show aldric_img at left with dissolve
    aldric "领主大人，我们的人刚修完外墙缺口，储粮还没补上。此刻不宜——"
    hide aldric_img
    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "他就是在赌我们不敢来。"

    $ hide_all_chars()
    "你拍了拍马颈，带队下坡。"
    "村中心的打谷场上，一个高大的身影站在临时搭起的帐篷前，手里捏着一只银杯。冯·哈根男爵没穿甲，只一件黑色貂裘，像是来做客而非带兵。他看到你的队列，并不意外，甚至微微举杯。"
    "男爵身后的骑兵军官按住剑柄，朝你的方向偏了偏头。"

    $ hide_all_chars("soldier_generic_img")
    show soldier_generic_img at left with dissolve
    baron_officer "是艾登堡的人。约一百出头，轻步兵为主。"

    $ hide_all_chars()
    "男爵将银杯递给侍从，整了整衣领，大步迎上来。他比你高半个头，目光从你身上扫过，又落在你身后的雷恩脸上，停了一瞬。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "年轻的艾登堡领主。你父亲在世时，我们隔着这道山口做了十年邻居。他从不亲自跑到边界来——倒是比你沉得住气。"
    hide baron_img
    $ hide_all_chars("player_char_img")
    show player_char_img at left with dissolve
    player "他也从没让别人的旗帜插在自己的村子里。"

    $ hide_all_chars()
    "男爵笑了一声。那种笑不到眼睛里的笑。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "几天前有股匪徒从北面来，烧了你的粮仓，砸了你的墙。我带人越境，是替你追剿残匪，顺便帮你看住这道口子。格伦瓦德的乡亲们可以作证，我的人秋毫无犯。"

    $ hide_all_chars()
    "他说\"秋毫无犯\"的时候，你注意到打谷场边上有两辆装满粮袋的马车，车辕上刻着村民的姓氏。"
    "雷恩向前半步，声音沉而稳。"

    $ hide_all_chars("captain_img")
    show captain_img at left with dissolve
    captain "男爵大人对格伦瓦德村的关心，十二年前就领教过了。"

    $ hide_all_chars()
    "空气冷了一瞬。男爵侧头看他，认出了他。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "雷恩。你还活着。看来老卡尔捡东西的习惯一直没改——什么都往家里捡。"

    $ hide_all_chars()
    "雷恩的下颌绷紧了，但他没有接话。你抬手，示意他退后。"
    "男爵重新看向你，声音里多了一层试探。"

    $ hide_all_chars("baron_img")
    show baron_img at left with dissolve
    baron "领主大人，你该清楚，你那座城刚挨了打，粮也短，兵也伤。我如今带着三百铁骑站在这里，是在帮你。你真要跟一个帮你的人翻脸？"

    $ mark_important_choice()
    menu:
        "正面示威——\"你的骑兵在我的村子里待够了。\"|需权力≥45 · 列阵封住隘口逼退铁骑" if power >= 45:
            $ baron_checked_early = True
            $ baron_clash_choice = "stand"
            $ change_stat("power", 5)
            $ change_stat("reputation", 4)
            $ change_stat("loyalty", 2)
            $ change_rel("rel_baron", -15)
            $ log_decision("第三章", "格伦瓦德对峙: 列阵封住隘口, 逼退男爵三百铁骑")
            hide baron_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "你的帮忙我心领了。不过艾登堡的事，艾登堡自己料理。请你的人在日落前退回边界。"

            $ hide_all_chars()
            "男爵脸上的笑淡了半分。"

            $ hide_all_chars("baron_img")
            show baron_img angry at left with dissolve
            baron "你有一百来人，要拦我三百铁骑？"

            $ hide_all_chars()
            "你没有答话。你转向雷恩，点了点头。"
            $ play_sound("audio/sfx/sword_draw.ogg")
            "雷恩立刻发出号令。你带来的步兵迅速展开，沿着隘口前的窄道列成三排枪阵，盾牌抵住两侧岩壁。这道口子不过三丈宽——铁骑在这里施展不开。"
            "男爵看着你的阵形，目光第一次变得认真。"
            "骑兵军官压低声音凑到男爵耳边。"

            $ hide_all_chars("soldier_generic_img")
            show soldier_generic_img at left with dissolve
            baron_officer "口子太窄，骑兵冲不开。硬打占不到便宜。"

            $ hide_all_chars()
            "男爵沉默了几息。远处传来盾牌撞击地面的闷响，你的士兵齐齐将枪尖压低，指向谷口。没有人喊口号，只有整齐的、冰冷的金属声。"

            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "有意思。"

            $ hide_all_chars()
            "他转身举手，骑兵开始收队。男爵翻身上马，居高临下看你。"

            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "你父亲不敢做的事，你做了。希望你也担得起后果。"

            $ hide_all_chars()
            $ play_sound("audio/sfx/horse_gallop.ogg")
            "铁骑从村中缓缓撤出，黑狼旗最后倒下。你站在原地没动，直到最后一骑消失在北面的山脊线上。"
            "雷恩走到你身侧，声音比平时低了几分。"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "他没有真打。下次不会这么客气了。"

        "计谋——\"男爵，咱们坐下来算一笔账。\"|需谋略≥40 · 不动刀让他退兵" if intrigue >= 40:
            $ baron_checked_early = True
            $ baron_clash_choice = "scheme"
            $ change_stat("intrigue", 5)
            $ change_stat("reputation", 3)
            $ change_rel("rel_baron", -10)
            $ log_decision("第三章", "格伦瓦德对峙: 以征粮清单串联北境三家小领主, 智退男爵")
            hide baron_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "男爵，你说是追剿匪徒，那匪徒呢？你三百骑追了几天，匪首的人头在哪里？"

            $ hide_all_chars()
            "男爵的笑容僵了一瞬。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我这里倒有些东西。"

            $ hide_all_chars()
            "你示意艾琳娜上前。她取出一卷文书展开——是男爵这两日在格伦瓦德征粮征马的详细清单，数目、时辰、哪家哪户，一笔不差。"

            $ hide_all_chars("elena_img")
            show elena_img at left with dissolve
            elena "同样的副本，今早已送往坎贝尔家、莫林家和瓦特家。三家的地也被你的骑兵踩过。"

            $ hide_all_chars()
            "男爵目光沉了下来。坎贝尔、莫林、瓦特——北境三个小领主，长年受他挤压。单个不足为虑，但如果被艾登堡串联起来，就是另一回事了。"

            if baron_is_darkflame_known:
                "你往前走了一步，压低声音，只有他能听见。"
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "男爵，焰火这种东西，暗处烧得旺，见了光就灭了。你说是不是？"
                $ hide_all_chars()
                "男爵的瞳孔微缩。他盯着你看了很长一息，脸上那种从容的傲慢头一次出现裂纹。"
            else:
                "你迎着他的目光，没有退让。"
                $ hide_all_chars("player_char_img")
                show player_char_img at left with dissolve
                player "我父亲或许不爱得罪邻居。但我年轻，不怕多几个朋友——也不怕少几个。"
                $ hide_all_chars()
                "男爵审视着你，像在重新估量什么。"

            "男爵沉默了一会儿，忽然笑了——这次的笑和之前不同。"

            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "你比你父亲有趣。"

            $ hide_all_chars()
            $ play_sound("audio/sfx/horse_gallop.ogg")
            "他转身上马，抬手下令撤队。经过那两辆粮车时顿了一下，最终没有带走。"

        "退让——\"我可以给你粮，换你退回边界。\"|以粮换退兵 · 财富- 声望- 忠诚-":
            $ baron_checked_early = False
            $ baron_clash_choice = "yield"
            $ change_stat("wealth", -8)
            $ change_stat("reputation", -6)
            $ change_stat("loyalty", -3)
            $ change_rel("rel_baron", 5)
            $ log_decision("第三章", "格伦瓦德对峙: 三十车粮十匹马换男爵退兵")
            hide baron_img
            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "我的城刚受过袭击，百姓需要安稳。如果粮食能让你退回边界，我可以给。"

            $ hide_all_chars()
            "男爵看了你一眼。那目光里有满意，也有一丝你不想细辨的东西——像是轻蔑，又像是失望。"

            $ hide_all_chars("baron_img")
            show baron_img happy at left with dissolve
            baron "痛快。我要五十车粮、三十匹驮马，够我的人回程嚼用。"

            $ hide_all_chars()
            "数目远超你预想。身后传来雷恩粗重的呼吸。你能感觉到你带来的士兵们在看你的背影。"

            $ hide_all_chars("player_char_img")
            show player_char_img at left with dissolve
            player "三十车粮，十匹马。边界以北的事你自己处理。"

            $ hide_all_chars()
            "男爵没有还价。他点了点头，像是一开始就只打算要这么多。"

            $ hide_all_chars("baron_img")
            show baron_img at left with dissolve
            baron "成交。"

            $ hide_all_chars()
            $ play_sound("audio/sfx/horse_gallop.ogg")
            "铁骑列队离开时，格伦瓦德村的村民站在屋檐下沉默地看着。粮车碾过冻土，发出沉闷的声响。没有人向你行礼。也没有人说话。"
            "雷恩走到你身后，欲言又止。最终他只说了一句。"

            $ hide_all_chars("captain_img")
            show captain_img at left with dissolve
            captain "老领主在世时，也有过这样的时候。"

            $ hide_all_chars()
            "你听不出这是安慰还是别的什么。"

    ## ── 收尾（三线共用） ──
    $ hide_all_chars()
    $ set_weather("clear")
    scene bg castle_exterior_dusk with dissolve
    "你带队回城。初冬的山路硬而滑，队伍走得很慢。艾登堡的轮廓在暮色里浮现时，外墙上新补的石块颜色比旧墙浅了一大片。"
    "艾琳娜策马跟上来，看着远处的城门。"

    $ hide_all_chars("elena_img")
    show elena_img at left with dissolve
    elena "格伦瓦德的事，三天之内北境各家都会知道。"

    $ hide_all_chars()
    "她没说这是好是坏。但你明白她的意思——不管你今天做了什么选择，从现在起，每一个北境领主都在掂量你的分量。"
    return
