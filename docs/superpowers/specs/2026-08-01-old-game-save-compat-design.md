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
- 守卫用 `pickletools` 模拟基础栈操作；遇到 `STACK_GLOBAL`、`REDUCE`、`NEWOBJ` 时只放入不透明哨兵，绝不导入、构造或调用二进制指定的对象。
- 必需的 generation 必须实际出现在对应脚本节点的 `Node.name_version` 中，不能只是在任意整数操作码中偶然出现。
- `Tools/old_game_required_nodes.py` 只保存节点 ID 与来源哈希，不含序列化玩家状态。它精确覆盖曾在 fresh 3.9.2 中加载失败的 `7-1-LT1.save` 所引用的 129 个节点，包括 pickle 中不显式保存、由 `IntegerSlot` 默认恢复为 `0` 的 serial-zero 节点。
- 回归测试会受控改写一个 serial-zero 节点，同时保留同一 generation 的其他节点，证明旧的“只查 generation”方式会假绿，而精确节点检查会失败。

任何新增、删除或重命名 `.rpy` 都会使守卫失败，提醒发布者先更新 `old-game`。

静态节点检查不是旧档兼容性的最终证明。旧存档的 rollback 日志可能引用已删除节点；Ren'Py 可以丢弃部分无法解析的旧回滚项，不能把“日志里出现过”一律当成加载硬依赖。例如受支持的 3.9 `7-8-LT1.save` 有 6 个旧回滚节点不在当前 `prologue.rpyc` 中，但真实加载仍可完成。因此三份受支持旧档都必须再过带锚点的运行时冒烟。

## 后续发布流程

每次准备发布会影响脚本节点的版本时：

1. 从已提交的 `old-game` 开始，不得清空后 fresh 编译。
2. 正常修改并完成全套测试。
3. 用官方 `launcher update_old_game` 刷新兼容基线。
4. 运行 `python -B -m unittest Tools.test_old_game_compat -v`。
5. 对以下三份旧档逐一做隔离自动加载冒烟；不得把真实 `.save` 提交进仓库：
   - `7-1-LT1.save`，SHA256 `9AEBCE6B73C2F20C3E668F2B45C58AA0FB75EA56813F59C7D5948E0BEF68867C`
   - `7-8-LT1.save`，SHA256 `317E71C7B6814242A568065404A3D4EC990C8DEBA8ADE82EB5854B620447B350`
   - `auto_ch-southern-LT1.save`，SHA256 `0F7C82FB2F40250D1A8F66B3176025D3D5C0B92B0B3EBD81914F4991A06CA024`

   每份旧档使用全新 savedir 和副本，通过 `RENPY_AUTO_LOAD` 加载；临时测试探针必须在 `after_load` 回调链中写出唯一 marker。门禁同时要求 marker 存在、日志无 `traceback`/`incompatible`、原始旧档哈希不变，并在结束后恢复及复核所有受保护 persistent。只看到窗口或 `Interface start` 不能算通过。
6. 提交更新后的 `old-game`；继续禁止提交 `game/*.rpyc`、缓存、存档、日志和测试截图。

Ren'Py 默认构建规则将项目根 `old-game/` 分类为 `None`，不会放进 Windows 或 Android 玩家包。它是仓库内的编译输入，不是发行载荷；正式候选包仍需检查一次，确认包内没有 `old-game/`。

## 资产影响

本改动只增加 Ren'Py 技术兼容数据、Python 守卫和说明文档，不改变玩家可见内容。无需新增或替换美术、音乐、音效、动画或 UI 资产。`old-game/` 与 `**.py` 有明确排除规则，但说明文档可能被当前默认分类收进玩家包，因此不能预先声称发行包增量为 0；Windows 与 Android 候选包完成后必须测量实际差分。
