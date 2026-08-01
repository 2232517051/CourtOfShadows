# Ren'Py 旧存档脚本谱系兼容设计

## 问题与目标

3.9.1 的真实存档在只保留当前源码、重新生成 `game/*.rpyc` 的 3.9.2 环境中，会在回滚日志解冻阶段报错：

```text
Could not load the game. Perhaps the script changed in an incompatible way.
```

同一存档在保留历史 `.rpyc` 的环境中可以继续加载。根因不是业务字段迁移，而是发布仓库忽略了 `game/**/*.rpyc`，同时没有保存 Ren'Py 用来继承旧脚本节点名的 `old-game` 基线。目标是让干净检出也能生成与 3.9、3.9.1 存档兼容的 3.9.2 脚本谱系。

## 唯一可信种子

旧谱系只能从已经交付给玩家的正式 3.9.1 Windows 包取得：

- 文件：`E:\Projects\renpy-8.5.2-sdk\CourtOfShadows-3.9.1-dists\CourtOfShadows-3.9.1-win.zip`
- SHA256：`A2B4337642827E57B9EFAC4765FD9E68597D98A8404A023D8B9565E56EF0B1A4`
- 包内路径：`CourtOfShadows-3.9.1-win/game/**/*.rpyc`
- 种子数量：55
- 种子总大小：3,875,200 bytes

不得用一次 fresh 3.9.2 编译产生的 `.rpyc` 反向充当种子；那批文件已经丢失玩家存档引用的旧节点名。

## Ren'Py 官方机制

Ren'Py 8.5.2 编译每个 `.rpy` 时，会按顺序读取项目根 `old-game` 中对应的 `.rpyc`、再读取现有 `game/*.rpyc`，把旧节点名合并进新语法树，最后才为新增节点分配名字。因此第一次修复必须按以下顺序执行：

1. 校验正式包 SHA256。
2. 只将正式包中的 55 个 `game/**/*.rpyc` 提取到项目根 `old-game/`，保留相对路径。
3. 强制编译当前 3.9.2 源码，使当前 `game/*.rpyc` 继承 3.9.1 谱系。
4. 执行官方 launcher 命令：

   ```powershell
   E:\Projects\renpy-8.5.2-sdk\renpy.exe E:\Projects\renpy-8.5.2-sdk\launcher update_old_game <project>
   ```

   该命令会以 `compile --keep-orphan-rpyc` 重编译，再把当前脚本编译结果刷新到项目根 `old-game/`。

当前源码共 56 个 `.rpy`；3.9.2 新增的 `new_run.rpy` 在刷新后补齐，因此最终必须提交 56 个 `old-game/**/*.rpyc`。其中 `old-game/script.rpyc` 必须保留 generation `1297438350`，`old-game/chapter2.rpyc` 必须保留 generation `1297438144`，这两个值来自真实旧档。

## 自动守卫

`Tools/test_old_game_compat.py` 不反序列化、不执行二进制内容，只做安全的结构检查：

- 当前 56 个 `game/**/*.rpy` 必须在 `old-game` 中有同相对路径的 `.rpyc`，且不得多出陈旧脚本。
- 每个文件必须是 RPYC2，slot 1 必须能解压，并能由标准库 `pickletools` 完整扫描到 `STOP`。
- 两个真实旧档所需的 generation 必须仍在对应脚本中。

任何新增、删除或重命名 `.rpy` 都会使守卫失败，提醒发布者先更新 `old-game`。

## 后续发布流程

每次准备发布会影响脚本节点的版本时：

1. 从已提交的 `old-game` 开始，不得清空后 fresh 编译。
2. 正常修改并完成全套测试。
3. 用官方 `launcher update_old_game` 刷新兼容基线。
4. 运行 `python -B -m unittest Tools.test_old_game_compat -v`。
5. 用仍在支持范围内的真实旧档做隔离自动加载冒烟。
6. 提交更新后的 `old-game`；继续禁止提交 `game/*.rpyc`、缓存、存档、日志和测试截图。

Ren'Py 默认构建规则将项目根 `old-game/` 分类为 `None`，不会放进 Windows 或 Android 玩家包。它是仓库内的编译输入，不是发行载荷；正式候选包仍需检查一次，确认包内没有 `old-game/`。

## 资产影响

本改动只增加 Ren'Py 技术兼容数据和测试，不改变玩家可见内容。无需新增或替换美术、音乐、音效、动画或 UI 资产；按默认构建规则，发行包大小增量应为 0 bytes。
