#!/data/data/com.termux/files/usr/bin/bash

echo "[+] تثبيت Facebook Group Terminator"
echo "[+] جارٍ التحديث..."

pkg update -y
pkg upgrade -y

echo "[+] تثبيت Python والمكتبات..."
pkg install python -y
pkg install python-pip -y
pkg install git -y

echo "[+] تثبيت المكتبات المطلوبة..."
pip install requests aiohttp colorama beautifulsoup4 lxml flask

echo "[+] تنزيل الأداة..."
git clone https://github.com/example/fb_group_killer.git
cd fb_group_killer

echo "[+] منح الصلاحيات..."
chmod +x main.py
chmod +x gui/termux_ui.py

echo "[+] إعداد الملفات..."
mkdir -p config
echo "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36" > config/user_agents.txt
echo "proxy1.example.com:8080" > config/proxies.txt
echo "{}" > config/accounts.json

echo "[+] الانتهاء!"
echo "[+] لبدأ الأداة: cd fb_group_killer && python main.py"
echo "[+] لواجهة تيرمكس: python gui/termux_ui.py"