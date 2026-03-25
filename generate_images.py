#!/usr/bin/env python3
import subprocess
import os
import time

# 确保在正确的目录
os.chdir(r"C:\Users\Administrator\.openclaw\workspace\bianbiang-dance\public\img")

# 定义10个图片的提示词
images = [
    {
        "filename": "news01-kaoji.jpg",
        "prompt": "中国舞蹈家协会街舞考级证书，金色奖状样式，官方认证，红色印章，专业舞蹈考级，背景简洁明亮"
    },
    {
        "filename": "news02-yikao.jpg",
        "prompt": "现代大学校园，山西风格建筑，舞蹈学院，青春活力的学生，街舞教室，专业的艺术教育环境"
    },
    {
        "filename": "news03-hiphop.jpg",
        "prompt": "Hip-hop街舞舞蹈动作，时尚潮流的年轻舞者，动感的舞蹈姿势，街头风格，彩色背景"
    },
    {
        "filename": "news04-jazz.jpg",
        "prompt": "Jazz爵士舞表演，优雅的舞者，流畅的舞蹈动作，舞台灯光，专业的舞蹈演出"
    },
    {
        "filename": "news05-competition.jpg",
        "prompt": "街舞比赛现场，舞台灯光，竞技氛围，Battle对抗，裁判评分，观众欢呼"
    },
    {
        "filename": "news06-bikeng.jpg",
        "prompt": "选择培训机构的警示牌，正确的选择，专业的舞蹈教室，学生在认真练习"
    },
    {
        "filename": "news07-breaking.jpg",
        "prompt": "Breaking霹雳舞地板动作，奥运风格，专业的地板舞者，高难度技巧，运动风格"
    },
    {
        "filename": "news08-xuexi.jpg",
        "prompt": "孩子学习街舞和读书，快乐的小朋友，街舞与学业兼顾，积极向上"
    },
    {
        "filename": "news09-urban.jpg",
        "prompt": "Urban Dance现代编舞，时尚舞蹈工作室，专业的舞者团队，现代流行音乐舞蹈"
    },
    {
        "filename": "news10-locking.jpg",
        "prompt": "Locking锁舞动作，有趣的舞蹈风格，夸张的舞蹈姿势，快乐的舞者"
    }
]

script_path = r"C:\Users\Administrator\.openclaw\workspace\skills\free-image-generation-skill\scripts\perchance_generate.py"

for i, img in enumerate(images):
    print(f"生成图片 {i+1}/10: {img['filename']}")
    cmd = [
        "python", script_path,
        "--prompt", img["prompt"],
        "--out", img["filename"],
        "--shape", "landscape"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    time.sleep(2)  # 避免请求过快

print("全部完成！")
