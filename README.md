# 📧 自动邮件发送系统 (Auto Email Sender)

这是一个基于 Python 的自动化邮件发送工具，专为 Gmail 设计。它支持：
1.  自动定时发送邮件。
2.  发送包含图片附件的邮件。
3.  自定义发送频率和持续时间。

## ✨ 功能特点

- **自动化**: 启动后自动运行，无需人工干预。
- **支持附件**: 可在配置文件中指定要发送的图片。
- **安全配置**: 使用 `.env` 文件管理敏感信息，保护你的账号密码。
- **实时反馈**: 控制台实时显示发送状态和日志。

## 🛠️ 环境要求

- Python 3.6 或更高版本
- Gmail 账号

## 🚀 快速开始

### 1. 安装依赖

首先，确保你安装了 Python。然后在终端中运行以下命令安装必要的库：

```bash
pip install -r requirements.txt
```

### 2. 配置 Gmail 应用专用密码 (重要！)

为了安全起见，Google 不允许第三方应用直接使用你的登录密码。你需要生成一个"应用专用密码"：

1.  登录你的 Google 账号。
2.  访问 **[Google 账户安全性页面](https://myaccount.google.com/security)**。
3.  确保你已经开启了 **两步验证 (2-Step Verification)**。
4.  在"两步验证"下方，找到并点击 **应用专用密码 (App passwords)**（如果找不到，请在页面顶部的搜索栏搜索 "App passwords"）。
5.  应用名称随便填（例如 "Python Mail Sender"），点击 **创建 (Create)**。
6.  复制生成的 **16位字符密码**（不需要空格）。

### 3. 设置配置文件

1.  将项目中的 `env_template.txt` 重命名为 `.env`：
    ```bash
    mv env_template.txt .env
    ```
2.  用文本编辑器打开 `.env` 文件，填入你的信息：

```ini
# 发送方 Gmail 地址
SENDER_EMAIL=你的邮箱@gmail.com
# 刚刚生成的16位应用专用密码
SENDER_PASSWORD=xxxx xxxx xxxx xxxx
# 接收方邮箱
RECIPIENT_EMAIL=接收者@example.com
# 邮件内容配置
EMAIL_SUBJECT=测试邮件标题
EMAIL_BODY=这是邮件的正文内容
# (可选) 附件图片路径，如 ./photo.jpg
ATTACHMENT_PATH=
```

### 4. 运行程序

在终端中运行：

```bash
python main.py
```

## ⚙️ 高级设置

### 如何修改发送频率和持续时间？

打开 `main.py` 文件，找到 `main` 函数中的以下部分进行修改：

```python
    # --- 用户配置区域 ---
    # 在这里修改持续时间和发送间隔
    RUN_HOURS = 3          # 持续运行小时数 (例如改为 1 就是运行1小时)
    INTERVAL_SECONDS = 60  # 发送间隔秒数 (例如改为 300 就是每5分钟发一次)
    # ------------------
```

### 如何发送图片附件？

1.  准备好你的图片文件（例如 `my_photo.jpg`）。
2.  在 `.env` 文件中，设置 `ATTACHMENT_PATH` 的值。
    *   如果图片和代码在同一目录，直接写文件名：`ATTACHMENT_PATH=my_photo.jpg`
    *   或者写绝对路径：`ATTACHMENT_PATH=/Users/xujiaqi/Desktop/photos/cat.jpg`

## ⚠️ 注意事项

- 请勿将包含真实密码的 `.env` 文件上传到 GitHub。
- 过于频繁的发送可能会触发 Gmail 的反垃圾邮件限制，建议间隔不要太短。

## 📦 推送到 GitHub

如果你想将此项目推送到你的 GitHub 仓库：

```bash
git add .
git commit -m "update: add attachment support and config guide"
git push
```
