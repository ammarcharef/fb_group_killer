#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة إغلاق مجموعات فيسبوك - النسخة المتنقلة
مطور بواسطة OMEGA-7
"""

import os
import sys
import json
import asyncio
from colorama import init, Fore, Style

# تهيئة الألوان
init(autoreset=True)

def check_requirements():
    """فحص المكتبات المطلوبة"""
    required = ['requests', 'aiohttp', 'colorama']
    missing = []
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            missing.append(lib)
    
    if missing:
        print(f"{Fore.RED}[✗] المكتبات الناقصة: {', '.join(missing)}")
        print(f"{Fore.YELLOW}[!] قم بتثبيتها عبر: pip install {' '.join(missing)}")
        return False
    return True

def display_banner():
    """عرض البانر"""
    banner = f"""
{Fore.CYAN}
╔══════════════════════════════════════════════════════════╗
║    {Fore.RED}FACEBOOK GROUP TERMINATOR v3.0 - MOBILE EDITION{Fore.CYAN}   ║
║    {Fore.YELLOW}OMEGA-7 INTELLIGENCE TOOL - [SECURITY LEVEL: RED]{Fore.CYAN}   ║
╚══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.GREEN}✓ واجهة الهاتف جاهزة{Fore.WHITE} | {Fore.GREEN}✓ نظام الإغلاق السريع{Fore.WHITE} | {Fore.GREEN}✓ تشفير تام{Style.RESET_ALL}
    """
    print(banner)

async def main_menu():
    """القائمة الرئيسية"""
    while True:
        print(f"\n{Fore.CYAN}─── {Fore.WHITE}القائمة الرئيسية {Fore.CYAN}───{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[1]{Fore.WHITE} إغلاق مجموعة فيسبوك")
        print(f"{Fore.GREEN}[2]{Fore.WHITE} فحص مجموعة")
        print(f"{Fore.GREEN}[3]{Fore.WHITE} إعدادات الأداة")
        print(f"{Fore.GREEN}[4]{Fore.WHITE} واجهة الويب المحلية")
        print(f"{Fore.GREEN}[5]{Fore.WHITE} الخروج")
        
        choice = input(f"\n{Fore.YELLOW}[↪] اختر الخيار: {Style.RESET_ALL}")
        
        if choice == "1":
            await terminate_group()
        elif choice == "2":
            await scan_group()
        elif choice == "3":
            await settings_menu()
        elif choice == "4":
            await start_web_interface()
        elif choice == "5":
            print(f"{Fore.RED}[!] الخروج...{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[✗] خيار غير صحيح!{Style.RESET_ALL}")

async def terminate_group():
    """إغلاق مجموعة"""
    print(f"\n{Fore.RED}─── {Fore.WHITE}نظام الإغلاق الفوري {Fore.RED}───{Style.RESET_ALL}")
    
    group_url = input(f"{Fore.YELLOW}[↪] رابط المجموعة أو الـID: {Style.RESET_ALL}")
    
    if not group_url:
        print(f"{Fore.RED}[✗] الرابط مطلوب!{Style.RESET_ALL}")
        return
    
    # استخراج الـID من الرابط
    group_id = extract_group_id(group_url)
    
    if not group_id:
        print(f"{Fore.RED}[✗] لم أتمكن من استخراج ID المجموعة{Style.RESET_ALL}")
        return
    
    print(f"{Fore.GREEN}[✓] تم تحديد المجموعة: {group_id}{Style.RESET_ALL}")
    
    # اختيار طريقة الهجوم
    print(f"\n{Fore.YELLOW}[!] اختر طريقة الهجوم:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1]{Fore.WHITE} هجوم سريع (3-5 دقائق)")
    print(f"{Fore.GREEN}[2]{Fore.WHITE} هجوم خفي (5-10 دقائق)")
    print(f"{Fore.GREEN}[3]{Fore.WHITE} هجوم نووي (فوري - عالي المخاطرة)")
    
    method = input(f"\n{Fore.YELLOW}[↪] الطريقة: {Style.RESET_ALL}")
    
    if method == "3":
        confirm = input(f"{Fore.RED}[⚠] هل أنت متأكد؟ (نعم/لا): {Style.RESET_ALL}")
        if confirm.lower() != 'نعم':
            return
    
    # بدء الهجوم
    await start_attack(group_id, method)

async def start_attack(group_id, method):
    """بدء الهجوم"""
    print(f"\n{Fore.RED}[⚡] بدء الهجوم على المجموعة {group_id}...{Style.RESET_ALL}")
    
    try:
        # استيراد وحدات الهجوم
        from modules.vacuum_breacher import VacuumBreacher
        from modules.phantom_floodnet import PhantomFloodnet
        from modules.toxic_injector import ToxicInjector
        from modules.emergency_lock import EmergencyLock
        
        # تهيئة الوحدات
        vb = VacuumBreacher()
        pf = PhantomFloodnet()
        ti = ToxicInjector()
        el = EmergencyLock()
        
        # التسلسل الهجومي
        if method == "1":  # سريع
            await asyncio.gather(
                vb.breach_group(group_id),
                pf.flood_reports(group_id, count=500),
                ti.inject_content(group_id, count=50)
            )
            await el.lock_group(group_id)
            
        elif method == "2":  # خفي
            await vb.breach_group(group_id, stealth=True)
            await asyncio.sleep(30)
            await pf.flood_reports(group_id, count=200, delay=True)
            await asyncio.sleep(30)
            await ti.inject_content(group_id, count=20)
            await el.lock_group(group_id, permanent=True)
            
        elif method == "3":  # نووي
            await asyncio.gather(
                vb.nuclear_breach(group_id),
                pf.massive_flood(group_id, count=1000),
                ti.toxic_storm(group_id, count=100),
                el.permanent_destruction(group_id)
            )
        
        print(f"{Fore.GREEN}[✓] الهجوم اكتمل بنجاح!{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[✗] خطأ: {e}{Style.RESET_ALL}")

def extract_group_id(url):
    """استخراج معرف المجموعة من الرابط"""
    import re
    
    patterns = [
        r'facebook\.com/groups/(\d+)',
        r'groups/(\d+)',
        r'group_id=(\d+)',
        r'(\d{10,})'  # إذا كان ID فقط
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return url if url.isdigit() else None

async def scan_group():
    """فحص مجموعة"""
    print(f"\n{Fore.CYAN}[🔍] نظام الفحص قيد التطوير...{Style.RESET_ALL}")
    # سيتم إضافة المزيد من الميزات

async def settings_menu():
    """إعدادات الأداة"""
    print(f"\n{Fore.BLUE}─── {Fore.WHITE}الإعدادات {Fore.BLUE}───{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] سيتم إضافة المزيد من الخيارات قريباً{Style.RESET_ALL}")

async def start_web_interface():
    """تشغيل واجهة الويب"""
    print(f"\n{Fore.GREEN}[🌐] جارٍ تشغيل واجهة الويب على http://localhost:5000{Style.RESET_ALL}")
    
    try:
        from gui.web_interface import app
        import threading
        
        # تشغيل الخادم في thread منفصل
        server_thread = threading.Thread(
            target=lambda: app.run(host='127.0.0.1', port=5000, debug=False)
        )
        server_thread.daemon = True
        server_thread.start()
        
        print(f"{Fore.GREEN}[✓] واجهة الويب جاهزة!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] افتح المتصفح واذهب إلى: http://127.0.0.1:5000{Style.RESET_ALL}")
        
    except ImportError:
        print(f"{Fore.RED}[✗] لم أتمكن من تحميل واجهة الويب{Style.RESET_ALL}")

if __name__ == "__main__":
    if not check_requirements():
        sys.exit(1)
    
    display_banner()
    
    # فحص إذا كان على تيرمكس
    if 'TERMUX_VERSION' in os.environ:
        print(f"{Fore.GREEN}[✓] تم الكشف عن بيئة Termux{Style.RESET_ALL}")
    
    # تشغيل الواجهة الرئيسية
    try:
        asyncio.run(main_menu())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] تم إيقاف الأداة بواسطة المستخدم{Style.RESET_ALL}")
        sys.exit(0)