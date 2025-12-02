import smtplib
import time
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def send_email(sender, password, recipient, subject, body, attachment_path=None):
    """发送单封邮件的函数，支持图片附件"""
    try:
        # 构建邮件对象
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # 处理图片附件
        if attachment_path and os.path.exists(attachment_path):
            try:
                with open(attachment_path, 'rb') as f:
                    img_data = f.read()
                    image = MIMEImage(img_data, name=os.path.basename(attachment_path))
                    msg.attach(image)
                    print(f"已添加附件: {os.path.basename(attachment_path)}")
            except Exception as e:
                print(f"读取附件失败: {e}")
        elif attachment_path:
            print(f"警告: 找不到附件文件 {attachment_path}，将只发送正文。")

        # 连接 Gmail SMTP 服务器
        # 端口 587 是 TLS 标准端口
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # 开启安全传输
        server.login(sender, password)
        
        # 发送邮件
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 邮件发送成功 -> {recipient}")
        return True
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 发送失败: {e}")
        return False

def main():
    # 1. 获取配置信息
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    subject = os.getenv('EMAIL_SUBJECT')
    body = os.getenv('EMAIL_BODY')
    attachment_path = os.getenv('ATTACHMENT_PATH')

    # 2. 验证配置是否完整
    if not all([sender_email, sender_password, recipient_email]):
        print("错误: 缺少必要的配置信息。请检查 .env 文件。")
        print("请确保配置了 SENDER_EMAIL, SENDER_PASSWORD, 和 RECIPIENT_EMAIL。")
        sys.exit(1)

    print("=== 邮件自动发送系统启动 ===")
    print(f"发送方: {sender_email}")
    print(f"接收方: {recipient_email}")
    if attachment_path:
        print(f"附件: {attachment_path}")
    
    # --- 用户配置区域 ---
    # 在这里修改持续时间和发送间隔
    RUN_HOURS = 3          # 持续运行小时数
    INTERVAL_SECONDS = 60  # 发送间隔秒数 (60秒 = 1分钟)
    # ------------------
    
    print(f"计划: 每 {INTERVAL_SECONDS} 秒发送一次，持续 {RUN_HOURS} 小时")
    print("============================")

    # 3. 设置时间控制
    start_time = datetime.now()
    duration = timedelta(hours=RUN_HOURS)
    end_time = start_time + duration
    
    count = 0

    # 4. 循环发送逻辑
    while datetime.now() < end_time:
        count += 1
        print(f"\n正在发送第 {count} 封邮件...")
        
        # 发送邮件
        success = send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)
        
        # 检查是否到达结束时间，如果没到，休眠指定时间
        if datetime.now() < end_time:
            if success:
                print(f"等待 {INTERVAL_SECONDS} 秒后发送下一封...")
            else:
                print(f"发送出错，等待 {INTERVAL_SECONDS} 秒重试...")
            
            # 使用 time.sleep 进行等待
            time.sleep(INTERVAL_SECONDS)
        else:
            print(f"\n已到达设定时间 ({RUN_HOURS}小时)，停止发送。")
            break

    print(f"\n任务完成。共尝试发送 {count} 封邮件。")

if __name__ == "__main__":
    main()
