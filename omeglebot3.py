import discord
from discord.ext import commands
from discord.ext.commands import Context
import asyncio
#setting the intents
intents = discord.Intents.all()
#setting up the bot client
bot = commands.Bot(command_prefix="!", description="cashbot", intents=intents)
#creating wait function
async def wait():
    await asyncio.sleep(1)


#HOLDING COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def h(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member):
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    #supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"
    #supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    #confirmed trades channel
    confirmed_trades = bot.get_channel(866729946658242600)
    #setting up the embed
    embed_variable = discord.Embed(color=0x5C5CFF)
    embed_variable.add_field(name="Held:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + member.mention + " to confirm the transaction.")

    #creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = member.mention + " has confirmed the transaction"
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()


#EXCHANGE COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def e(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member):
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    # supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"
    # supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    # confirmed trades channel
    confirmed_trades = bot.get_channel(866729946658242600)
    # setting up the embed
    embed_variable = discord.Embed(color=0xFFFF00)
    embed_variable.add_field(name="Exchanged:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + member.mention + " to confirm the transaction.")

    # creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = member.mention + " has confirmed the transaction"
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def r(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member):
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    # supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"
    # supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    # confirmed trades channel
    confirmed_trades = bot.get_channel(868414903520743454)
    # setting up the embed
    embed_variable = discord.Embed(color=0xFF0000)
    embed_variable.add_field(name="Held/Exchanged:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + "[redacted]" + " to confirm the transaction.")

    # creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = "[redacted] has confirmed the transaction"
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()




#CHAT CLEANER COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def clear(ctx: Context, number: int):
    await ctx.channel.purge(limit=number)


#DOUBLE HOLDING COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def hh(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member, amount1: float, paymentapp1: str, percent1, crypto1):
    #percentages 01
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    #percentages 02
    percentage1 = float(percent1) / 100
    vysledok1 = amount1 * percentage1
    output1 = amount1 - vysledok1
    finalrounded1 = round(output1, 2)
    amountrouded1 = round(amount1, 2)

    # supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"

    # supported cryptocurrencies list
    if crypto1.lower() == "ltc":
        crypto1 = "LTC"
    elif crypto1.lower() == "btc":
        crypto1 = "BTC"
    elif crypto1.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto1 = "USDT"
    elif crypto1.lower() == "xlm":
        crypto1 = "XLM"
    elif crypto1.lower() == "bch":
        crypto1 = "BCH"

    # supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    # supported payment services list
    if paymentapp1.lower() == "venmo":
        paymentapp1 = "Venmo"
    elif paymentapp1.lower() == "cashapp" or paymentapp.lower() == "ca":
        paymentapp1 = "CashApp"
    elif paymentapp1.lower() == "applepay" or paymentapp.lower() == "apay":
        paymentapp1 = "ApplePay"
    elif paymentapp1.lower() == "zelle":
        paymentapp1 = "Zelle"
    elif paymentapp1.lower() == "googlepay" or paymentapp.lower() == "gpay":
        paymentapp1 = "GooglePay"
    elif paymentapp1.lower() == "paypal" or paymentapp.lower() == "pp":
        paymentapp1 = "PayPal"
    elif paymentapp1.lower() == "agc":
        paymentapp1 = "Amazon GC"
    elif paymentapp1.lower() == "vcc":
        paymentapp1 = "VCC"

    # confirmed trades channel
    confirmed_trades = bot.get_channel(866729946658242600)
    # setting up the embed
    embed_variable = discord.Embed(color=0x00ff00)
    embed_variable.add_field(name="Held:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    embed_variable.add_field(name="Held:", value="$" + str(amountrouded1) + " " + paymentapp1 + " -> $" + str(finalrounded1) + " " + crypto1 + ".", inline=False)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + member.mention + " to confirm the transactions.")

    # creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = member.mention + " has confirmed the transactions."
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()


#DOUBLE EXCHANGE COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def ee(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member, amount1: float, paymentapp1: str, percent1, crypto1):
    #percentages 01
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    #percentages 02
    percentage1 = float(percent1) / 100
    vysledok1 = amount1 * percentage1
    output1 = amount1 - vysledok1
    finalrounded1 = round(output1, 2)
    amountrouded1 = round(amount1, 2)

    # supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"

    # supported cryptocurrencies list
    if crypto1.lower() == "ltc":
        crypto1 = "LTC"
    elif crypto1.lower() == "btc":
        crypto1 = "BTC"
    elif crypto1.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto1 = "USDT"
    elif crypto1.lower() == "xlm":
        crypto1 = "XLM"
    elif crypto1.lower() == "bch":
        crypto1 = "BCH"

    # supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    # supported payment services list
    if paymentapp1.lower() == "venmo":
        paymentapp1 = "Venmo"
    elif paymentapp1.lower() == "cashapp" or paymentapp.lower() == "ca":
        paymentapp1 = "CashApp"
    elif paymentapp1.lower() == "applepay" or paymentapp.lower() == "apay":
        paymentapp1 = "ApplePay"
    elif paymentapp1.lower() == "zelle":
        paymentapp1 = "Zelle"
    elif paymentapp1.lower() == "googlepay" or paymentapp.lower() == "gpay":
        paymentapp1 = "GooglePay"
    elif paymentapp1.lower() == "paypal" or paymentapp.lower() == "pp":
        paymentapp1 = "PayPal"
    elif paymentapp1.lower() == "agc":
        paymentapp1 = "Amazon GC"
    elif paymentapp1.lower() == "vcc":
        paymentapp1 = "VCC"

    # confirmed trades channel
    confirmed_trades = bot.get_channel(866729946658242600)
    # setting up the embed
    embed_variable = discord.Embed(color=0x00ff00)
    embed_variable.add_field(name="Exchanged:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    embed_variable.add_field(name="Exchanged:", value="$" + str(amountrouded1) + " " + paymentapp1 + " -> $" + str(finalrounded1) + " " + crypto1 + ".", inline=False)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + member.mention + " to confirm the transactions.")

    # creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = member.mention + " has confirmed the transactions."
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()


#HOLD-EXCHANGE COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def he(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member, amount1: float, paymentapp1: str, percent1, crypto1):
    #percentages 01
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    #percentages 02
    percentage1 = float(percent1) / 100
    vysledok1 = amount1 * percentage1
    output1 = amount1 - vysledok1
    finalrounded1 = round(output1, 2)
    amountrouded1 = round(amount1, 2)

    # supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"

    # supported cryptocurrencies list
    if crypto1.lower() == "ltc":
        crypto1 = "LTC"
    elif crypto1.lower() == "btc":
        crypto1 = "BTC"
    elif crypto1.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto1 = "USDT"
    elif crypto1.lower() == "xlm":
        crypto1 = "XLM"
    elif crypto1.lower() == "bch":
        crypto1 = "BCH"

    # supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    # supported payment services list
    if paymentapp1.lower() == "venmo":
        paymentapp1 = "Venmo"
    elif paymentapp1.lower() == "cashapp" or paymentapp.lower() == "ca":
        paymentapp1 = "CashApp"
    elif paymentapp1.lower() == "applepay" or paymentapp.lower() == "apay":
        paymentapp1 = "ApplePay"
    elif paymentapp1.lower() == "zelle":
        paymentapp1 = "Zelle"
    elif paymentapp1.lower() == "googlepay" or paymentapp.lower() == "gpay":
        paymentapp1 = "GooglePay"
    elif paymentapp1.lower() == "paypal" or paymentapp.lower() == "pp":
        paymentapp1 = "PayPal"
    elif paymentapp1.lower() == "agc":
        paymentapp1 = "Amazon GC"
    elif paymentapp1.lower() == "vcc":
        paymentapp1 = "VCC"

    # confirmed trades channel
    confirmed_trades = bot.get_channel(866729946658242600)
    # setting up the embed
    embed_variable = discord.Embed(color=0x00ff00)
    embed_variable.add_field(name="Held:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    embed_variable.add_field(name="Exchanged:", value="$" + str(amountrouded1) + " " + paymentapp1 + " -> $" + str(finalrounded1) + " " + crypto1 + ".", inline=False)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + member.mention + " to confirm the transactions.")

    # creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = member.mention + " has confirmed the transactions."
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()


#EXCHANGE-HOLD COMMAND


@bot.command()
@commands.has_any_role('Rico', 'Technician')
async def eh(ctx: Context, amount: float, paymentapp: str, percent, crypto, member: discord.Member, amount1: float, paymentapp1: str, percent1, crypto1):
    #percentages 01
    percentage = float(percent) / 100
    vysledok = amount * percentage
    output = amount - vysledok
    finalrounded = round(output, 2)
    amountrouded = round(amount, 2)
    #percentages 02
    percentage1 = float(percent1) / 100
    vysledok1 = amount1 * percentage1
    output1 = amount1 - vysledok1
    finalrounded1 = round(output1, 2)
    amountrouded1 = round(amount1, 2)

    # supported cryptocurrencies list
    if crypto.lower() == "ltc":
        crypto = "LTC"
    elif crypto.lower() == "btc":
        crypto = "BTC"
    elif crypto.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto = "USDT"
    elif crypto.lower() == "xlm":
        crypto = "XLM"
    elif crypto.lower() == "bch":
        crypto = "BCH"

    # supported cryptocurrencies list
    if crypto1.lower() == "ltc":
        crypto1 = "LTC"
    elif crypto1.lower() == "btc":
        crypto1 = "BTC"
    elif crypto1.lower() == "usdt" or crypto.lower() == "tether" or crypto.lower() == "usd" or crypto.lower() == "$":
        crypto1 = "USDT"
    elif crypto1.lower() == "xlm":
        crypto1 = "XLM"
    elif crypto1.lower() == "bch":
        crypto1 = "BCH"

    # supported payment services list
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
    elif paymentapp.lower() == "vcc":
        paymentapp = "VCC"

    # supported payment services list
    if paymentapp1.lower() == "venmo":
        paymentapp1 = "Venmo"
    elif paymentapp1.lower() == "cashapp" or paymentapp.lower() == "ca":
        paymentapp1 = "CashApp"
    elif paymentapp1.lower() == "applepay" or paymentapp.lower() == "apay":
        paymentapp1 = "ApplePay"
    elif paymentapp1.lower() == "zelle":
        paymentapp1 = "Zelle"
    elif paymentapp1.lower() == "googlepay" or paymentapp.lower() == "gpay":
        paymentapp1 = "GooglePay"
    elif paymentapp1.lower() == "paypal" or paymentapp.lower() == "pp":
        paymentapp1 = "PayPal"
    elif paymentapp1.lower() == "agc":
        paymentapp1 = "Amazon GC"
    elif paymentapp1.lower() == "vcc":
        paymentapp1 = "VCC"

    # confirmed trades channel
    confirmed_trades = bot.get_channel(866729946658242600)
    # setting up the embed
    embed_variable = discord.Embed(color=0x00ff00)
    embed_variable.add_field(name="Exchanged:", value="$" + str(amountrouded) + " " + paymentapp + " -> $" + str(finalrounded) + " " + crypto + ".", inline=True)
    embed_variable.add_field(name="Held:", value="$" + str(amountrouded1) + " " + paymentapp1 + " -> $" + str(finalrounded1) + " " + crypto1 + ".", inline=False)
    await confirmed_trades.send(embed=embed_variable)
    await wait()
    last_message = await confirmed_trades.fetch_message(confirmed_trades.last_message_id)
    await last_message.add_reaction("👍")
    await last_message.add_reaction("👎")
    waiting_for_confirmation = await confirmed_trades.send("Waiting for " + member.mention + " to confirm the transactions.")

    # creating check function
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '👍'

    confirmation = await bot.wait_for('reaction_add', check=check)

    if confirmation:
        edit = member.mention + " has confirmed the transactions."
        await waiting_for_confirmation.edit(content=edit)
        await last_message.clear_reactions()


bot.run("ODY5MTc5NTM4NTkxMDY4MjMw.YP6chg.QOjbbwAjd3boNYVQLAFYRjq8gX")
