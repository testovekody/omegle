import discord
from discord.ext import commands
from discord.ext.commands import Context
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", description="cashbot", intents=intents)
import asyncio

async def wait():
    await asyncio.sleep(1)





@bot.command()
async def h(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member):
    percentage = float(percent) / 100
    vysledok = amount * percentage
    final = amount - vysledok
    final1 = round(final, 2)
    amount1 = round(amount, 2)
    if crypto.lower() == "ltc":
        crypto = "LTC"
    if crypto.lower() == "btc":
        crypto = "BTC"
    if crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    if paymentapp.lower() == "venmo":
        paymentapp = "Venmo"
    elif paymentapp.lower() == "cashapp" or paymentapp.lower() == "ca":
        paymentapp = "CashApp"
    elif paymentapp.lower() == "applepay" or paymentapp.lower() == "apay":
        paymentapp = "ApplePay"
    elif paymentapp.lower() == "zelle":
        paymentapp = "Zelle"
    elif paymentapp.lower() == "googlepay" or paymentapp.lower() == "gpay":
        paymentapp = "GooglePay"
    elif paymentapp.lower() == "paypal" or paymentapp.lower() == "pp":
        paymentapp = "PayPal"
    elif paymentapp.lower() == "agc":
        paymentapp = "Amazon GC"
    polls = bot.get_channel(868414903520743454)
    embedVar = discord.Embed(color=0x00ff00)
    embedVar.add_field(name="Held:", value="$" + str(amount1) + " " + paymentapp + " -> $" + str(
        final1) + " " + crypto + ".", inline=True)
    embedVar.add_field(name="For: ", value=member.mention, inline=True)
    await polls.send(embed=embedVar)
    await wait()
    sprava = await polls.fetch_message(polls.last_message_id)
    await sprava.add_reaction("👍")
    await sprava.add_reaction("👎")

    #syntax: amount, paymentapp, percentage, crypto, user

@bot.command()
async def e(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member):
    percentage = float(percent) / 100
    vysledok = amount * percentage
    final = amount - vysledok
    final1 = round(final, 2)
    amount1 = round(amount, 2)
    if crypto.lower() == "ltc":
        crypto = "LTC"
    if crypto.lower() == "btc":
        crypto = "BTC"
    if crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    if paymentapp.lower() == "venmo":
        paymentapp = "Venmo"
    elif paymentapp.lower() == "cashapp" or paymentapp.lower() == "ca":
        paymentapp = "CashApp"
    elif paymentapp.lower() == "applepay" or paymentapp.lower() == "apay":
        paymentapp = "ApplePay"
    elif paymentapp.lower() == "zelle":
        paymentapp = "Zelle"
    elif paymentapp.lower() == "googlepay" or paymentapp.lower() == "gpay":
        paymentapp = "GooglePay"
    elif paymentapp.lower() == "paypal" or paymentapp.lower() == "pp":
        paymentapp = "PayPal"
    elif paymentapp.lower() == "agc":
        paymentapp = "Amazon GC"
    polls = bot.get_channel(868414903520743454)
    embedVar = discord.Embed(color=0x00ff00)
    embedVar.add_field(name="Exchanged:", value="$" + str(amount1) + " " + paymentapp + " -> $" + str(
        final1) + " " + crypto + ".", inline=True)
    embedVar.add_field(name="For: ", value=member.mention, inline=True)
    await polls.send(embed=embedVar)
    await wait()
    sprava = await polls.fetch_message(polls.last_message_id)
    await sprava.add_reaction("👍")
    await sprava.add_reaction("👎")

bot.run("ODY5MTc5NTM4NTkxMDY4MjMw.YP6chg.tDPLzA6mO7jwDcC5DUeaOihEEa")
