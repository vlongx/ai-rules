# AI Rules

全球 AI 服务分流规则合集。独立整理，参考 [VPSDance/ai-proxy-rules](https://github.com/VPSDance/ai-proxy-rules) 的目录结构。

## 支持服务

共 41 组，包括 ChatGPT、OpenAI、Codex、Sora、Claude、Gemini、Grok、Meta AI / Muse、Suno、Perplexity、Cursor、Manus、Midjourney 等。

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

## 项目结构

- `rules/surge/all.list`：所有 AI 服务合并规则（不含代理策略）
- `rules/surge/<service>.list`：独立服务规则
- `services.json`：服务名清单
- `scripts/validate.py`：规则格式及一致性校验
- `.github/workflows/validate.yml`：GitHub Actions 自动校验

## 注意事项

域名为初始参考集合，并非持续探测的实时完整清单。服务认证、CDN、WebSocket 和客户端请求可能需要按 Surge 日志增补。

`muse.ai` 保留参考项目规则，但未独立证实为 Meta Muse 官方专属域名。尽量不纳入 `google.com`、`github.com`、`stripe.com` 等共享域名，避免影响其他业务。

鸣谢：[VPSDance/ai-proxy-rules](https://github.com/VPSDance/ai-proxy-rules)。本项目不是其官方版本。
