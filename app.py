import asyncio
import os
import threading
import urllib3
import random
import json
import base64

import discord
from discord import app_commands
from flask import Flask, request, jsonify

# Import từ các file khác
from xC4 import *
from xHeaders import *
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# ================== DISCORD SETUP ==================
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Encrypted Credit Info
_Xk9mN3pL5vR8wQ2 = "e3tZWV1bR0dDWVlbWVhYWFlYWF1cW1tbX19fXFxZWkdHQ1lZW1lYWFhZWFldXFtbWV1ZXFxaWkdHQ1lZW1lb"
_Yt4jH7qW2sD6fB1 = "WFhYWkdGRFlYV1laR0Q="
_Zc8vN5mL4pR7wS3 = "WFdZWkdEWVhXWVpHRA=="
_A1bC3dE5fG7hI9k = "WFhYWFhYWFhYWEtHWFhYVkpFRFlYWFhYWFhYWFhZR0RYWFhYWEdEWA=="

def _dEcOdE_cReDiT():
    try:
        _key = "MaFuCrEdIt2024"
        _d1 = base64.b64decode(_Xk9mN3pL5vR8wQ2.encode()).decode()
        _d2 = base64.b64decode(_Yt4jH7qW2sD6fB1.encode()).decode()
        _d3 = base64.b64decode(_Zc8vN5mL4pR7wS3.encode()).decode()
        _d4 = base64.b64decode(_A1bC3dE5fG7hI9k.encode()).decode()
        _result = {}
        _result['developer'] = ''.join(chr(ord(c) ^ ord(_key[i % len(_key)])) for i, c in enumerate(_d1))
        return _result
    except:
        return {}

CREDIT_INFO = _dEcOdE_cReDiT()

# ================== GLOBAL VARIABLES ==================
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
BOT_UID = 15900821779
bot_khangios = "bot_khangios"
key = None
iv = None
region = "VN"
TarGeT = None
acc_name = "bot_khangios"

# ================== FLASK ==================
app = Flask(__name__)

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB53"}

def get_random_color():
    colors = ["[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]"]
    return random.choice(colors)

# ================== DISCORD COMMANDS ==================
@tree.command(name="status", description="Kiểm tra trạng thái bot")
async def status(interaction: discord.Interaction):
    st = "🟢 Online" if online_writer else "🔴 Connecting"
    await interaction.response.send_message(
        f"**🤖 Free Fire Bot Status**\n\n"
        f"**Trạng thái:** {st}\n"
        f"**Tên:** `{acc_name}`\n"
        f"**Bot UID:** `{BOT_UID}`\n"
        f"**Target:** `{TarGeT}`\n"
        f"**Region:** `{region}`"
    )

@tree.command(name="5", description="Mời 5 người")
@app_commands.describe(uid="UID người nhận")
async def invite5(interaction: discord.Interaction, uid: str):
    await interaction.response.defer()
    try:
        await perform_invite_5(int(uid))
        await interaction.followup.send(f"✅ Đã gửi mời 5 người đến `{uid}`")
    except Exception as e:
        await interaction.followup.send(f"❌ Lỗi: {str(e)}")

@tree.command(name="6", description="Mời 6 người")
@app_commands.describe(uid="UID người nhận")
async def invite6(interaction: discord.Interaction, uid: str):
    await interaction.response.defer()
    try:
        await perform_invite_6(int(uid))
        await interaction.followup.send(f"✅ Đã gửi mời 6 người đến `{uid}`")
    except Exception as e:
        await interaction.followup.send(f"❌ Lỗi: {str(e)}")

@tree.command(name="help", description="Danh sách lệnh")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message("**Lệnh:**\n`/status`\n`/5 <uid>`\n`/6 <uid>`")

# ================== INVITE FUNCTIONS ==================
async def perform_invite_5(target_uid: int):
    global online_writer, key, iv, region, BOT_UID
    if not online_writer: raise Exception("Bot chưa kết nối")
    try:
        PAc = await OpEnSq(key, iv, region)
        await SEndPacKeT(None, online_writer, 'OnLine', PAc)
        C = await cHSq(5, target_uid, key, iv, region)
        await SEndPacKeT(None, online_writer, 'OnLine', C)
        V = await SEnd_InV(5, target_uid, key, iv, region)
        await SEndPacKeT(None, online_writer, 'OnLine', V)
        await asyncio.sleep(5)
        E = await ExiT(BOT_UID, key, iv)
        await SEndPacKeT(None, online_writer, 'OnLine', E)
    except Exception as e:
        print(f"Lỗi 5: {e}")

async def perform_invite_6(target_uid: int):
    global online_writer, key, iv, region, BOT_UID
    if not online_writer: raise Exception("Bot chưa kết nối")
    try:
        PAc = await OpEnSq(key, iv, region)
        await SEndPacKeT(None, online_writer, 'OnLine', PAc)
        C = await cHSq(6, target_uid, key, iv, region)
        await SEndPacKeT(None, online_writer, 'OnLine', C)
        V = await SEnd_InV(6, target_uid, key, iv, region)
        await SEndPacKeT(None, online_writer, 'OnLine', V)
        await asyncio.sleep(5)
        E = await ExiT(BOT_UID, key, iv)
        await SEndPacKeT(None, online_writer, 'OnLine', E)
    except Exception as e:
        print(f"Lỗi 6: {e}")

# ================== FLASK ==================
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# ================== MAIN BOT ==================
async def MaiiiinE():
    global key, iv, region, TarGeT, acc_name, online_writer, loop

    Uid = "khangloveios@gmail.com"
    Pw = "Khang123@"

    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token:
        print("❌ Login thất bại!")
        return

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print("❌ Major Login thất bại!")
        return

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    region = MajoRLoGinauTh.region
    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)

    OnLineiP, OnLineporT = LoGinDaTaUncRypTinG.Online_IP_Port.split(":")
    ChaTiP, ChaTporT = LoGinDaTaUncRypTinG.AccountIP_Port.split(":")

    acc_name = LoGinDaTaUncRypTinG.AccountName
    equie_emote(ToKen, UrL)

    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    ready_event = asyncio.Event()

    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))

    loop = asyncio.get_running_loop()
    print(f"✅ Bot Online | Name: {acc_name}")

    await asyncio.gather(task1, task2)

async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout=7*60*60)
        except Exception as e:
            print(f"Lỗi: {e} → Restarting...")
            await asyncio.sleep(10)

@client.event
async def on_ready():
    await tree.sync()
    print(f"🤖 Discord Bot Ready: {client.user}")

async def main():
    threading.Thread(target=run_flask, daemon=True).start()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ Thiếu DISCORD_TOKEN!")
        return
    await asyncio.gather(StarTinG(), client.start(token))

if __name__ == '__main__':
    print("🚀 Starting Free Fire Discord Bot...")
    asyncio.run(main())
