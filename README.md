# GoldAI 自動黃金通知系統

此專案為每日自動發送黃金價格快報到 Email + Telegram。

## 如何部署（Render）

1. 上傳此 repo 至你的 GitHub
2. 打開 https://render.com
3. 登入後點「New +」→ 選「Web Service」
4. 選擇你的 GitHub Repo，Render 會自動讀取 render.yaml
5. 部署後每天自動執行 main.py → 發出通知

## Secrets 環境變數（Render → Environment）

- TELEGRAM_TOKEN
- TELEGRAM_CHAT_ID
- EMAIL_USER
- EMAIL_PASS
- EMAIL_RECEIVER
