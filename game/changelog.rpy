## ============================================================
## 更新日志 - Changelog
## changelog.rpy
## ============================================================

screen changelog_screen():
    tag menu
    use game_menu(_("更新日志"), scroll="viewport"):
        vbox:
            spacing 16

            ## 标题
            hbox:
                spacing 8
                text "【卷】" size 24 color "#d4a942" yalign 0.5
                text "更新日志" size 26 color "#d4a942" font "msyh.ttf"

            null height 8

            ## ── v3.18 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.18" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "文本终审 · 界面修复" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.07.11" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "文本终审" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 全篇旁白与台词终审一轮：删掉一百五十余处说教式收尾、格言腔和空洞比喻，把话还给人物和事" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 决战平衡完成全量推演验证：常规打法稳拿完胜，代价换来的惨胜只属于真正艰难的路" size 14 color "#c8b890" font "msyh.ttf"
                    null height 8
                    text "修复" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复同伴招募与名册界面、锻造界面在特定情况下报错的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复「臣服」结局尾声与北疆开场两处立绘缺失" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## ── v3.17 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.17" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "七近卫兑现 · 结局尾声 · 选项修缮" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.07.05" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "剧情兑现与结局" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 先王七近卫的下落全部收口——影卫、铁刺、暗焰三支的恩怨在正文与结局中交代完整" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 「臣服」「城破」两个结局补上完整尾声；八个结局的主要角色都有了自己的收场" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 雷恩、奥尔德里克、艾琳娜等人的性格弧线贯穿五章，不再前后脱节" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复：第五章战前答应与王子结盟后，这条线不再无疾而终——信使会来讨你的答复" size 14 color "#c8b890" font "msyh.ttf"
                    null height 8
                    text "选项修缮（感谢玩家指出）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 高属性专属选项以前总带半句解释，比别的选项长一截，等于把「选我」写在脸上——已全部剪平，选项好坏请自己判断" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 全篇旁白与台词再打磨近百处；片尾新增「玩家反馈」鸣谢名单" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## ── v3.16 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.16" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "建设入主线 · 结局收束 · 政治联姻" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.07.02" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "政治联姻线「盟约」" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 全新剧情线：北疆议会提亲（第三章）→ 王都会面（第四章）→ 婚约（第五章），与艾琳娜恋爱线互斥" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 英格丽在终章军议、决战前夜均有戏份；「议会的兵」在会战中真实兑现；五个结局各有联姻镜像 + 新成就「盟约联姻」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 提亲回信「先拖着」不再静默等同婉拒——北疆会有回应" size 14 color "#c8b890" font "msyh.ttf"
                    null height 8
                    text "城堡建设接入主线（玩家反馈：建设与游戏关联度不强）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 第二章新增建设工程与旱灾危机事件；一周目最多可建三座建筑" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 建筑真正改变剧情：粮仓可化解旱灾并支撑围城；诊所决定第三章瘟疫走向与伤兵存活；望楼提前预警敌军；学堂在王子夜谈与结局中回响" size 14 color "#c8b890" font "msyh.ttf"
                    null height 8
                    text "结局收束（玩家反馈：终选模糊 / 收尾仓促）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 毒药公爵新增完整尾声「公爵府的最后一冬」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 终章九个抉择的提示改为写明实际后果；决策前新增幕僚盘点；「加入男爵联军」有了专属的战场与结算文本" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 七个结局补齐雷恩、奥尔德里克、艾琳娜、暗百合等主要角色的下场；属性结算移至全部尾声之后，不再打断故事" size 14 color "#c8b890" font "msyh.ttf"
                    null height 8
                    text "选择深度与伏笔回收" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 39 处中期关键选项加入真实取舍与剧情走向差分" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 商会会长克劳斯的「这事没完」兑现；商人卡尔的复仇往事与结局归宿；世纪婚礼格雷伯爵后续；根卫暗记等十余处一次性钩子全部落地" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 全篇 200 余处旁白措辞修订；渗透调查加入成败判定；困难模式会战更具挑战；修正多处前后矛盾与重复揭示" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## ── v3.15 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.15" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "时间线 / 自述一致性修正" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.06.08" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "叙事时间线一致性（真相大白线玩家反馈）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 母亲画像「保留二十年」修正为「十五年」：母亲在主角七岁病逝，主角现二十二岁，应为十五年" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 艾琳娜往事去矛盾：删去「幼年被卖到城堡、老夫人收留教我识字」自述，改为从城堡老人处听闻老夫人——与第三章揭示的间谍身份（五年前王后派来、第四个任务）一致" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 队长雷恩跟随老领主年数统一为「十二年」，与其十二年前落难获救的往事吻合（此前主线说五年、第一/四章扩展说十五年，互相打架）" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## ── v3.14 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.14" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "AI 味第三轮清洗 + balance pass" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.05.18" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "AI 味清洗第三轮（打遍天下无敌手 4 星反馈）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 禁用清单扩 13 → 17 类，新加角色出戏 / 旁白说教 / 反派话太正确 / 抽象大词 / 选项均匀化 5 子类" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 全项目清洗 18 处（chapter1-5 主线 + interludes 章间 + ending 收尾）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 玩家审查直接抓的两条新规则：「躲」改「逃避」/「X 很 A，很 B」双形容词对仗删整句" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "属性 balance pass（洋溢 + 千品反馈持续推进）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· menu 属性锁批量加：17 → 131 处，6 大属性真的影响选项可见性" size 14 color "#c8b890" font "msyh.ttf"
                    text "· reputation 检定 1 → 14 处，不再是纯展示数值" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 检定阈值批量上调：低门槛 30/35/40 → 40/45/50（>=50 以上保留）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· chapter5 关键 menu 加配对扣减：谈判让步扣 power / 阴谋反间扣 reputation" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "bug 修复" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 修 3 处全锁 menu 保底（chapter4 王后税法 / chapter5 战后处置 / chapter3_expansion 暗百合）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 每个 menu 至少留 1 个无属性 condition 选项，防玩家属性不达标卡死" size 14 color "#c8b890" font "msyh.ttf"
                    text "· Måneskin 反馈：Elena 主线坦白事件闭合加 flag set，修森林夜话重复说秘密" size 14 color "#c8b890" font "msyh.ttf"

            null height 8

            ## ── v3.13 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.13" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "玩家反馈批量修复 + 平衡推进 + 系统优化" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.05.11" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "阿威克反馈（4 处全闭环）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 第一章加主角内心清点资源段（卫队 / 老管家 / 城堡 / 金鹰印戒），缓解「天崩开局」感" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第二章渡鸦旅店加武力路线钩子：高 power 玩家可雇佣兵长期签约" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第三章失踪事件加武力路线钩子：高 power 玩家可联合三家领主家臣 300 人搜山" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第二章艾琳娜首谈加 5 行内心独白：「她至少站在你这边」" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "阿巴阿巴反馈（主角带疤立绘）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 主角脸上的疤痕现已落实到立绘：第三章遇刺后自动切换「带疤版」（4 张表情变体）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· canon 终于在视觉层呈现（剧本明示已久但立绘未跟上）" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "终章节奏 + 戏剧深化" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 北城反馈「终章稍微有点赶了」：第五章最终选择后加共用「决定后的夜」呼吸段" size 14 color "#c8b890" font "msyh.ttf"
                    text "   大厅众人散去 → 主角独上城墙 → 陪伴分支 → 天明回大厅 → 进入结局" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第三章主教对峙加「起誓」第 4 选项（faith ≥ 30）：以艾登家纹章起誓换主教信任" size 14 color "#c8b890" font "msyh.ttf"
                    text "   成功拿到先王遗诏 + 主教好感大增；失败空手而归，证据链残缺" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "属性反馈感大幅提升（千品反馈持续推进）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 全章节新加 8 处属性专属 menu 选项（覆盖 6 stat × 阈值梯度 25-70）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 阴谋路线加 8 处属性扣减（伪装 / 暗中 / 反间 / 收买 / 监视盟友 等场景）" size 14 color "#c8b890" font "msyh.ttf"
                    text "   让阴谋手段有持续成本压力，不再「选什么都没代价」" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "艾琳娜路线深化（云反馈「满好感无视觉/感情线打磨」）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 高好感（rel_elena ≥ 80）或确认恋爱后，艾琳娜立绘自动切换「亲密版」" size 14 color "#c8b890" font "msyh.ttf"
                    text "   表情更柔和 + 眼神温和 + 脸颊微红，给玩家「她对你不一样了」的视觉反馈" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第四章花园握手后那夜加独处段：北方银带 / 走山路五天 / 一起回去看星空" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "其他打磨" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· AI 味金句清洗：清除多处对仗 / 升华式收尾旁白（保持沉浸感）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 跨作品 canon 一致性审核：管家年龄链 76 岁验证 + epilogue 年份 1352 确认" size 14 color "#c8b890" font "msyh.ttf"

            null height 8

            ## ── v3.12 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.12" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "玩家反馈修复 (月光疾风)" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.05.11" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "月光疾风反馈（1 处）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 真相结局加王后自请退位分支：rel_queen ≥ 50 + 王子同盟未叛时，王后" size 14 color "#c8b890" font "msyh.ttf"
                    text "   不再被公审，而是深夜与主角私下谈心后自请去修道院静修。" size 14 color "#c8b890" font "msyh.ttf"
                    text "   原反馈：「王后也不是十恶不赦之人，应该让她自己放下」" size 14 color "#c8b890" font "msyh.ttf"

            null height 8

            ## ── v3.11 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.11" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "玩家反馈批量修复 (栀子 + 北城)" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.05.10" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 栀子 batch 11
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "栀子热心玩家反馈修复（10 处）" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 救王子失败分支地点修正：从山林营地汇合，不再误说「爬出王宫」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 铁箱选项：主角拿走羊皮卷+印章+便笺，而非「看过即合上」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 艾琳娜亲密关系下的旁白改写：「这五年她都在你身边」（去除突兀用词）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 奥尔德里克报告：村庄请愿改为月夜祭奠老领主，不再是无下文悬念" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 民生优先选项分支生效：选了「亲自去村庄」后，章间不再重复报告" size 14 color "#c8b890" font "msyh.ttf"
                    text "· pacifist 隐藏成就 dead code 修复：加触发条件可正常解锁" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 主教/院长「念珠」→「祈祷珠」：西方教会用语统一" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 艾琳娜首次坦白时序：去除对玩家「已知间谍身份」的假设" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 奥尔德里克服务年数 50→近 40 年，年龄回到「七十多岁」：跨作品 canon (前传 1316 年 40 岁入门→ 1352 年 76 岁)" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修道院专长选择半年违和：加「贵族子弟破例提前」hand-wave 解释" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 北城 batch 6
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "北城反馈伏笔回收（6 处）" size 18 color "#1abc9c" font "msyh.ttf" bold True
                    null height 4
                    text "· 序章欺负主角的费利克斯：chapter2 格雷伯爵书摊段加子辈对比 cameo" size 14 color "#c8b890" font "msyh.ttf"
                    text "· Marcus 后续亮眼戏：chapter2 集市段扩展为暗中盯梢保护者" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 街头救济男孩重逢：chapter4 王都贫民区段「乌鸦」少年闭环" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 艾琳娜父亲死因：chapter5 重逢戏揭示——王宫文书撞见暮色之露被灭口" size 14 color "#c8b890" font "msyh.ttf"
                    text "· truth 结局艾琳娜 closure：5 年后核对受害者名单，给「真相能给人的交代」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 暮色之露下毒最后一环：chapter3 揭示酒窖管事汉斯（已灭口）" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 千品 batch 9 (balance pass 部分)
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "声望条件 menu（5 处新增，回应「reputation 几乎纯装饰」）" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 第四章 格雷伯爵书摊（声望≥60）：以平等姿态回应——你的名声已传到王都" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第四章 王后觐见（声望≥60）：以领地民望做担保——王后给额外奖励" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第四章 王都宴会（声望≥50）：以名声做姿态——让大厅的人围过来听你的故事" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第五章 战前动员（声望≥60）：亲自巡视——声望本身就是力量（防御加成 +4）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 治理-高税事件（声望≥50）：亲自下村——以民望让百姓自愿撑过这段" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 完整 balance pass（属性扣减 / menu 锁 60+ / 阈值上调 / UI 飘字）下版陆续上" size 13 color "#8a7e60" font "msyh.ttf" italic True

            null height 16

            ## ── v3.10 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.10" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "角色死亡状态一致性审计" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.31" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 暗百合死亡状态
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "暗百合被摧毁后的「复活」修复（10处）" size 18 color "#e74c3c" font "msyh.ttf" bold True
                    null height 4
                    text "· 第四章：地图标注、章末旁白不再无条件提及暗百合据点和暗处注视" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第四章：王后对话新增已摧毁分支——「被你铲除的叛逆分子」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第四章扩展：灰区暗百合标记新增已摧毁分支——「旧标记，余党还没来得及清理」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第五章：Elena列举势力、地图描述、战局旁白不再无条件提及暗百合" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 幕间：驿站老板暗百合涂鸦传闻新增已摧毁分支" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 随机事件：丰收节传单不再硬编码暗百合标记，改为通用可疑人物" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 同伴系统：暗百合密探「影」在组织被摧毁后不再可招募" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 弗雷德里克王子
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "弗雷德里克王子背叛后的「复活」修复（3处）" size 18 color "#f39c12" font "msyh.ttf" bold True
                    null height 4
                    text "· 真相结局尾声：被背叛时写信对象改为「摄政议会」而非「弗雷德里克国王」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 真相结局审判：判决交给「摄政议会」而非「弗雷德里克国王」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 影之王结局：新增prince_betrayed专属分支——背叛叙述而非「他以为你是朋友」" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.9 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.9" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "死旗激活 & 叙事补强" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.31" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 死旗激活
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "死旗激活（设而未检的flag全面启用）" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 第五章议事厅：奥尔德里克请战、队长重申誓约、艾琳娜私下嘱令、主教全力支持等条件对话" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第五章扩展：主教献出教会老兵、艾琳娜汇报敌军补给弱点、密道引导加成、百合双面间谍情报" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 第五章扩展：新增「用把柄反威胁男爵」菜单选项（需baron_blackmail_option）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 结局篇：队长回忆五年前誓言、王后最终处置分支、男爵命运分支、百合双面遗产、奥尔德里克老兵回忆" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 共激活11个死旗，新增1个条件菜单选项，所有触发均为if条件包裹，不影响原有流程" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 叙事补强
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "叙事一致性补强" size 18 color "#f39c12" font "msyh.ttf" bold True
                    null height 4
                    text "· 补强父亲身份：序章暗示先王对父亲的特殊信任，第一章老兵旁证「国王交给最信得过的人」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 补强男爵低爵：海因里希解释男爵故意不升爵——「男爵养私兵没人管，伯爵养私兵就是威胁」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 补强兵力叙事：奥尔德里克与主角确立「以小博大」战略定调——这点人守不住城，但能守住秘密" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 补强男爵双面身份：艾琳娜详述暗焰从王后情报网到反叛工具的演变——「暗焰是手段，反叛才是目的」" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.8 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.8" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "叙事矛盾全面梳理修复（第二批）" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.26" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 直接矛盾修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "直接矛盾修复" size 18 color "#e74c3c" font "msyh.ttf" bold True
                    null height 4
                    text "· 统一父亲发现艾琳娜身份时间：百合首领「三年」修正为「不到三个月」（与艾琳娜本人说法一致）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 统一队长来历：「父亲派小队偷袭地牢」修正为「鞭刑五十后流放，巡逻队在野外发现」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正队长回忆时间：「十二年前先王还在世」→「二十多年前」（先王二十年前驾崩）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正密道修建时长：「花了十年」→「花了好几年」（第十五年开始修，只剩五年）" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 叙事重复清理
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "叙事重复清理" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 艾琳娜身世从重复5次缩减为1次完整+4次简短引用（第4/5章深度对话、NPC支线）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 主教「伪善者」对话、「信徒被卖给王后」对话、「遗诏摄政人选」对话各去除重复段落" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 逻辑一致性
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "逻辑一致性修正" size 18 color "#f39c12" font "msyh.ttf" bold True
                    null height 4
                    text "· 双重/三重间谍回退修复：三重身份揭示后不再退回说「双重间谍」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 统一暗百合历史为「两百年」：「上百年」→「两百年」，「王国建立之初」→「两百多年」，「比王国还古老」→「和王国一样古老」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 施泰因伯爵夫人丈夫去世时间：早期对话去掉「去年」，改用模糊时间「在南方战役中战死」" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.7 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94220")
                hbox:
                    spacing 8
                    text "v3.7" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "CG跳过崩溃修复" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.25" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "崩溃修复" size 18 color "#e74c3c" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复第二至五章过场动画点击「跳过」后退回主菜单的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 根本原因：跳过函数调用 renpy.return_statement() 在 jump 进入的章节里落点错误" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复方式：改用 renpy.dismiss() 驱散暂停，各 cinematic label 自行检测跳过标志并自然返回" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.6 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94215")
                hbox:
                    spacing 8
                    text "v3.6" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "属性系统重构 & 好感度系统重做" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.25" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 属性系统重构
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "属性系统重构（布兰特设计哲学）" size 18 color "#f39c12" font "msyh.ttf" bold True
                    null height 4
                    text "· 引入五段阶位系统：每属性分5阶，每阶有专属名称与颜色（如「铁腕领主」「腹黑帝王」）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 阶位突破叙事弹窗：升阶/降阶时弹出专属文字，反映世界对你改变的反应" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 骰子判定系统：危机检定改为 1d10 + 属性加成 vs 难度，结果分大成功/成功/失败/大失败" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 路线印记系统：铁血/谋士/圣光/外交四条路线，积累3枚印记激活专属路线" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 高属性双面代价：权力/谋略/财富/信仰达到80时触发一次性负面事件" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 全局增益缩放（×0.4）：属性成长节奏更合理，专注某一属性需要跨越多章才能达顶" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 好感度系统重做
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "好感度系统重做" size 18 color "#e91e8c" font "msyh.ttf" bold True
                    null height 4
                    text "· 阈值突破弹窗：关系越过敌视/警惕/中立/友善/信任节点时弹出后果说明" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 章节被动效果：每章开头根据各NPC好感度自动应用属性加成/惩罚" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 奥尔德里克（信任）→ 谋略+4 / 深度敌对 → 谋略-4、声望-3" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 队长雷恩（信任）→ 权力+3、忠诚+3 / 深度敌对 → 权力-4、忠诚-4" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 主教马修斯（信任）→ 信仰+4、声望+3 / 深度敌对 → 信仰-5、声望-4" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 艾琳娜、冯·哈根男爵、伊莎贝拉王后亦有各自专属被动效果" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 章节开头汇总面板：清晰展示本章受哪些NPC关系影响及具体数值" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.5 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94215")
                hbox:
                    spacing 8
                    text "v3.5" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "叙事一致性全面修正" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.24" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 崩溃修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "崩溃修复" size 18 color "#e74c3c" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复第一章深化剧情结尾 AttributeError：rel_elena 属性引用错误导致崩溃" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 叙事一致性修正
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "叙事一致性修正" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 统一雷恩跟随年数：第四章扩展「二十年」修正为「十五年」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正管家奥尔德里克服务年数：「四十年」→「三十余年」，与主线三十年描述一致" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正结局中管家年龄：「七十岁」→「六十五岁」（十五岁入门五十年后）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正结局中管家台词：「跟了费雷恩大人」→「跟了您的父亲」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正父亲治理年数：「四十年」→「近三十年」（符合 1298-1347 时间线）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正费雷恩复活漏洞：第三章「已经死了二十年」→「早已秘密去世」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正第四章扩展情报「大主教费雷恩来王都」→「大主教马修斯来王都」" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 明确影月草与暮色之露的关系：影月草为原料，暮色之露为提炼毒药" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 扩充暮色之露描述：「数月才致命」补充为「数月乃至数年，剂量越低越难察觉」" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.4 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94215")
                hbox:
                    spacing 8
                    text "v3.4" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "剧情重复修复 & 体验优化" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.22" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 剧情修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "剧情逻辑修复" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复主教教堂场景中「西里尔」与王子老师重名造成玩家混淆的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复遗诏剧情在同一章中重复出现两次的问题（主教正式告白 & 醉酒忏悔）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 已知信息不再重复解释：若玩家已从其他途径得知遗诏真相，对话自动调整" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 体验优化
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "操作体验优化" size 18 color "#27ae60" font "msyh.ttf" bold True
                    null height 4
                    text "· 手机端快捷栏新增「快进」按钮，支持快速跳过已读剧情" size 14 color "#c8b890" font "msyh.ttf"

            null height 12

            ## ── v3.3 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94215")
                hbox:
                    spacing 8
                    text "v3.3" size 22 color "#d4a942" font "msyh.ttf" bold True yalign 0.5
                    text "大规模Bug修复 & 平衡性调整" size 16 color "#c8b890" font "msyh.ttf" yalign 0.5
                    text "2026.03.21" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## 崩溃/UI修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "崩溃与UI修复" size 18 color "#e74c3c" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复背包界面打开后返回游戏卡死/闪退的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复队伍管理界面关闭后游戏无响应的问题（tag menu冲突）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复商店界面关闭需要双击的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 背包/队伍/商店界面现在可以点击暗色遮罩区域直接关闭" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复第一章深化剧情结尾闪退崩溃的问题（属性引用错误）" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 剧情逻辑修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "剧情逻辑修复" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复第三章扩展剧情在危机高潮之后才播放，导致时间线错乱的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复第二章奥尔德里克勋章故事重复播放两次的问题（秘密揭示→徽章传承顺序颠倒）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复暗百合首领人设矛盾：统一为女性首领「影」，铁刺派艾德蒙改为分裂势力头目" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复深化仪式场景中暗百合首领性别与主线不一致的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复密道逻辑漏洞：前期选择不告诉任何人，后续不再无条件提及密道" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复已加入暗百合后仪式场景仍询问是否加入的矛盾" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 立绘修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "立绘显示修复" size 18 color "#9b59b6" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复结局中暗百合首领立绘因tag不匹配无法正常隐藏的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复多处角色立绘在同一位置重叠的问题（第四章王子/第五章艾琳娜/序章马库斯）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复NPC支线中奥尔德里克立绘闪烁及村长立绘残留的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复深化场景中hide对象错误导致艾琳娜立绘未正确隐藏的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复第五章王后立绘连续show两次导致闪烁的问题" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 平衡性
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "平衡性调整" size 18 color "#f39c12" font "msyh.ttf" bold True
                    null height 4
                    text "· 大幅调整属性分配：谋略(intrigue)不再独占大部分选项奖励" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 勇敢/果断的行动现在提升武力而非谋略" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 信任/联盟/感情类选项现在提升忠诚而非谋略" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 观察/学术/调查类选项现在提升声望而非谋略" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 信仰/道德/信念类选项现在提升信仰而非谋略" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 同一菜单的多个选项不再全部给予相同属性，鼓励多样化选择" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 削减序章中过高的单次属性增量（+10→+5）" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 其他
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "其他改进" size 18 color "#2ecc71" font "msyh.ttf" bold True
                    null height 4
                    text "· 收藏品系统现在读档重玩时也会显示提示（标注「已收集」）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 感谢TapTap社区玩家的详细反馈！" size 14 color "#d4a942" font "msyh.ttf"

            null height 16

            ## ── v3.2 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94210")
                hbox:
                    spacing 8
                    text "v3.2" size 22 color "#8a7e60" font "msyh.ttf" bold True yalign 0.5
                    text "剧情修正 & Bug修复版" size 16 color "#6a5e48" font "msyh.ttf" yalign 0.5
                    text "2026.03.20" size 13 color "#6a5e48" xalign 1.0 yalign 0.5

            ## Bug修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "Bug修复" size 18 color "#2ecc71" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复同伴管理界面选择/装备/解散操作后游戏卡死的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复决策日志不随存档保存，读档后显示错误记录的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复部分属性变化（幕间/NPC支线/治理）不显示通知弹窗的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复第二章扩展内容（领主会议）大部分场景没有背景音乐的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复平衡调试面板操作后界面卡死的问题" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 剧情修正
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "剧情修正" size 18 color "#3498db" font "msyh.ttf" bold True
                    null height 4
                    text "· 统一先王驾崩时间线（全部修正为二十年前）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 统一艾琳娜身世（没落贵族→侍女学院→间谍→双重间谍）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正管家奥尔德里克讲述先王之死时两段叙事自相矛盾的问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 统一管家服务年限（三十年）" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正遗诏伪造者身份：王后策划，大主教费雷恩执行" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正原始遗诏内容：指定主角父亲为唯一摄政者" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修正队长雷恩服务年限、格伦瓦德村人口、北境入侵时间线" size 14 color "#c8b890" font "msyh.ttf"

            null height 4

            ## 流程修复
            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152820")
                vbox:
                    spacing 6
                    text "流程修复" size 18 color "#e67e22" font "msyh.ttf" bold True
                    null height 4
                    text "· 修复第二章领主大会闭幕日在开幕前播放的时间线倒置问题" size 14 color "#c8b890" font "msyh.ttf"
                    text "· 修复第五章战争会议重复（相同情报简报讲两遍）的问题" size 14 color "#c8b890" font "msyh.ttf"

            null height 16

            ## ── v3.1 ──
            frame:
                xfill True
                xpadding 16
                ypadding 10
                background Solid("#d4a94210")
                hbox:
                    spacing 8
                    text "v3.1" size 22 color "#8a7e60" font "msyh.ttf" bold True yalign 0.5
                    text "最终定稿版" size 16 color "#6a5e48" font "msyh.ttf" yalign 0.5

            frame:
                xfill True
                xpadding 20
                ypadding 12
                background Solid("#1a152815")
                vbox:
                    spacing 6
                    text "· 五章完整剧情，35万字" size 14 color "#8a7e60" font "msyh.ttf"
                    text "· 六维属性系统 + 角色好感度" size 14 color "#8a7e60" font "msyh.ttf"
                    text "· 五个独特结局 + 隐藏结局" size 14 color "#8a7e60" font "msyh.ttf"
                    text "· NPC深度支线、同伴系统、制作系统、治理系统" size 14 color "#8a7e60" font "msyh.ttf"
                    text "· 画廊、音乐室、成就、章节选择" size 14 color "#8a7e60" font "msyh.ttf"
                    text "· New Game+ 与隐藏成就" size 14 color "#8a7e60" font "msyh.ttf"

            null height 16

            ## 底部
            frame:
                xalign 0.5
                xpadding 24
                ypadding 12
                background Solid("#1a152840")
                text "感谢每一位玩家的反馈，让权谋之庭变得更好" size 14 color "#8a7e60" font "msyh.ttf"
