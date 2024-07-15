from kyt import *

@bot.on(events.CallbackQuery(data=b'trojan-go'))
async def nob(event):
	async def nob_(event):
		inline = [
[Button.inline(" CREATE TROJAN-GO ","create-trgo"),
Button.inline(" CHECK USER ","cek-trgo")],
[Button.inline(" DELETE USER ","delete-trgo"),
Button.inline(" RENEW USER ","renew-trgo")],
[Button.inline("‹ BACK ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		tgo = f' cat /etc/trojan-go/trgo | grep "###" | wc -l'
		trgo = subprocess.check_output(tgo, shell=True).decode("ascii")
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🔥 PANEL MENU TROJAN-GO 🔥**
━━━━━━━━━━━━━━━━━━━━━━━ 
✨ **» Service:** `TROJAN-GO`
✨ **» Total Account  :** `{trgo.strip()}` __account__
✨ **» Host:** `{DOMAIN}`
✨ **» ISP:** `{z["isp"]}`
✨ **» Country:** `{z["country"]}`
🤖 **» @AMIQYU**
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await nob_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'create-trgo'))
async def create_trgo(event):
	async def create_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'delete-trgo'))
async def delete_trgo(event):
	async def delete_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'renew-trgo'))
async def renew_trgo(event):
	async def renew_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'cek-trgo'))
async def cek_trgo(event):
	async def cek_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
