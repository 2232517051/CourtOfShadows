# 《权谋之庭》门控改造 — 仓库硬数据扫描

扫描对象: `E:\Projects\renpy-8.5.2-sdk\CourtOfShadows\game\*.rpy`(Ren'Py 8.5)。
扫描时间: 2026-07-26。用途: 「属性不够选项隐藏 → 可见但走失败分支」改造 + 危机判定语境修正。

属性变量名(characters.rpy:115-134 定义, 含初始值): power=30(权力) / intrigue=20(谋略) / faith=50(信仰) / wealth=40(财富) / reputation=40(声望) / loyalty=50(忠诚); courage=50, max_courage=100(勇气)。

---

## 一、门控点全量清单(118 个选项行 / 120 个属性条件)

匹配模式: menu 选项行 `"选项文本" if <条件含 属性 >= 阈值>:`。两行含双属性条件(chapter5.rpy:2800、southern_expansion.rpy:1110), 故 120 个条件落在 118 行上。

**勇气(courage)没有任何 menu 选项门控**——勇气门控只存在一处: crisis.rpy:236 危机界面的「迎接挑战」按钮(`has_courage(crisis_courage_cost)`, 不足时变灰显示「需要 X 勇气」, 见第二节)。这本身已是「可见但不可选」的现成范式。

| 文件 | 行号 | 所在章节 | 属性 | 阈值 | 选项文本 |
|---|---|---|---|---|---|
| chapter1_deepening.rpy | 452 | 第一章 | 声望(reputation) | ≥50 | 派使者去克雷恩家明面交涉——亮家名压人 |
| chapter1_deepening.rpy | 705 | 第一章 | 忠诚(loyalty) | ≥50 | 叫村里其他养羊户作证——这种事不止你们两家 |
| chapter1_deepening.rpy | 832 | 第一章 | 财富(wealth) | ≥50 | 自掏腰包付面包钱+给少年安排工作 |
| chapter1_expansion.rpy | 384 | 第一章 | 谋略(intrigue) | ≥50 | 下令调出父亲遇袭那夜的卷宗——你要从头查这件事 |
| chapter1_expansion.rpy | 505 | 第一章 | 声望(reputation) | ≥25 | 等她离开后，在她房门口留一张纸条 |
| chapter1_expansion.rpy | 720 | 第一章 | 财富(wealth) | ≥50 | 雇一支佣兵团代打——你出钱, 他们出血 |
| chapter2.rpy | 241 | 第二章 | 谋略(intrigue) | ≥25 | 仔细研究每位领主的底细 |
| chapter2.rpy | 518 | 第二章 | 财富(wealth) | ≥50 | 买下他们这趟运的全部货 |
| chapter2.rpy | 664 | 第二章 | 权力(power) | ≥25 | 私下找佣兵头领谈雇佣 |
| chapter2.rpy | 1325 | 第二章 | 财富(wealth) | ≥50 | 主动谈酒生意 |
| chapter2.rpy | 2448 | 第二章 | 财富(wealth) | ≥50 | 付钱 |
| chapter2.rpy | 2665 | 第二章 | 忠诚(loyalty) | ≥50 | 派艾琳娜带两个民兵截在南门外 |
| chapter2.rpy | 3427 | 第二章 | 谋略(intrigue) | ≥45 | 追问——「关于一切，是什么意思？」 ‡ |
| chapter3.rpy | 202 | 第三章 | 权力(power) | ≥50 | 召集附近领主家臣联合搜山 |
| chapter3.rpy | 278 | 第三章 | 谋略(intrigue) | ≥45 | 先不管失踪的事，调查符号的来源 |
| chapter3.rpy | 403 | 第三章 | 声望(reputation) | ≥50 | 召集所有铁匠樵夫家属当众发誓 |
| chapter3.rpy | 481 | 第三章 | 权力(power) | ≥55 | 命令雷恩立刻搜索森林 |
| chapter3.rpy | 657 | 第三章 | 谋略(intrigue) | ≥45 | 保持沉默，让奥尔德里克继续说 |
| chapter3.rpy | 793 | 第三章 | 权力(power) | ≥60 | 亲自带剑去——让他知道艾登堡不怕硬碰硬 |
| chapter3.rpy | 806 | 第三章 | 权力(power) | ≥55 | 拒绝，并警告男爵管好自己的事 |
| chapter3.rpy | 812 | 第三章 | 谋略(intrigue) | ≥45 | 接受邀请——借机探查男爵的意图 |
| chapter3.rpy | 867 | 第三章 | 谋略(intrigue) | ≥45 | 假装没看见，但暗中让人跟踪他 |
| chapter3.rpy | 1197 | 第三章 | 谋略(intrigue) | ≥60 | 回想父亲日记里的暗号系统 |
| chapter3.rpy | 1369 | 第三章 | 谋略(intrigue) | ≥45 | 走右边——那边有微弱的光线 |
| chapter3.rpy | 1448 | 第三章 | 谋略(intrigue) | ≥70 | 什么都不出示——直接报出几个内部暗号 |
| chapter3.rpy | 1472 | 第三章 | 谋略(intrigue) | ≥45 | 出示在密道中找到的银质徽章 |
| chapter3.rpy | 1635 | 第三章 | 权力(power) | ≥55 | 拒绝喝 |
| chapter3.rpy | 2257 | 第三章 | 谋略(intrigue) | ≥45 | 走右边——追踪脚印 |
| chapter3.rpy | 2946 | 第三章 | 谋略(intrigue) | ≥60 | 提议合作而非加入，互不臣属 |
| chapter3.rpy | 3049 | 第三章 | 权力(power) | ≥65 | 加入铁刺 |
| chapter3.rpy | 3101 | 第三章 | 权力(power) | ≥60 | 摧毁暗百合 |
| chapter3.rpy | 3351 | 第三章 | 谋略(intrigue) | ≥45 | 交出你掌握的所有情报——这是你唯一的出路 |
| chapter3.rpy | 3367 | 第三章 | 忠诚(loyalty) | ≥55 | 看在父亲的份上——我给你一次机会 |
| chapter3.rpy | 3600 | 第三章 | 谋略(intrigue) | ≥45 | 证明你的忠诚——告诉我王后在策划什么 |
| chapter3.rpy | 3637 | 第三章 | 忠诚(loyalty) | ≥55 | 我相信你——父亲信任你，我也选择信任 |
| chapter3.rpy | 3815 | 第三章 | 谋略(intrigue) | ≥45 | 这些情报有多可靠？证明你的价值 |
| chapter3.rpy | 3834 | 第三章 | 忠诚(loyalty) | ≥55 | 父亲信任你的判断——我尊重他的选择 |
| chapter3.rpy | 4213 | 第三章 | 谋略(intrigue) | ≥45 | 先做好充分准备再去找他 |
| chapter3.rpy | 4295 | 第三章 | 权力(power) | ≥55 | 威逼——'如果你不合作，我会公开教会的丑闻' |
| chapter3.rpy | 4361 | 第三章 | 信仰(faith) | ≥50 | 起誓——以艾登家纹章起誓教会一切受我保护 |
| chapter3.rpy | 4596 | 第三章 | 忠诚(loyalty) | ≥60 | 为他设一条退路——以艾登堡的名义保他余生 |
| chapter3.rpy | 4630 | 第三章 | 信仰(faith) | ≥58 | 表示理解——'你也是受害者' |
| chapter3.rpy | 4959 | 第三章 | 谋略(intrigue) | ≥45 | 主动出击——收集更多证据，联合盟友，在适当的时候公开真相 |
| chapter3.rpy | 4995 | 第三章 | 权力(power) | ≥55 | 防守为主——加强领地防御，等待对方露出破绽 |
| chapter3.rpy | 5285 | 第三章 | 谋略(intrigue) | ≥45 | 今晚就把盒子转移走 |
| chapter3.rpy | 5687 | 第三章 | 权力(power) | ≥60 | 全力防守——死守城堡 |
| chapter3.rpy | 5764 | 第三章 | 权力(power) | ≥65 | 主动出击——在他们完成包围之前冲出去 |
| chapter3_expansion.rpy | 111 | 第三章 | 谋略(intrigue) | ≥45 | 渗透路线「化暗为明」 |
| chapter3_expansion.rpy | 201 | 第三章 | 声望(reputation) | ≥45 | 联合三位领主共同调查 |
| chapter3_expansion.rpy | 279 | 第三章 | 权力(power) | ≥45 | 直接冲入「速战速决」 |
| chapter3_expansion.rpy | 365 | 第三章 | 谋略(intrigue) | ≥45 | 主动接近「套取情报」 |
| chapter3_expansion.rpy | 627 | 第三章 | 权力(power) | ≥45 | 独自前往「只有一个人才能看到真相」 |
| chapter3_expansion.rpy | 687 | 第三章 | 声望(reputation) | ≥45 | 仔细搜查遗迹「寻找更多线索」 |
| chapter3_expansion.rpy | 704 | 第三章 | 信仰(faith) | ≥45 | 在祭坛前冥想「感受这个地方的力量」 |
| chapter3_expansion.rpy | 868 | 第三章 | 谋略(intrigue) | ≥45 | 请教更多关于毒药的知识 |
| chapter3_expansion.rpy | 1085 | 第三章 | 谋略(intrigue) | ≥55 | 继续潜伏「获取更多情报」 |
| chapter3_expansion.rpy | 1117 | 第三章 | 谋略(intrigue) | ≥45 | 趁乱留下记号「标记几个关键人物」 |
| chapter3_expansion.rpy | 1259 | 第三章 | 声望(reputation) | ≥55 | 政治手段「向王廷举报」 |
| chapter3_expansion.rpy | 1304 | 第三章 | 谋略(intrigue) | ≥58 | 谈判策略「分化瓦解暗百合」 |
| chapter3_expansion.rpy | 1357 | 第三章 | 谋略(intrigue) | ≥60 | 暗中接管「取代首领的位置」 |
| chapter4.rpy | 270 | 第四章 | 谋略(intrigue) | ≥45 | 问她王都有哪些值得注意的人物 |
| chapter4.rpy | 551 | 第四章 | 财富(wealth) | ≥50 | 塞几枚银币让驿站管事「忘记」我们路过 |
| chapter4.rpy | 1038 | 第四章 | 声望(reputation) | ≥60 | 以平等姿态回应——你的名声已传到王都 |
| chapter4.rpy | 1078 | 第四章 | 谋略(intrigue) | ≥45 | 直接问他觐见时需要注意什么 |
| chapter4.rpy | 1301 | 第四章 | 声望(reputation) | ≥60 | 以领地民望做担保——你已名声在外 |
| chapter4.rpy | 1388 | 第四章 | 权力(power) | ≥55 | 坚持立场——税法确实不合理 |
| chapter4.rpy | 1429 | 第四章 | 谋略(intrigue) | ≥50 | 动用情报网——不解释，反将一军 ‡ |
| chapter4.rpy | 1507 | 第四章 | 谋略(intrigue) | ≥50 | 反问——『也许陛下比我更清楚？』 |
| chapter4.rpy | 1699 | 第四章 | 谋略(intrigue) | ≥45 | 直接问他关于父亲的事 |
| chapter4.rpy | 1729 | 第四章 | 声望(reputation) | ≥50 | 以名声做姿态——主动向众人致意 |
| chapter4.rpy | 2172 | 第四章 | 信仰(faith) | ≥50 | 找教会档案员私下打听先王临终圣礼 |
| chapter4.rpy | 2232 | 第四章 | 谋略(intrigue) | ≥45 | 查找父亲在王都的活动记录 |
| chapter4.rpy | 2240 | 第四章 | 谋略(intrigue) | ≥58 | 寻找先王遗诏的相关文件 |
| chapter4.rpy | 2729 | 第四章 | 谋略(intrigue) | ≥45 | 记住内容后烧掉信件——太危险了 |
| chapter4.rpy | 2847 | 第四章 | 权力(power) | ≥55 | 冒险营救王子 |
| chapter4.rpy | 3127 | 第四章 | 谋略(intrigue) | ≥45 | 让艾琳娜想办法悄悄绕过 |
| chapter4.rpy | 3633 | 第四章 | 信仰(faith) | ≥40 | 请教会公开站到你这边——与马修斯结盟 ‡ |
| chapter4_expansion.rpy | 407 | 第四章 | 财富(wealth) | ≥60 | 推一袋金币过去——「告诉我你今天没说完的那部分」 |
| chapter4_expansion.rpy | 600 | 第四章 | 信仰(faith) | ≥45 | 在教堂中祈祷，感受氛围 |
| chapter4_expansion.rpy | 1028 | 第四章 | 谋略(intrigue) | ≥70 | 反问她——「您见过他几面，怎么这么了解我父亲？」 |
| chapter4_prince.rpy | 345 | 第五章·王子支线 | 谋略(intrigue) | ≥60 | 不回信——信使可能被跟踪 |
| chapter5.rpy | 634 | 第五章 | 权力(power) | ≥50 | 当面拒绝并让卫兵把他赶出去 |
| chapter5.rpy | 841 | 第五章 | 权力(power) | ≥70 | 亲自指挥北墙改造 |
| chapter5.rpy | 942 | 第五章 | 财富(wealth) | ≥60 | 拿一半金库银币给战死者家属预付抚恤金 |
| chapter5.rpy | 984 | 第五章 | 财富(wealth) | ≥45 | 节省开支，准备长期消耗 |
| chapter5.rpy | 1033 | 第五章 | 声望(reputation) | ≥40 | 下城楼，亲自帮老人搬一块石头 |
| chapter5.rpy | 1049 | 第五章 | 忠诚(loyalty) | ≥40 | 去铁匠铺，给打了一夜的老铁匠送一壶水 |
| chapter5.rpy | 1067 | 第五章 | 谋略(intrigue) | ≥40 | 回书房，把昨晚没看完的舆图研究完 |
| chapter5.rpy | 1191 | 第五章 | 忠诚(loyalty) | ≥60 | 亲自走遍城堡每一处——你要的是「人都看见过你」 |
| chapter5.rpy | 1856 | 第五章 | 财富(wealth) | ≥50 | 把财库所有应急金分给士兵 |
| chapter5.rpy | 2309 | 第五章 | 谋略(intrigue) | ≥70 | 用毒药清理一切——以母亲的方式收尾\|不动刀兵，用「暮色之露」逐一清场 → 毒药公爵 ‡ |
| chapter5.rpy | 2482 | 第五章·结局段 | 信仰(faith) | ≥60 | 祈祷夜——以信仰为全军点一夜的火 |
| chapter5.rpy | 2535 | 第五章·结局段 | 财富(wealth) | ≥40 | 收买雇佣兵——瓦解敌军内部\|需财富≥40 · 战场上获得内应 |
| chapter5.rpy | 2554 | 第五章·结局段 | 权力(power) | ≥55 | 山路绕后——前后夹击\|需权力≥55 · 战术优势 |
| chapter5.rpy | 2694 | 第五章·结局段 | 忠诚(loyalty) | ≥70 | 亲自跪在老人面前——以你的名义起誓重建 |
| chapter5.rpy | 2760 | 第五章·结局段 | 权力(power) | ≥60 | 正面强攻，以气势压倒对方\|需权力≥60 |
| chapter5.rpy | 2779 | 第五章·结局段 | 谋略(intrigue) | ≥55 | 采用迂回战术，先攻击敌军侧翼\|需谋略≥55 |
| chapter5.rpy | 2800 | 第五章·结局段 | 谋略(intrigue)、忠诚(loyalty) | ≥45、≥50 | 先防御，等待敌军露出破绽再反击\|需谋略≥45 · 忠诚≥50 ‡ |
| chapter5.rpy | 2853 | 第五章·结局段 | 谋略(intrigue) | ≥60 | 用早就埋下的反间——让他们的右翼调头攻自己人 |
| chapter5.rpy | 3092 | 第五章·结局段 | 权力(power) | ≥55 | 杀鸡儆猴——处决首恶，释放士兵\|权力+ 声望- 威慑四方 |
| chapter5.rpy | 3104 | 第五章·结局段 | 权力(power) | ≥60 | 吞并领地——将战败方纳入版图\|权力+ 财富+ 管理压力大 |
| chapter5.rpy | 4034 | 第五章 | 信仰(faith) | ≥55 | 用教会的权威压住双方 |
| chapter5.rpy | 4092 | 第五章 | 信仰(faith) | ≥58 | 以信仰为突破口 |
| chapter5.rpy | 4868 | 第五章·结局段 | 信仰(faith) | ≥55 | 用道义压力迫使真相浮出水面 |
| chapter5.rpy | 5035 | 第五章·结局段 | 谋略(intrigue) | ≥45 | 提出谈判——给她一条体面的退路 |
| chapter5.rpy | 5080 | 第五章·结局段 | 谋略(intrigue) | ≥60 | 动用整张情报网——把附和者的底册当场摊开\|烧掉多年暗线，换一场干净的胜利 |
| chapter5_expansion.rpy | 322 | 第五章 | 信仰(faith) | ≥50 | 外交斡旋——以谈判化解战争 ‡ |
| chapter5_expansion.rpy | 430 | 第五章 | 声望(reputation) | ≥60 | 亲自巡视——你的声望本身就是力量 |
| chapter5_expansion.rpy | 2275 | 第五章 | 信仰(faith) | ≥60 | 圣盾阵——以教会之名化解敌意 ‡ |
| chapter5_expansion.rpy | 2309 | 第五章 | 忠诚(loyalty) | ≥60 | 民堡阵——全民皆兵，守护家园 |
| governance.rpy | 484 | 内政系统(跨章) | 声望(reputation) | ≥50 | 亲自下村——以民望让百姓自愿撑过这段 |
| governance.rpy | 717 | 内政系统(跨章) | 忠诚(loyalty) | ≥60 | 亲自下村组织自救——你的话能让百姓愿意撑 |
| governance.rpy | 1489 | 内政系统(跨章) | 信仰(faith) | ≥60 | 亲自带教会修士进疫区祷告 + 救治——你的虔信能稳住人心 |
| npc_sidelines.rpy | 841 | NPC支线(跨章) | 信仰(faith) | ≥60 | 为他赦罪——以你能给的全部虔信 |
| southern_expansion.rpy | 602 | 南境扩展(跨章) | 谋略(intrigue) | ≥45 | 试探：是不是有人在背后推着两边斗？（谋略） ‡ |
| southern_expansion.rpy | 1110 | 南境扩展(跨章) | 谋略(intrigue)、声望(reputation) | ≥35、≥40 | 都不站——把两边按在一张桌子上谈 ‡ |
| southern_expansion.rpy | 1438 | 南境扩展(跨章) | 谋略(intrigue) | ≥40 | 智取——不靠人多，单凭证据和谋略，反将王廷一军 ‡ |
| southern_expansion.rpy | 1446 | 南境扩展(跨章) | 声望(reputation) | ≥45 | 代潮汐港向王廷请附——归顺王廷，换一纸自治诏书 ‡ |

‡ = 复合条件(属性只是条件之一, 完整条件见源码), 共 11 处:

- chapter2.rpy:3427 — `if (intrigue >= 45 or rel_aldric >= 50) and not father_was_regent_known:`
- chapter4.rpy:1429 — `if eagle_intel and intrigue >= 50:`
- chapter4.rpy:3633 — `if faith >= 40 and not lily_full_member:`
- chapter5.rpy:2309 — `if deep_mother_herb == "poison" and intrigue >= 70 and poison_evidence:`
- chapter5.rpy:2800 — `if intrigue >= 45 and loyalty >= 50:`
- chapter5_expansion.rpy:322 — `if alliance_church or faith >= 50:`
- chapter5_expansion.rpy:2275 — `if alliance_church or faith >= 60:`
- southern_expansion.rpy:602 — `if broker_rumor_heard or intrigue >= 45:`
- southern_expansion.rpy:1110 — `if intrigue >= 35 or reputation >= 40 or port_insight >= 3:`
- southern_expansion.rpy:1438 — `if evidence_count >= 4 or (evidence_count >= 3 and intrigue >= 40):`
- southern_expansion.rpy:1446 — `if reputation >= 45 or southern_first_impression == "polite":`

### 统计

**各属性出现次数(共 120 个条件):**

| 属性 | 次数 | 占比 |
|---|---|---|
| 谋略(intrigue) | 47 | 39% |
| 权力(power) | 22 | 18% |
| 声望(reputation) | 14 | 12% |
| 信仰(faith) | 14 | 12% |
| 忠诚(loyalty) | 12 | 10% |
| 财富(wealth) | 11 | 9% |

**各章分布(按选项行数, 共 118 行):**

| 章节 | 行数 |
|---|---|
| 第一章 | 6 |
| 第二章 | 7 |
| 第三章 | 47 |
| 第四章 | 20 |
| 第五章 | 16 |
| 第五章·结局段 | 13 |
| 第五章·王子支线 | 1 |
| 内政系统(跨章) | 3 |
| NPC支线(跨章) | 1 |
| 南境扩展(跨章) | 4 |

**阈值分布(共 120 个条件):**

| 阈值 | 次数 |
|---|---|
| 25 | 3 |
| 35 | 1 |
| 40 | 7 |
| 45 | 35 |
| 50 | 22 |
| 55 | 17 |
| 58 | 4 |
| 60 | 24 |
| 65 | 2 |
| 70 | 5 |

阈值特征: 45/50/55/60 四档占 82%(98/120); 最低 25(第一二章早期), 最高 70(共 5 处, 全在戏剧张力最强的场景)。以初始值(intrigue=20/power=30)对照, 45+ 的门槛在不专精该属性时基本不可达——正是「隐藏选项玩家根本不知道存在」的重灾区。

---

## 二、危机判定系统精确规格(crisis.rpy)

### 2.1 判定公式(crisis.rpy:55-94 calculate_crisis_chance / :111-170 resolve_crisis)

判定形式: **1d10 + bonus ≥ difficulty** 即成功。与 attr_system.rpy:166 `dice_check` 同源(布兰特式), 但 resolve_crisis 内部是独立复制的一份逻辑, 没有复用 dice_check。

**bonus 合成(display 与 resolve 两处代码一致):**

```
## crisis.rpy:74-86 (calculate_crisis_chance) — resolve_crisis :133-138 同逻辑
stat_map = {"combat": "power", "intrigue": "intrigue",
            "faith": "faith", "survival": "loyalty"}
stat_val = getattr(store, stat_name, 30)

bonus = max(-3, min(7, (stat_val - 30) // 10))   ## 属性加成: -3..+7

## 勇气修正: courage >= 60 时 +1(只有这一档, 无更细梯度)
if store.courage >= 60:
    bonus += 1

## 伤势修正: 每次受伤 -1, 上限 -2
injury_penalty = min(2, store.crisis_injuries)
bonus -= injury_penalty
```

**UI 成功率换算(crisis.rpy:88-94):**

```
needed_roll = difficulty - bonus
success_faces = max(0, 10 - max(0, needed_roll - 1))
chance = success_faces * 10        ## clamp 0-100
## 例: difficulty=6, bonus=2 → 需 roll>=4 → 7 面 → 70%
```

危机类型→属性映射: combat→power(战斗) / intrigue→intrigue(阴谋) / faith→faith(信仰) / survival→loyalty(生存)。(CRISIS_TYPES, crisis.rpy:40-45)

### 2.2 界面展示(screen crisis_event, crisis.rpy:225-354)

玩家在决策前能看到的全部信息:

- 危机类型图标+名称(剑/刃/十/盾 + 「战斗危机」等), 红色标题
- 危机描述文本(crisis_description, 由 trigger_crisis 调用方传入)
- **成功率大数字 + 颜色**(≥70% 绿 / ≥40% 橙 / <40% 红) + 同色进度条
- **完整判定公式明牌**(crisis.rpy:302-308): `1d10 + [bonus] ≥ [difficulty]（[属性中文名] [属性值]）`——bonus 的显示值已含勇气修正与伤势修正
- 当前伤势 `[crisis_injuries]/3`(仅受过伤时显示)
- 按钮「迎接挑战」: 勇气足够时金色可点; **勇气 < crisis_courage_cost 时变灰不可点, 显示「需要 X 勇气」**(crisis.rpy:330-340)——全项目唯一的勇气门控点
- 按钮「退缩」+ 说明「退缩：回复 X 勇气，但错过奖励」; `crisis_allow_skip=False` 时整个隐藏(强制迎战)

判定后(screen crisis_dice_result, :360-397): 骰子大数字(成功绿/失败红) + 「骰子 X + 加成 Y = Z」+「需要总计 ≥ D」+ 结果文字, 2.5 秒自动关闭。

### 2.3 迎战/退缩完整结算流程(resolve_crisis :111-170 + label crisis_encounter :544-574)

**迎战(brave=True):**
1. `change_will(-crisis_courage_cost)` — 先扣勇气(默认 20, 无论成败不退还)
2. 重算 bonus(属性 + 勇气≥60 修正 + 伤势修正), 掷 1d10
3. **成功**(total ≥ difficulty): `crisis_result="success"`; `change_will(+25)`(固定回复, 不走 courage_gain 参数); `add_path_mark()` 加一枚路线印记(combat→martial / intrigue→scheme / faith→faith / survival→diplomacy, 集3枚激活路线, attr_system.rpy:349); 显示骰子结果 2.5s → `jump crisis_success_label`
4. **失败**: `crisis_result="fail"`; `crisis_injuries += 1`; `_apply_injury()` 施加减益并随机抽受伤文案; 显示骰子结果 → 受伤界面(伤势 X/3, ≥2 时红字死亡警告) → `is_dead()`(injuries≥3)则死亡结算画面(读档/重开, 进程终止), 否则 `jump crisis_fail_label`

**退缩(brave=False):** `crisis_result="retreat"`; `change_will(+crisis_courage_gain)`(默认 15); **不 jump, 直接 return 回调用处继续剧情**——即退缩没有专属分支文本, 是「无事发生」。

**受伤减益数值(_apply_injury :172-186):** combat→injury_debuff_power+3 / intrigue→injury_debuff_intrigue+3 / faith→injury_debuff_faith+3 / survival→power+2 且 intrigue+1。

> **硬发现: 伤势减益是「显示欺诈」。** injury_debuff_* 三个变量在全仓库只有 crisis.rpy 引用(受伤界面显示「权力 -3（伤势影响）」), 从未真正从属性扣除、也不参与任何判定; 实际参与判定的伤势惩罚是 `crisis_injuries` 计数(每伤 -1 bonus, 上限 -2)。改造危机系统时这里要么做实要么删掉。

### 2.4 勇气消耗与回复数值

| 事件 | 数值 | 出处 |
|---|---|---|
| 迎战消耗 | -crisis_courage_cost, 默认 20(实际调用见 20/25 两档) | crisis.rpy:121 |
| 迎战成功回复 | +25(硬编码) | crisis.rpy:151 |
| 迎战失败 | 无回复(净 -20/-25) | — |
| 退缩回复 | +crisis_courage_gain, 默认 15 | crisis.rpy:168 |
| 勇气判定加成 | courage ≥ 60 时 bonus +1 | crisis.rpy:80 |
| 初始/上限 | courage=50 / max_courage=100 | characters.rpy:133-134 |

change_will = `store.courage = max(0, min(store.max_courage, courage + delta))`(attr_system.rpy:451-453; courage.rpy:13 另有一份带 toast 的 change_courage)。

### 2.5 现有危机调用点(14 处, 语境修正的落点)

script.rpy:1231(ch1 阴谋 d4)、script.rpy:1696(ch1 战斗 d5, courage_cost=25)、chapter3.rpy:267(d4)、chapter3.rpy:4384(信仰 d5)、chapter3_expansion.rpy:410/423(d6/d5)、chapter4.rpy:2948/2967/2986(营救王子潜入三路线 d5/d2~4/d6, 全部 allow_skip=False, courage_cost=25)、chapter5.rpy:2864/2877/2889(终战 d6/d7/d5)、chapter5.rpy:3892/3911(d4/d4)。难度实测范围 d2-d7。

> **现成的语境修正先例**: chapter4.rpy:2966 `$ _stealth_diff = 2 if dark_lily_joined else 4` —— 与暗百合的关系直接改危机难度。改造方案可以把这种手写 if 泛化成 trigger_crisis 的修正参数。

---

## 三、12 个试点候选(含场景上下文原文)

遴选标准: 高阈值 / 选项文本自带戏剧张力 / 覆盖一至五章 / 涉及关键剧情人物(奥尔德里克、主教、国王、王子、暗百合)。属性覆盖: 谋略5 / 权力3 / 信仰1 / 财富1 / 声望1 / 忠诚1——与全量分布(谋略39%)一致。

| # | 文件:行 | 章节 | 门槛 | 选项文本 |
|---|---|---|---|---|
| 1 | chapter1_expansion.rpy:384 | 第一章 | 谋略≥50 | 下令调出父亲遇袭那夜的卷宗——你要从头查这件事 |
| 2 | chapter2.rpy:3427 | 第二章 | 谋略≥45(或 rel_aldric≥50) | 追问——「关于一切，是什么意思？」 |
| 3 | chapter3.rpy:1448 | 第三章 | 谋略≥70 | 什么都不出示——直接报出几个内部暗号 |
| 4 | chapter3.rpy:4630 | 第三章 | 信仰≥58 | 表示理解——'你也是受害者' |
| 5 | chapter3.rpy:5764 | 第三章 | 权力≥65 | 主动出击——在他们完成包围之前冲出去 |
| 6 | chapter4.rpy:1301 | 第四章 | 声望≥60 | 以领地民望做担保——你已名声在外 |
| 7 | chapter4.rpy:2847 | 第四章 | 权力≥55 | 冒险营救王子 |
| 8 | chapter4_expansion.rpy:407 | 第四章 | 财富≥60 | 推一袋金币过去——「告诉我你今天没说完的那部分」 |
| 9 | chapter5.rpy:841 | 第五章 | 权力≥70 | 亲自指挥北墙改造 |
| 10 | chapter5.rpy:2309 | 第五章 | 谋略≥70 + 序章毒草flag + 毒证flag | 用毒药清理一切——以母亲的方式收尾\|不动刀兵，用「暮色之露」逐一清场 → 毒药公爵 |
| 11 | chapter5.rpy:2694 | 第五章·结局段 | 忠诚≥70 | 亲自跪在老人面前——以你的名义起誓重建 |
| 12 | chapter5.rpy:5080 | 第五章·结局段 | 谋略≥60 | 动用整张情报网——把附和者的底册当场摊开\|烧掉多年暗线，换一场干净的胜利 |

### 候选 1 — chapter1_expansion.rpy:384(第一章, 谋略≥50)

**选项**: 「下令调出父亲遇袭那夜的卷宗——你要从头查这件事」  
**label**: `ch1_exp_ramparts_night`  
**完整条件**: `if intrigue >= 50:`  
**入选理由**: 下令调出父亲遇袭那夜的卷宗——主线核心谜团(父亲遇袭)的首个主动侦查口; 对初始谋略20而言是难以企及的高墙

```renpy
    354| 
    355|     "两人对视了一瞬。然后他收剑行礼。"
    356| 
    357|     $ hide_all_chars("captain_img")
    358|     show captain_img at left with dissolve
    359|     captain "领主大人。深夜巡城？"
    360| 
    361|     hide captain_img
    362|     $ hide_all_chars("player_char_img")
    363|     show player_char_img at left with dissolve
    364|     player "睡不着。你呢？"
    365| 
    366|     hide player_char_img
    367|     $ hide_all_chars("captain_img")
    368|     show captain_img at left with dissolve
    369|     captain "……也睡不着。"
    370| 
    371|     "他把剑插回鞘中，走到城垛旁，望着远处的黑暗。"
    372| 
    373|     captain "我跟随老领主十二年了。从他把我收留下来那天起。他教我带兵，也教我怎么做一个好的卫队长。"
    374| 
    375|     "他的声音很平静，但你听得出底下的暗流。"
    376| 
    377|     captain "他走的那天晚上，我也是在这里。就站在这个位置。"
    378| 
    379|     "他转过头看你。夜色中看不清表情，但你从他的眼神里读到了一种你没想到的东西——不是悲伤，是愧疚。"
    380| 
    381|     captain "我应该保护好他的。这是我唯一的职责。但我失败了。"
    382| 
    383|     menu:
>>  384|         "下令调出父亲遇袭那夜的卷宗——你要从头查这件事" if intrigue >= 50:
    385|             $ change_stat("intrigue", 5)
    386|             $ change_rel("rel_captain", 5)
    387|             $ ch1_exp_captain_respect = True
    388|             $ log_decision("第一章扩展", "调阅父亲遇袭卷宗")
    389| 
    390|             hide captain_img
    391|             $ hide_all_chars("player_char_img")
    392|             show player_char_img at left with dissolve
    393|             player "雷恩， 把那一夜每个值班士兵的名字、岗位、当晚行动列出来。我要看。"
    394| 
    395|             $ hide_all_chars()
    396|             "雷恩愣了一下。然后他点了点头， 表情第一次有了别的颜色——不只是悔。"
    397|             "他比你还清楚——这才是你父亲会让你做的事。"
    398| 
    399|             $ hide_all_chars("captain_img")
    400|             show captain_img at left with dissolve
    401|             captain "我天亮前送到您书房。"
    402| 
    403|         "「不是你的错。我也没能保护他。」":
    404|             $ change_rel("rel_captain", 10)
    405|             $ change_stat("loyalty", 3)
    406|             $ log_decision("第一章扩展", "安慰雷恩")
    407| 
    408|             "你走到他身边，和他并肩站在城垛前。"
    409| 
    410|             hide captain_img
    411|             $ hide_all_chars("player_char_img")
    412|             show player_char_img at left with dissolve
    413|             player "如果自责有用，我应该比你更自责。我甚至不在他身边。"
    414| 
```

### 候选 2 — chapter2.rpy:3427(第二章, 谋略≥45(或 rel_aldric≥50))

**选项**: 「追问——「关于一切，是什么意思？」」  
**label**: `ch2_end`  
**完整条件**: `if (intrigue >= 45 or rel_aldric >= 50) and not father_was_regent_known:`  
**入选理由**: 章末追问奥尔德里克「关于一切」——揭开父亲摄政身份(father_was_regent_known)的关键触发, 复合条件门控的代表

```renpy
   3397|         show player_char_img at left with dissolve
   3398|         player "你觉得和当年的事有关？"
   3399| 
   3400|         hide player_char_img
   3401|         $ hide_all_chars("aldric_img")
   3402|         show aldric_img at left with dissolve
   3403|         aldric "老臣不敢妄下定论。但三十年了，那些暗中行事的人……也许从未消失。"
   3404| 
   3405|         "他的目光落在你身上，带着一种你熟悉的沉重——那是他在书房中向你坦白骑士团往事时同样的神情。"
   3406| 
   3407|         aldric "领主大人，先让大夫处理您的伤口。今晚的事，明日再细细商议。"
   3408|     else:
   3409|         ## 安全兜底：若支线未触发
   3410|         aldric "领主大人，有些事……也许到了该告诉你的时候了。"
   3411| 
   3412|         aldric "但不是现在。先让大夫处理您的伤口，好好休息一晚。明天，老臣有话对您说。"
   3413| 
   3414|         hide aldric_img
   3415|         $ hide_all_chars("player_char_img")
   3416|         show player_char_img at left with dissolve
   3417|         player "关于父亲？"
   3418| 
   3419|         hide player_char_img
   3420|         $ hide_all_chars("aldric_img")
   3421|         show aldric_img at left with dissolve
   3422|         aldric "关于一切。"
   3423| 
   3424|     "老骑士的语气异常沉重。你从他脸上读到了深深的忧虑——不只是为今晚的伏击。"
   3425| 
   3426|     menu:
>> 3427|         "追问——「关于一切，是什么意思？」" if (intrigue >= 45 or rel_aldric >= 50) and not father_was_regent_known:
   3428|             $ change_stat("intrigue", 5)
   3429|             hide aldric_img
   3430|             $ hide_all_chars("player_char_img")
   3431|             show player_char_img at left with dissolve
   3432|             player "雷恩，让人都退下。"
   3433|             player "奥尔德里克——「关于一切」，是什么意思？刚才那刀差点穿过我的喉咙。我想我有资格现在就听。"
   3434| 
   3435|             hide player_char_img
   3436|             $ hide_all_chars("aldric_img")
   3437|             show aldric_img at left with dissolve
   3438|             aldric "……领主大人。"
   3439|             aldric "好吧。也许该让你知道一些了——尤其是在你刚刚活下来之后。"
   3440| 
   3441|             aldric "你父亲不是寻常的边境领主。先王临终前，留下过一道遗诏——指定一位摄政者，辅佐年幼的王子，直至他成年。"
   3442| 
   3443|             aldric "那个名字……是你父亲。"
   3444| 
   3445|             $ father_was_regent_known = True
   3446| 
   3447|             hide aldric_img
   3448|             $ hide_all_chars("player_char_img")
   3449|             show player_char_img at left with dissolve
   3450|             player "……父亲？摄政？"
   3451| 
   3452|             "你听见自己的声音从很远的地方传来。"
   3453| 
   3454|             hide player_char_img
   3455|             $ hide_all_chars("aldric_img")
   3456|             show aldric_img at left with dissolve
   3457|             aldric "但那道遗诏从未公开生效。其中的曲折，老领主从未对老臣细说——他守得太严了。"
```

### 候选 3 — chapter3.rpy:1448(第三章, 谋略≥70)

**选项**: 「什么都不出示——直接报出几个内部暗号」  
**label**: `ch3_dark_lily_clues`  
**完整条件**: `if intrigue >= 70:`  
**入选理由**: 不出示任何信物、直接报暗号闯暗百合据点——全游戏最高谋略门槛之一, 失败分支天然成立(暗号报错=当场暴露)

```renpy
   1418| 
   1419|     "卖水果的摊贩偷偷往几个水果上画了百合花的标记。"
   1420| 
   1421|     "一个修鞋匠的摊位上挂着一面旗帜，旗帜的角落里绣着一朵几乎看不见的百合花。"
   1422| 
   1423|     "他们是暗百合的人？还是只是巧合？"
   1424| 
   1425|     "你继续走。沿着密道中发现的地图指引，穿过拥挤的人群，来到集市的东北角。"
   1426| 
   1427|     "这里是一条幽暗的小巷。一家不起眼的草药铺还亮着灯。"
   1428| 
   1429|     "店铺的招牌上写着——「百合草药」。"
   1430| 
   1431|     $ hide_all_chars("player_char_img")
   1432|     show player_char_img at left with dissolve
   1433|     player "百合草药……"
   1434| 
   1435|     $ hide_all_chars()
   1436|     "你推门而入。"
   1437| 
   1438|     "一个老妇人坐在柜台后面，正在研磨什么东西。她没有抬头。"
   1439| 
   1440|     hide player_char_img
   1441|     $ hide_all_chars("lily_root_img")
   1442|     show lily_root_img at left with dissolve
   1443|     apothecary "客人要什么？治感冒？补身子？还是……别的？"
   1444| 
   1445|     "你注意到她的围裙上绣着一朵百合花——不是倒置的，但你直觉告诉你这不是巧合。"
   1446| 
   1447|     menu:
>> 1448|         "什么都不出示——直接报出几个内部暗号" if intrigue >= 70:
   1449|             $ change_stat("intrigue", 5)
   1450|             $ change_rel("rel_lily", -5)  ## 厚度: 外人能背出内部暗号=安全漏洞, 暗百合从一开始就提防你
   1451|             $ hide_all_chars("player_char_img")
   1452|             show player_char_img at left with dissolve
   1453|             player "「七瓣莲花将在月圆之夜绽放」。「壁炉后的人没有倒下」。"
   1454|             $ hide_all_chars()
   1455|             "老妇人的研磨棒停了。她看了你三秒， 然后慢慢转身， 把店门口的木牌翻成了「已打烊」。"
   1456|             $ hide_all_chars("lily_root_img")
   1457|             show lily_root_img at left with dissolve
   1458|             apothecary "你哪里学来的？"
   1459|             hide lily_root_img
   1460|             $ hide_all_chars("player_char_img")
   1461|             show player_char_img at left with dissolve
   1462|             player "我父亲留给我一本日记。我翻得不下百遍。"
   1463|             $ hide_all_chars()
   1464|             "她盯着你， 终于叹了口气。"
   1465|             $ hide_all_chars("lily_root_img")
   1466|             show lily_root_img at left with dissolve
   1467|             apothecary "一个外人能一字不差地报出我们的暗号——你知道这说明什么吗？说明这套暗号已经不安全了。"
   1468|             apothecary "你父亲怎么知道的， 你又记了多少——这些我们迟早要问清楚。在那之前， 你在我们眼里不是自己人， 是个会走路的窟窿。"
   1469|             apothecary "跟我来。"
   1470|             "她推开了柜台后面的一扇暗门。门轴的声音很轻， 但她让你走在前面——她不放心把背留给你。"
   1471| 
   1472|         "出示在密道中找到的银质徽章" if intrigue >= 45:
   1473|             $ change_stat("intrigue", 8)
   1474|             $ hide_all_chars()
   1475|             "你从怀中取出那枚银质徽章，放在柜台上。"
   1476|             "老妇人终于抬起头来。她的眼睛在看到徽章的一瞬间猛然睁大。"
   1477|             $ hide_all_chars("lily_root_img")
   1478|             show lily_root_img at left with dissolve
```

### 候选 4 — chapter3.rpy:4630(第三章, 信仰≥58)

**选项**: 「表示理解——'你也是受害者'」  
**label**: `ch3_bishop_take_to_vault`  
**完整条件**: `if faith >= 58:`  
**入选理由**: 对主教说「你也是受害者」——关键人物主教的救赎线, 信仰路线的情感高点

```renpy
   4600|             hide bishop_img
   4601|             $ hide_all_chars("player_char_img")
   4602|             show player_char_img at left with dissolve
   4603|             player "二十年的恐惧， 够了。"
   4604|             player "你跟我回艾登堡。我给你一座院子， 一队卫士， 一份没人能动的安宁。"
   4605|             player "你余生只做一件事——把你知道的， 写下来。"
   4606|             $ hide_all_chars()
   4607|             "马修斯哭了。这次不是悔恨——是终于有人愿意接住他这二十年的重量。"
   4608|             "你给了一个怕死的老人一条可以坦然走完的路。这比惩罚更难， 也更值得。"
   4609| 
   4610|         "严厉斥责——'你的沉默害死了我的父亲'":
   4611|             $ change_rel("rel_bishop", -15)
   4612|             $ change_stat("power", 5)
   4613|             hide bishop_img
   4614|             $ hide_all_chars("player_char_img")
   4615|             show player_char_img at left with dissolve
   4616|             player "如果你早些站出来，我的父亲就不用死！"
   4617|             hide player_char_img
   4618|             $ hide_all_chars("bishop_img")
   4619|             show bishop_img at left with dissolve
   4620|             bishop "我知道……我知道！我的罪孽深重……"
   4621|             hide bishop_img
   4622|             $ hide_all_chars("player_char_img")
   4623|             show player_char_img at left with dissolve
   4624|             player "但现在后悔已经来不及了。你能做的，就是帮我把这件事做到底。"
   4625|             hide player_char_img
   4626|             $ hide_all_chars("bishop_img")
   4627|             show bishop_img at left with dissolve
   4628|             bishop "……是。我会的。这是我唯一能赎罪的方式。"
   4629| 
>> 4630|         "表示理解——'你也是受害者'" if faith >= 58:
   4631|             $ change_rel("rel_bishop", 15)
   4632|             $ change_stat("faith", 12)
   4633|             hide bishop_img
   4634|             $ hide_all_chars("player_char_img")
   4635|             show player_char_img at left with dissolve
   4636|             player "费雷恩的错不应该由你来承担。你保住了这份遗诏——这已经足够。"
   4637|             hide player_char_img
   4638|             $ hide_all_chars("bishop_img")
   4639|             show bishop_img at left with dissolve
   4640|             bishop "领主大人……你和老领主一样宽容。"
   4641|             hide bishop_img
   4642|             $ hide_all_chars("player_char_img")
   4643|             show player_char_img at left with dissolve
   4644|             player "但从现在起，你必须和我站在一起。"
   4645|             hide player_char_img
   4646|             $ hide_all_chars("bishop_img")
   4647|             show bishop_img at left with dissolve
   4648|             bishop "我愿意。以上天之名，我愿意。"
   4649| 
   4650|         "冷静分析——'这份遗诏需要验证'":
   4651|             $ change_stat("reputation", 5)
   4652|             hide bishop_img
   4653|             $ hide_all_chars("player_char_img")
   4654|             show player_char_img at left with dissolve
   4655|             player "我们不能贸然使用这份遗诏。首先要确认它的真实性。"
   4656|             hide player_char_img
   4657|             $ hide_all_chars("bishop_img")
   4658|             show bishop_img at left with dissolve
   4659|             bishop "你说得对。我可以安排教会的文书专家来鉴定。"
   4660|             hide bishop_img
```

### 候选 5 — chapter3.rpy:5764(第三章, 权力≥65)

**选项**: 「主动出击——在他们完成包围之前冲出去」  
**label**: `ch3_chapter_crisis`  
**完整条件**: `if power >= 65:`  
**入选理由**: 围城之夜主动突围——章节危机的高武力解, 失败=突围被截杀, 戏剧张力极强

```renpy
   5734|                 $ hide_all_chars("captain_img")
   5735|                 show captain_img at left with dissolve
   5736|                 captain "明白。我立刻安排骑手。"
   5737|             else:
   5738|                 hide captain_img
   5739|                 $ hide_all_chars("player_char_img")
   5740|                 show player_char_img at left with dissolve
   5741|                 player "那就用密道。"
   5742|                 hide player_char_img
   5743|                 $ hide_all_chars("captain_img")
   5744|                 show captain_img at left with dissolve
   5745|                 captain "密道？"
   5746|                 hide captain_img
   5747|                 $ hide_all_chars("player_char_img")
   5748|                 show player_char_img at left with dissolve
   5749|                 player "城堡下面有密道通向外面。我发现的。奥尔德里克知道路线。"
   5750|                 "奥尔德里克点了点头。"
   5751|             hide player_char_img
   5752|             hide captain_img
   5753|             $ hide_all_chars("aldric_img")
   5754|             show aldric_img at left with dissolve
   5755|             aldric "我带人从密道出去。两天之内，援军就到。"
   5756|             hide aldric_img
   5757|             $ hide_all_chars("player_char_img")
   5758|             show player_char_img at left with dissolve
   5759|             player "去吧。小心。"
   5760|             $ hide_all_chars()
   5761|             "奥尔德里克带着两个信使消失在城堡地下。"
   5762|             "你则留在城墙上，指挥防御。"
   5763| 
>> 5764|         "主动出击——在他们完成包围之前冲出去" if power >= 65:
   5765|             $ change_stat("power", 20)
   5766|             $ change_stat("loyalty", 5)
   5767|             $ hide_all_chars("player_char_img")
   5768|             show player_char_img at left with dissolve
   5769|             player "他们还没有完成包围。南面的这支是主力——北面一定薄弱。"
   5770|             hide player_char_img
   5771|             $ hide_all_chars("captain_img")
   5772|             show captain_img at left with dissolve
   5773|             captain "大人想突围？"
   5774|             hide captain_img
   5775|             $ hide_all_chars("player_char_img")
   5776|             show player_char_img at left with dissolve
   5777|             player "不是突围。是反击。"
   5778|             player "我亲自带五十人从北门出击，绕到他们侧翼。雷恩，你带剩下的人守城。"
   5779|             hide player_char_img
   5780|             $ hide_all_chars("captain_img")
   5781|             show captain_img at left with dissolve
   5782|             captain "大人！太危险了！"
   5783|             hide captain_img
   5784|             $ hide_all_chars("aldric_img")
   5785|             show aldric_img at left with dissolve
   5786|             aldric "让他去。他父亲年轻时也是这样——亲自上阵。"
   5787|             $ hide_all_chars()
   5788|             "你带着五十名精锐骑兵从北门冲出。"
   5789|             "正如你所料，敌人的主力集中在南面。北面只有少量哨骑。"
   5790|             "你绕了一个大弧，从西面杀入敌人的侧翼。"
   5791|             "突如其来的打击让敌人阵脚大乱。他们没想到守军会主动出击。"
   5792|             "混战持续了不到半个小时。敌人撤退了，留下了十几具尸体。"
   5793|             "你俘虏了三个人。也许能从他们口中得到有用的信息。"
   5794| 
```

### 候选 6 — chapter4.rpy:1301(第四章, 声望≥60)

**选项**: 「以领地民望做担保——你已名声在外」  
**label**: `ch4_throne`  
**完整条件**: `if reputation >= 60:`  
**入选理由**: 御前以领地民望做担保——面对国王的声望豪赌, 失败分支(国王不买账)有天然的政治代价

```renpy
   1271| 
   1272|     "你保持着平静的表情。"
   1273| 
   1274|     $ hide_all_chars("queen_img")
   1275|     show queen_img at left with dissolve
   1276|     queen "我召你来，是有两件事要谈。"
   1277| 
   1278|     queen "第一，北方边境的局势。冯·哈根男爵近来动作频频，我需要你替我盯着他。"
   1279| 
   1280|     queen "艾登堡地处要冲，是北方通往王都的门户。你明白这意味着什么。"
   1281| 
   1282|     if eagle_intel:
   1283|         $ hide_all_chars()
   1284|         "（信息网没说错。她要借你的刀除掉男爵。她以为这是试探——可你昨夜就拿到了答案。）"
   1285| 
   1286|     hide queen_img
   1287|     $ hide_all_chars("player_char_img")
   1288|     show player_char_img at left with dissolve
   1289|     player "臣明白。艾登堡是王室的屏障。"
   1290| 
   1291|     hide player_char_img
   1292|     $ hide_all_chars("queen_img")
   1293|     show queen_img at left with dissolve
   1294|     queen "很好。不过光明白还不够，我需要你做到。"
   1295| 
   1296|     queen "我会给你一千枚金币和三百套军械，用于加强艾登堡的防务。"
   1297| 
   1298|     queen "作为交换——每月一份详细的北方动态报告，直接送到我手中。"
   1299| 
   1300|     menu:
>> 1301|         "以领地民望做担保——你已名声在外" if reputation >= 60:
   1302|             $ log_decision("第四章", "以民望做担保, 王后给了额外奖励")
   1303|             $ change_stat("reputation", 5)
   1304|             $ change_stat("wealth", 30)
   1305|             $ change_stat("power", 5)
   1306|             hide queen_img
   1307|             $ hide_all_chars("player_char_img")
   1308|             show player_char_img at left with dissolve
   1309|             player "臣愿领旨。陛下可问王都的人——艾登堡这一年的民望，不输王室任何一个直辖郡。这便是臣给陛下的担保。"
   1310|             hide player_char_img
   1311|             $ hide_all_chars("queen_img")
   1312|             show queen_img at left with dissolve
   1313|             queen "……你倒是真敢说。"
   1314|             "王后看了你许久，然后抬手招来侍从。"
   1315|             queen "再加五百金币，五十套军械。看你能不能把这份「民望」兑现成边境的安宁。"
   1316|             "你领旨退下。这是你第一次拿外人的评价当作筹码——而王后给了。"
   1317| 
   1318|         "接受条件":
   1319|             $ log_decision("第四章", "接受王后的条件")
   1320|             $ change_stat("wealth", 25)
   1321|             $ change_stat("power", 5)
   1322|             $ change_stat("reputation", -3)
   1323|             $ change_rel("rel_queen", 5)
   1324|             hide queen_img
   1325|             $ hide_all_chars("player_char_img")
   1326|             show player_char_img at left with dissolve
   1327|             player "臣领命。"
   1328|             hide player_char_img
   1329|             $ hide_all_chars("queen_img")
   1330|             show queen_img at left with dissolve
   1331|             queen "很好。我喜欢爽快的人。"
```

### 候选 7 — chapter4.rpy:2847(第四章, 权力≥55)

**选项**: 「冒险营救王子」  
**label**: `ch4_betrayal`  
**完整条件**: `if power >= 55:`  
**入选理由**: 冒险营救王子——牵动王子线全局的关键抉择, 门槛不够时玩家甚至不知道可以救

```renpy
   2817| 
   2818|         $ hide_all_chars("captain_img")
   2819|         show captain_img at left with dissolve
   2820|         captain "领主大人，我们必须马上行动，否则下一个被抓的就是您！"
   2821|         captain "我已经让卫队做好了撤离准备。但时间不多——"
   2822|         captain "王宫的大门随时可能关闭。"
   2823|     else:
   2824|         captain "王宫出大事了！王子殿下被指控谋反，已经被关押！"
   2825|         captain "整个王宫都乱成了一锅粥——"
   2826|         captain "王都全面戒严，所有外地领主不得离开！"
   2827|         captain "城门已经关闭，街上到处是巡逻的士兵。"
   2828| 
   2829|     hide captain_img with dissolve
   2830| 
   2831|     if prince_ally and not prince_betrayed:
   2832|         $ hide_all_chars()
   2833|         "你的心跳得撞到嗓子。你只有几秒钟。"
   2834| 
   2835|         $ hide_all_chars("elena_img")
   2836|         show elena_img at left with dissolve
   2837| 
   2838|         elena "领主大人，我了解这座王宫。有三条路可以走。"
   2839|         elena "第一，去地牢救人。我知道地牢的布局和守卫换班的时间。"
   2840|         elena "第二，撇清关系。销毁所有证据，否认一切。以你目前的身份，他们很难定你的罪。"
   2841|         elena "第三，趁乱逃离王都。城西的排水渠可以通到城外。"
   2842|         elena "无论你选哪条路——我都跟你走。"
   2843| 
   2844|         hide elena_img with dissolve
   2845| 
   2846|         menu:
>> 2847|             "冒险营救王子" if power >= 55:
   2848|                 $ change_stat("power", 10)
   2849|                 $ change_rel("rel_prince", 30)
   2850|                 $ change_rel("rel_queen", -30)
   2851|                 $ hide_all_chars("player_char_img")
   2852|                 show player_char_img at left with dissolve
   2853|                 player "我答应过他。我不能食言。"
   2854|                 jump ch4_rescue
   2855| 
   2856|             "撇清关系，否认一切":
   2857|                 $ change_stat("intrigue", 5)
   2858|                 $ change_rel("rel_prince", -20)
   2859|                 $ hide_all_chars("player_char_img")
   2860|                 show player_char_img at left with dissolve
   2861|                 player "告诉所有人，我根本不认识王子。那天晚上我一直在房间里。"
   2862|                 "雷恩迟疑了一下，但还是点了头。"
   2863|                 hide player_char_img
   2864|                 $ hide_all_chars("captain_img")
   2865|                 show captain_img at left with dissolve
   2866|                 captain "明白。我去安排人证。"
   2867| 
   2868|                 $ hide_all_chars()
   2869|                 "三天后，你听说地牢里的王子一个字都没为你辩解。他既没有指认你，也没有否认。"
   2870|                 "他只是沉默。"
   2871| 
   2872|                 jump ch4_deny
   2873| 
   2874|             "趁乱逃离王都":
   2875|                 $ change_stat("power", -5)
   2876|                 $ change_rel("rel_prince", -15)
   2877|                 hide captain_img
```

### 候选 8 — chapter4_expansion.rpy:407(第四章, 财富≥60)

**选项**: 「推一袋金币过去——「告诉我你今天没说完的那部分」」  
**label**: `ch4_exp_explore_market`  
**完整条件**: `if wealth >= 60:`  
**入选理由**: 推一袋金币买下「没说完的那部分」——财富门控代表, 失败分支(钱不够被讥讽)几乎是自动生成的

```renpy
    377|         "《六卫终录》里的那句话是真的——根卫没死。他们就在这些商会里，就在这杆秤上。"
    378|         "你不动声色地记下了这家商号的名字。南边的商路上还有多少这样的记号，值得让艾琳娜查一查。"
    379|         $ change_stat("intrigue", 3)
    380| 
    381|     "你假装挑选货物，耳朵却在捕捉周围的对话。"
    382| 
    383|     narrator "「……新税又加了两成。照这样下去，年底前得关掉三分之一的店铺。」"
    384| 
    385|     narrator "「嘘！小声点。上次老马抱怨税重，第二天密探就上门了。」"
    386| 
    387|     narrator "「我就纳闷了，先王在的时候可不是这样。那时候商税才一成五……」"
    388| 
    389|     narrator "「先王？那都是二十年前的事了。现在是王后的天下。」"
    390| 
    391|     "你装作不经意地问了句。"
    392| 
    393|     $ hide_all_chars("player_char_img")
    394|     show player_char_img at left with dissolve
    395|     player "这位兄台，最近生意怎么样？"
    396| 
    397|     $ hide_all_chars()
    398|     narrator "胖老板警惕地看了你一眼，然后露出职业笑容。"
    399| 
    400|     narrator "「嘿，爷，您是外地来的吧？看您穿戴就知道是有身份的人。」"
    401| 
    402|     narrator "「生意嘛……还成，还成。王后治下国泰民安，我们做买卖的没什么好抱怨的。」"
    403| 
    404|     "他说最后一句话时，眼睛飞快地瞟了一下门外——你注意到门外确实站着一个不像是顾客的人。"
    405| 
    406|     menu:
>>  407|         "推一袋金币过去——「告诉我你今天没说完的那部分」" if wealth >= 60:
    408|             $ change_stat("wealth", -10)
    409|             $ change_stat("intrigue", 5)
    410|             $ ch4_exp_merchant_tip = True
    411| 
    412|             "你不动声色地把一袋金币放在柜台下面， 推了过去。"
    413| 
    414|             narrator "胖老板的手指捏了捏袋子的厚度， 立刻明白了你的意思。他把袋子收进围裙， 表情松了下来。"
    415| 
    416|             narrator "「贵客真是爽快人。」"
    417| 
    418|             narrator "「您是来觐见王后的吧？我说几句， 您听了就忘——上个月西区死了十几个人， 官面上是瘟疫， 实际是被灭了口。」"
    419| 
    420|             narrator "「都是打听先王遗诏的人。」"
    421| 
    422|             if true_killer_known:
    423|                 "先王遗诏——你心中一动。如果王后篡改了遗诏， 那被灭口就完全说得通了。"
    424| 
    425|             narrator "「还有——大主教马修斯最近来王都了。那老头一般不轻易出主教座堂。他来了， 肯定有大事。」"
    426| 
    427|             narrator "「再多您给再多金币， 我也不知道。这个城市深的地方， 我够不着。」"
    428| 
    429|             "你又往柜台下塞了半袋金币。「这袋不为打听。」你说。胖老板把它收得比第一袋更快——他知道这是封口的价钱。"
    430| 
    431|             $ change_stat("wealth", -5)
    432| 
    433|         "给他看艾登堡的家徽，表明身份":
    434|             $ change_stat("power", 3)
    435|             $ change_stat("reputation", 3)
    436|             $ change_stat("intrigue", -8)
    437|             $ ch4_exp_merchant_tip = True
```

### 候选 9 — chapter5.rpy:841(第五章, 权力≥70)

**选项**: 「亲自指挥北墙改造」  
**label**: `ch5_military_deploy`  
**完整条件**: `if power >= 70:`  
**入选理由**: 亲自指挥北墙改造——全仓库最高权力门槛, 大战前的统帅力展示

```renpy
    811|     $ hide_all_chars("player_char_img")
    812|     show player_char_img at left with dissolve
    813|     player "装备情况？"
    814| 
    815|     hide player_char_img
    816|     $ hide_all_chars("captain_img")
    817|     show captain_img at left with dissolve
    818|     captain "正规军的装备基本齐全。但民兵的装备比较简陋——大多只有皮甲和简单的武器。"
    819| 
    820|     if wealth >= 50:
    821|         captain "不过，领主大人之前拨付的军费让我们采购了一批新的装备。"
    822|         captain "至少每个人都有一件像样的铠甲和一把磨好的剑了。"
    823|     else:
    824|         captain "装备不足是我们最大的短板。不过铁匠们正在日夜赶工。"
    825| 
    826|     hide captain_img
    827|     $ hide_all_chars("player_char_img")
    828|     show player_char_img at left with dissolve
    829|     player "城防呢？"
    830| 
    831|     hide player_char_img
    832|     $ hide_all_chars("captain_img")
    833|     show captain_img at left with dissolve
    834|     captain "城墙高三丈，厚一丈二。四座箭塔，每座配备五名弓手。"
    835| 
    836|     captain "城门加固了铁皮，还准备了滚石、火油和沸水。"
    837| 
    838|     captain "唯一的弱点是北墙——去年冬天的暴风雪损坏了一段，虽然修补了，但强度不如其他地方。"
    839| 
    840|     menu:
>>  841|         "亲自指挥北墙改造" if power >= 70:
    842|             $ change_stat("power", 5)
    843|             $ change_stat("loyalty", 3)
    844|             $ change_stat("intrigue", -10)
    845|             hide captain_img
    846|             $ hide_all_chars("player_char_img")
    847|             show player_char_img at left with dissolve
    848|             player "雷恩，跟我去北墙。我亲自盯三天。"
    849|             player "石匠加固。陷阱布在内侧三十步。城上设三排弓手暗位，对准内侧死角——让北墙不只是难破， 是破了就死。"
    850|             $ hide_all_chars("captain_img")
    851|             show captain_img at left with dissolve
    852|             captain "……明白。亲自来盯， 工艺只会比我多想一倍。"
    853|             $ hide_all_chars()
    854|             "三天里你和士兵睡在城墙下。手上磨出两层老茧。但当北墙被加固到每块石都像是为攻城战量身定做时——士气也跟着起来了。"
    855|             "走过来挑刺的老兵都摇头笑了一声。不只是力量本身——是力量摆出来的姿态。"
    856|             "这三天你眼里只有那段墙。城里另外那些要你亲自过问的人和事，只能先搁着——奥德递进来的几张条子，你压根没翻。"
    857| 
    858|         "加强北墙的防御":
    859|             $ change_stat("power", 3)
    860|             $ change_stat("wealth", -8)
    861|             hide captain_img
    862|             $ hide_all_chars("player_char_img")
    863|             show player_char_img at left with dissolve
    864|             player "调更多人手去加固北墙。同时在北墙后面再建一道木栅栏作为第二道防线。"
    865|             hide player_char_img
    866|             $ hide_all_chars("captain_img")
    867|             show captain_img at left with dissolve
    868|             captain "好主意。多调人手、再添一道木栅，料和工钱我从账上支。"
    869|             captain "省是省不下，但这道墙稳了。"
    870|             "接下来两天，北墙的防御被大大加强了。"
    871| 
```

### 候选 10 — chapter5.rpy:2309(第五章, 谋略≥70 + 序章毒草flag + 毒证flag)

**选项**: 「用毒药清理一切——以母亲的方式收尾|不动刀兵，用「暮色之露」逐一清场 → 毒药公爵」  
**label**: `ch5_final_choice`  
**完整条件**: `if deep_mother_herb == "poison" and intrigue >= 70 and poison_evidence:`  
**入选理由**: 用母亲的方式收尾→毒药公爵结局——三重门控的隐藏终局路线, 玩家最容易完全错过的高价值内容

```renpy
   2279|             $ log_decision("第五章", "选择守护人民的幸福")
   2280|             $ ending_type = "peoples_lord"
   2281|             hide bishop_img
   2282|             $ hide_all_chars("player_char_img")
   2283|             show player_char_img at left with dissolve
   2284|             player "我不是任何人的棋子，也不需要任何人的王座。"
   2285|             player "我只需要保护好我的人民。艾登堡的百姓，就是我最大的财富。"
   2286|             hide player_char_img
   2287|             $ hide_all_chars("aldric_img")
   2288|             show aldric_img at left with dissolve
   2289|             aldric "领主大人……"
   2290|             $ hide_all_chars()
   2291|             "你做出了一个出乎所有人意料的决定——放弃争霸，全力守护。"
   2292|             call ending_decision_pause from _call_decision_pause_peoples
   2293|             jump ending_peoples_lord
   2294| 
   2295|         "公布先王遗诏真相——让正义重见天日|当众公开遗诏，与王后正面对质 → 真相大白" if true_killer_known and testament_original_obtained:
   2296|             $ log_decision("第五章", "选择揭露全部真相")
   2297|             $ ending_type = "truth"
   2298|             hide aldric_img
   2299|             $ hide_all_chars("player_char_img")
   2300|             show player_char_img at left with dissolve
   2301|             player "这个王国建立在一个谎言之上。是时候让真相大白了。"
   2302|             player "我的父亲为此付出了生命。我不能让他白死。"
   2303|             $ hide_all_chars()
   2304|             "你从怀中取出那份尘封多年的遗诏复本，在阳光下展开。"
   2305|             "这一刻，你不是在为自己而战——而是在为二十年前被掩盖的正义而战。"
   2306|             call ending_decision_pause from _call_decision_pause_truth
   2307|             jump ending_truth
   2308| 
>> 2309|         "用毒药清理一切——以母亲的方式收尾|不动刀兵，用「暮色之露」逐一清场 → 毒药公爵" if deep_mother_herb == "poison" and intrigue >= 70 and poison_evidence:
   2310|             $ log_decision("第五章", "选择以毒药逐一清理敌人")
   2311|             $ ending_type = "borgia"
   2312|             hide aldric_img
   2313|             $ hide_all_chars("player_char_img")
   2314|             show player_char_img at left with dissolve
   2315|             player "战场上的剑只能杀一个人。但一杯酒——可以让一整个家族在三个月内消失。"
   2316|             player "我母亲六岁就教会了我这个道理。"
   2317|             $ hide_all_chars()
   2318|             "你慢慢站起来，走到书房深处的那个旧木柜前。"
   2319|             "柜子最底层的暗格里，放着一个紫色的小瓶——你继任以来悄悄收集的「暮色之露」。"
   2320|             "够用了。"
   2321|             call ending_decision_pause from _call_decision_pause_borgia
   2322|             jump ending_borgia
   2323| 
   2324|         "效忠王后，换取艾登堡安全|签城下之盟——保人保地，交出自主 → 附庸领主" if _vassal_available:
   2325|             $ ending_type = "vassal"
   2326|             $ log_decision("第五章", "选择效忠王后, 艾登堡降为附庸")
   2327|             $ hide_all_chars("player_char_img")
   2328|             show player_char_img at left with dissolve
   2329|             player "在两个选择都不好的时候，选那个能保住更多人性命的。"
   2330|             player "通知王后——艾登堡愿意效忠。"
   2331|             "你做出了一个务实的选择。不光荣，但你的人和领地保住了。"
   2332|             call ending_decision_pause from _call_decision_pause_pragmatic
   2333|             jump ending_vassal
   2334| 
   2335|         "加入男爵联军，对抗王后暴政|与男爵会师，正面迎战王后军（风险较高）→ 铁腕领主" if _resist_available:
   2336|             $ ending_type = "iron_lord"
   2337|             $ resist_route = True
   2338|             $ log_decision("第五章", "选择加入男爵联军反抗")
   2339|             player "王后的统治建立在谎言和暴力之上。是时候终结了。"
```

### 候选 11 — chapter5.rpy:2694(第五章·结局段, 忠诚≥70)

**选项**: 「亲自跪在老人面前——以你的名义起誓重建」  
**label**: `ending_iron_lord`  
**完整条件**: `if loyalty >= 70:`  
**入选理由**: 跪在老人面前起誓重建——忠诚线的情感顶点, 高阈值+强演出

```renpy
   2664|             $ change_stat("power", 2)
   2665|             $ iron_war_score += 3
   2666|             $ change_rel("rel_captain", 4)
   2667|             $ hide_all_chars()
   2668|             "你站在山丘上，用旗语指挥部队的行动。"
   2669|             "雷恩率领前锋以精妙的战术击溃了敌军斥候。"
   2670|             "整支军队按你的旗语进退，没有一处脱节。"
   2671|             "雷恩在前头打得游刃有余。回阵时他朝山丘上的你点了点头——领主肯把刀递到他手里、自己稳坐中军，这份信他领了。代价是你没在士兵眼前露脸，这一仗的彩头记在雷恩名下，不在你头上。"
   2672| 
   2673|     "前哨战获胜后，你的军队继续推进。"
   2674| 
   2675|     "第二天，你遇到了一个被遗弃的村庄。"
   2676| 
   2677|     "房屋全烧了，田地踩烂了。一个老人坐在废墟上，茫然地看着天空。"
   2678| 
   2679|     $ hide_all_chars("farmer_rep_img")
   2680|     show farmer_rep_img at left with dissolve
   2681|     old_man "他们来了……像蝗虫一样……拿走了一切……"
   2682| 
   2683|     $ hide_all_chars("player_char_img")
   2684|     show player_char_img at left with dissolve
   2685|     player "是谁干的？"
   2686| 
   2687|     $ hide_all_chars("farmer_rep_img")
   2688|     show farmer_rep_img at left with dissolve
   2689|     old_man "穿铠甲的人……我分不清是哪边的……对我们来说都一样……"
   2690| 
   2691|     "你看着老人，又看了看他身后烧塌的房屋。"
   2692| 
   2693|     menu:
>> 2694|         "亲自跪在老人面前——以你的名义起誓重建" if loyalty >= 70:
   2695|             $ change_stat("loyalty", 5)
   2696|             $ change_stat("reputation", 5)
   2697|             $ change_stat("power", -6)
   2698|             $ hide_all_chars("player_char_img")
   2699|             show player_char_img at left with dissolve
   2700|             player "老人家。"
   2701|             "你下马， 单膝跪在他面前。"
   2702|             player "我以艾登堡领主的名义起誓——这场仗打完， 我亲自带石匠回来。"
   2703|             player "你的房子会有屋顶。你的田会有人翻。你儿子的坟前会有人烧纸。"
   2704|             $ hide_all_chars()
   2705|             "老人愣了。然后他握住你的手， 说不出话， 只是流泪。"
   2706|             "周围的士兵静下来了。他们看见领主单膝跪在一个庄稼老汉面前。"
   2707|             "雷恩站在马边没动。这位打了十二年仗的老兵心里清楚：肯为一个老人下跪的领主，士兵会替他卖命；可下跪这件事本身，也让一些人记住了——原来这位领主也会跪。"
   2708| 
   2709|         "留下食物和士兵守这里":
   2710|             $ change_stat("loyalty", 3)
   2711|             $ change_stat("power", -1)
   2712|             $ iron_war_score -= 3
   2713|             $ hide_all_chars("player_char_img")
   2714|             show player_char_img at left with dissolve
   2715|             player "留十个人在这里。帮老百姓重建家园。"
   2716|             hide player_char_img
   2717|             $ hide_all_chars("captain_img")
   2718|             show captain_img at left with dissolve
   2719|             captain "但领主大人，我们的兵力本就不——"
   2720|             hide captain_img
   2721|             $ hide_all_chars("player_char_img")
   2722|             show player_char_img at left with dissolve
   2723|             player "执行命令。"
   2724|             "十个人，加上半车干粮，从北上的队列里被划了出去。雷恩没再争——他只是在花名册上勾掉了那十个名字。这一队人马，三天后的旷野上你是用不上了。"
```

### 候选 12 — chapter5.rpy:5080(第五章·结局段, 谋略≥60)

**选项**: 「动用整张情报网——把附和者的底册当场摊开|烧掉多年暗线，换一场干净的胜利」  
**label**: `ending_truth`  
**完整条件**: `if intrigue >= 60:`  
**入选理由**: 烧掉整张情报网换一场干净的胜利——真相结局的代价型选项, 本身就带机会成本叙事

```renpy
   5050|             show player_char_img at left with dissolve
   5051|             player "够了，王后。你的功绩不能为你赎罪。"
   5052|             player "篡改遗诏是叛国。毒杀忠良是谋杀。无论动机如何，罪就是罪。"
   5053|             player "在场的各位是见证人——今天，正义不会再缺席。"
   5054| 
   5055|     $ hide_all_chars()
   5056| 
   5057|     python:
   5058|         ## 困难模式 + 声望/铁证不足 → 真相压不住一个掌权二十年的王后, 只能靠强硬手段惨胜。
   5059|         ## (2026-06-16 秦霸先反馈: 真相大白是唯一不吃难度的主结局, 困难一次过。
   5060|         ##  普通/简单仍走干净胜利, 不锁玩家; 仅困难下根基不够时付代价。)
   5061|         _truth_weight = reputation + intrigue // 2
   5062|         if poison_evidence:
   5063|             _truth_weight += 20
   5064|         if prince_ally and not prince_betrayed and rel_prince >= 25:
   5065|             _truth_weight += 20
   5066|         if dark_lily_joined:
   5067|             _truth_weight += 10
   5068|         _truth_contested = (persistent.difficulty == "hard" and _truth_weight < 85)
   5069| 
   5070|     if _truth_contested:
   5071|         "王后没有立刻屈服。"
   5072| 
   5073|         "她环顾大厅，去找那些还没有低头的人——而她找到了几个。"
   5074| 
   5075|         "「老领主的冤屈该查。可蛮族就压在边境上，这个节骨眼上动摇王后，谁来收场？」北境一位领主开了口，附和声跟着响起来。"
   5076| 
   5077|         "你压不住这股动摇。光靠一份二十年前的遗诏，撼不动一个掌权二十年的人。"
   5078| 
   5079|         menu:
>> 5080|             "动用整张情报网——把附和者的底册当场摊开|烧掉多年暗线，换一场干净的胜利" if intrigue >= 60:
   5081|                 $ change_stat("intrigue", -20)  ## 消耗大轮 Phase 2.2: 把柄当众用掉 = 暗线全部作废
   5082|                 "你朝艾琳娜看了一眼。她会意，从袖中抽出一叠早已备好的条陈，一份一份传下去。"
   5083| 
   5084|                 "谁收过王后的年金，谁家的关税少缴了七年，谁的次子在王都的军职是怎么来的——每一份，都对着一个刚才开口的人。"
   5085| 
   5086|                 "大厅重新安静下来。这一次不是被你压住的——是每个开过口的人都发现，自己的底册也在别人手里。"
   5087| 
   5088|                 "代价你自己清楚：把柄见了光就是废纸。你经营多年的那张网，今天一口气花完了。"
   5089| 
   5090|             "把话说重——点名旧账，逼他们闭嘴":
   5091|                 "你只能把话说重——点名那几个收过王后好处的领主，把当年的旧账一笔笔翻出来，逼他们把嘴闭上。"
   5092| 
   5093|                 "大厅安静了下来。你赢了，可赢得难看。在场的人都记住了你逼人就范的那副样子。"
   5094| 
   5095|                 $ change_stat("reputation", -8)
   5096|                 $ change_stat("loyalty", -4)
   5097|     else:
   5098|         "王后沉默了很长时间。"
   5099| 
   5100|         "她的目光掠过大厅里的每一张脸——她在寻找支持者。"
   5101| 
   5102|         "但她看到的只有回避的目光和低下的头。二十年的恩威并施，在铁证面前轰然崩塌。"
   5103| 
   5104|     hide player_char_img
   5105|     $ hide_all_chars("queen_img")
   5106|     show queen_img at left with dissolve
   5107|     queen "……"
   5108| 
   5109|     $ hide_all_chars()
   5110|     "她重新坐回王座。这次坐得端正，背挺得直。"
```

---

## 四、相关系统摸底

### 4.1 属性阶位(attr_system.rpy:19-146)

每属性 5 阶, 阈值固定 **0-19 / 20-39 / 40-59 / 60-79 / 80-100**(get_tier, :134)。阶位中文名(权力示例): 手无缚鸡→初显锋芒→铁腕领主→威震一方→无人能敌; 六属性各有一套名称与配色(TIER_DATA)。跨越 20/40/60/80 阈值时弹阶位叙事(TIER_CROSS_NARRATIVE, 升降各一条文案)。

对照门控阈值分布: 45-58 的门槛都落在第 3 阶(40-59)内部, 60/65/70 落在第 4 阶——即「亮出选项但走失败分支」的展示文案可以直接借用阶位名(如「铁腕领主可尝试/威震一方方可稳操」)。

「声望姿态」: 无独立系统。与之最接近的是三类立场 flag(见下表 council_stance 等)与 REL_STATES 关系七态(死敌→誓盟, attr_system.rpy:419-427)。

### 4.2 属性成长链条(改阈值前必读)

attr_system.rpy:205-236 的注释块(2026-07-15 实测)确认: 本文件的 change_stat 是**死代码**, 实际链条为 difficulty.rpy:94 的难度倍率(easy×1.5/normal×1.0/hard×0.7)→递减收益(0-40:100%|40-60:70%|60-80:40%|80+:20%)→effects.rpy:220 的直加+clamp。全项目 1158 个 change_stat 调用点。80+ 为软顶。

### 4.3 骰子判定复用点

attr_system.rpy:166 `dice_check(stat_name, difficulty)` 与危机判定同公式(1d10+bonus, bonus=(stat-30)//10 clamp -3..+7), 带大成功/大失败判定(±4)。「失败分支判定」可直接复用它而不必新写。

### 4.4 可作「语境修正」来源的现成剧情 flag(10 例)

全项目 flag 走 default + `$ x = True` 全局变量(不用 persistent; persistent 仅用于 gallery/成就等元进度)。已有先例: chapter4.rpy:2966 `_stealth_diff = 2 if dark_lily_joined else 4` 用 flag 改危机难度。

| flag | 含义 | 在哪章 set |
|---|---|---|
| deep_mother_herb | 序章母亲药草三选("poison"/"healing"/"question"), 定调主角底色 | 序章 prologue_deepening.rpy:105/143/176 |
| father_was_regent_known | 已知父亲曾是摄政(主线核心真相) | 第二章末 chapter2.rpy:3445; 第三章书房 chapter3.rpy:1062; 第四章 chapter4_expansion.rpy:1345; NPC线 npc_depth.rpy:616、npc_sidelines.rpy:775/838 |
| poison_evidence | 掌握毒杀证据 | 第二章 chapter2.rpy:2424; 第三章 chapter3.rpy:1108/2814; 幕间 interludes.rpy:1439 |
| dark_lily_joined | 与暗百合建立关系(加入/铁刺/合作任一路径) | 第三章 chapter3.rpy:2951/3005/3050、chapter3_expansion.rpy:1427 |
| lily_full_member | 正式入会(仅"加入影卫/铁刺"; "合作"为 False) | 第三章 chapter3.rpy:3006/3051 |
| eagle_intel | 觐见前收到信网情报 | 第四章 chapter4.rpy:958(已被 :1429 菜单条件当语境用) |
| alliance_church | 与教会公开结盟 | 第四章末 chapter4.rpy:3634(已被 ch5_expansion:322/2275 当替代门槛用) |
| council_stance | 北疆议会对你的立场("fear"/"respect"/"scorn") | 北境扩展 northern_expansion.rpy:23 定义 |
| southern_first_impression | 南境初见姿态("polite"/"wary"/"blunt") | 南境扩展 southern_expansion.rpy:850/872/896(已被 :1446 当替代门槛用) |
| port_insight / evidence_count | 渐进计数器: 对潮汐港了解度(0-6) / 费舍尔证据数 | 南境扩展 southern_expansion.rpy 多点 +=1(已被 :1110/:1438 当替代门槛用) |

另有一组「立场三选」flag 同构可用: ch1_exp_council_stance(aggressive/cautious/balanced)、ch2_exp_tax_stance(reform/maintain/compromise)、ch2_exp_border_stance、ch2_exp_trade_stance、deep_marcus_confession(forgive/distance/exploit)。

**关键观察**: southern_expansion.rpy 的四个门控点全部已是「属性 OR 剧情flag」的复合条件——语境修正的设计范式在最新的南境内容里已经自发出现, 改造等于把这种写法制度化并回填到 1-5 章的 114 个纯属性门控上。

