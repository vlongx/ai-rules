# AI Rules

<p align="center"><img src="icon/ai-rules-icon.svg" alt="AI Rules icon" width="160" /></p>

全球 AI 服务分流规则合集。独立整理，参考 [VPSDance/ai-proxy-rules](https://github.com/VPSDance/ai-proxy-rules) 的目录结构。

## 支持服务

原有 41 组服务保持不变，另增加一份 Haxhork/DeveloperBeta 扩展规则（统一订阅目前包含 313 条去重规则），包括 ChatGPT、OpenAI、Codex、Sora、Claude、Gemini、Grok、Meta AI / Muse、Suno、Perplexity、Cursor、Manus、Midjourney 等。

## Surge 统一订阅

```ini
[Rule]
RULE-SET,https://raw.githubusercontent.com/vlongx/ai-rules/main/rules/surge/all.list,AI-Proxy
```

`AI-Proxy` 改成你实际存在的 Surge 策略组名称；规则需放在 `FINAL` 之前。

单独订阅 Suno：

```ini
RULE-SET,https://raw.githubusercontent.com/vlongx/ai-rules/main/rules/surge/suno.list,AI-Proxy
```


## Haxhork AI.list 合并扩展

已将 [Haxhork/DeveloperBeta AI.list](https://raw.githubusercontent.com/Haxhork/DeveloperBeta/refs/heads/main/Surge/Ruleset/AI.list) 的规则按原始语义**全部纳入**统一订阅：原文件 245 条，源文件自身重复 2 条，已有规则完全重复 23 条，新增 220 条，统一订阅共 313 条。现有 41 个独立服务规则保持不变。

- `rules/surge/extensions/haxhork.list`：仅保存来自该来源、此前没有的 220 条规则（含 `AND`、`IP-CIDR` 和 `IP-CIDR6`）。
- `rules/surge/all.list`：自动订阅入口，已包含该扩展，无需在 Surge 中再单独添加扩展订阅，避免重复匹配。
- `scripts/validate.py`：校验普通域名、逻辑规则、IPv4/IPv6 CIDR 格式与合并一致性。

规则以 2026-11-12 读取的来源内容为静态快照，并非自动跟随上游更新。部分 AI API 域名属于中国或其他服务商，启用统一规则后也会走用户指定的 AI 策略组；请按 Surge 请求记录检查实际线路。规则仅用于分流，不保证所有上游端点持续有效。

## 可选 Apple 服务分流（与 AI 规则独立）

截图中的 Apple 服务规则另存于 `rules/surge/optional/apple-services.list`，**不会合入 AI 统一订阅**，也不会影响原有 41 组 AI 服务。

在 Surge 配置的 `[Rule]` 下，按需添加（将 `PROXY` 改成已有的策略组名称）：

```ini
RULE-SET,https://raw.githubusercontent.com/vlongx/ai-rules/main/rules/surge/optional/apple-services.list,PROXY
```

规则涵盖 Apple 软件更新、商店、iCloud 与 Siri 等相关域名。原截图中的 `chatgpt.com`、`openai.com` 已存在于 AI 总规则中，不重复加入 Apple 列表。此列表使用无策略字段的 Surge RULE-SET 格式；不应在独立列表内写 `,PROXY`。

**提醒：** 代理路由不等于阻止软件更新，也不能保证消除设置 App 的更新红色角标。把 iCloud、Apple Store、设备配置、Siri 等服务强制走代理可能影响正常使用；建议只在明确需要时开启。 `DOMAIN-KEYWORD,siri` 匹配范围较广，应特别留意误匹配。

## 项目结构

- `rules/surge/all.list`：所有 AI 服务合并规则（不含代理策略）
- `rules/surge/<service>.list`：独立服务规则
- `rules/surge/extensions/haxhork.list`：第三方 AI 来源补充规则（已合并到 all.list）
- `services.json`：服务名清单
- `scripts/validate.py`：规则格式及一致性校验
- `.github/workflows/validate.yml`：GitHub Actions 自动校验

## 注意事项

域名为初始参考集合，并非持续探测的实时完整清单。服务认证、CDN、WebSocket 和客户端请求可能需要按 Surge 日志增补。

`muse.ai` 保留参考项目规则，但未独立证实为 Meta Muse 官方专属域名。尽量不纳入 `google.com`、`github.com`、`stripe.com` 等共享域名，避免影响其他业务。

鸣谢：[VPSDance/ai-proxy-rules](https://github.com/VPSDance/ai-proxy-rules)。本项目不是其官方版本。
