import discord
from PIL import Image, ImageDraw, ImageFont
import pickle
import traceback
import threading
from discord.ext import commands
#from discord_slash import SlashCommand, SlashContext
from discord.utils import get
from discord import Status
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import re
import time
import string
import random
# Preperations
blacklistedlink = {}
supportteamid = 854413431019929601
supportlist = []
passkeys = []
random2 = ""
pseudo2 = ""
pseudo3 = ""
passphrases = []
logchannel = 880720982904549406
welcomechannel = 880728624284704788
passphraseusers = []
banlist = []
tick = 0
guildid = '787635357620371458' # ID of your (primary) server
blocklist = []
warnlist = []
welcomeimage = 'https://images-ext-1.discordapp.net/external/Ab1QUU20B3hBS6D58SmZ5kWiY2ckSRIkzAZNGCKPc6Y/https/media.discordapp.net/attachments/878682720383926312/880725410411851786/image0.jpg'

TOKEN = 'ODgwNzI2MTk3NjYxNzMyODg0.YSieMA._C9lxI_2RIdwPUdOWS4YnHOtlIk'

class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embedVar = discord.Embed(description=page, color=0x27b8d9)
            await destination.send(embed=embedVar)

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.help_command = NewHelpName()
#slash = SlashCommand(bot)
global spamlist
spamlist = []

def resync():
    threading.Timer(1.0, resync).start()
    spamlist.clear()

resync()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="UKRPC."))
    #channel = bot.get_channel(922965541386338325)
    #embedVar = discord.Embed(title="Unscheduled outage", description="A", color=0x27b8d9)
    #await channel.send(embed=embedVar)
    

@bot.event
async def on_reaction_add(reaction, user):
    spamlist.append(user.id)
    if spamlist.count(user.id) > 7:
        return
    elif reaction.message == message_react:
        if reaction.emoji == '✈️':
            role = reaction.message.guild.get_role(820324847649292318)
            await user.add_roles(role)
            embedVar = discord.Embed(title="Added your {} role.".format(role.name), description="TUI Moderation", color=0x27b8d9)
            await user.send(embed=embedVar)

@bot.event
async def on_reaction_remove(reaction, user):
    spamlist.append(user.id)
    if spamlist.count(user.id) > 7:
        return
    elif reaction.message == message_react:
        if reaction.emoji == '✈️':
            role = reaction.message.guild.get_role(820324847649292318)
            await user.remove_roles(role)
            embedVar = discord.Embed(title="Removed your {} role.".format(role.name), description="TUI Moderation", color=0x27b8d9)
            await user.send(embed=embedVar)
 
class Chat(commands.Cog):
    """Commands affiliated with chat purposes.\nAll commands in this list require the executor to have Administrator permissions within the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *, args):
        """Say a given keyword, no quote marks required."""
        await ctx.channel.send(args)
        await ctx.message.delete()

    @commands.command()
    @has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        """Delete the given number of messages, excluding the command message, from the current channel."""
        await ctx.channel.purge(limit=limit+1)
    
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def announce(self, ctx, channelto, att, title2, args):
        """Announce in a specified channel, place `NONE` in attribute (att) to post without an image."""
        embedVar = discord.Embed(title="Announcement", description="UKRPC Announcement by {}, {}".format(ctx.author, ctx.author.mention), color=0x27b8d9)
        embedVar.add_field(name=title2, value=args, inline=False)
        print(att)
        if not "http" in att:
            channelto = channelto.replace('<','')
            channelto = channelto.replace('>','')
            channelto = channelto.replace('#','')
            channel = bot.get_channel(int(channelto))
            await channel.send(embed=embedVar)
            await ctx.message.delete()
        else:
            embedVar.set_image(url=att)
            channelto = channelto.replace('<','')
            channelto = channelto.replace('>','')
            channelto = channelto.replace('#','')
            channel = bot.get_channel(int(channelto))
            await channel.send(embed=embedVar)
            await ctx.message.delete()

    @commands.command(pass_context=True)
    @commands.has_role(863837303688527922)
    async def changelog(self, ctx, channelto, att, title2, args):
        """Announce in a specified channel, place `NONE` in attribute (att) to post without an image."""
        embedVar = discord.Embed(title="Changelog", description="Bot Changelog by {}, {}".format(ctx.author, ctx.author.mention), color=0x27b8d9)
        embedVar.add_field(name=title2, value=args, inline=False)
        print(att)
        if not "http" in att:
            channelto = channelto.replace('<','')
            channelto = channelto.replace('>','')
            channelto = channelto.replace('#','')
            channel = bot.get_channel(int(channelto))
            await channel.send(embed=embedVar)
            await ctx.message.delete()
        else:
            embedVar.set_image(url=att)
            channelto = channelto.replace('<','')
            channelto = channelto.replace('>','')
            channelto = channelto.replace('#','')
            channel = bot.get_channel(int(channelto))
            await channel.send(embed=embedVar)
            await ctx.message.delete()
        
    #@commands.command()
    #@commands.has_permissions(administrator=True) 
    #async def stansted(self, ctx, channelto, checkin, security, gateOpen, gateClose, takeoff):
    #    """Announce custom Stansted airport flight schedule."""
    #    channelto = channelto.replace('<','')
    #    channelto = channelto.replace('>','')
    #    channelto = channelto.replace('#','')
    #    channelto = channelto.replace('!','')
    #    channel = bot.get_channel(int(channelto))
    #    embedVar = discord.Embed(title="**TUI London Stansted Departure.**", description="We will now be hosting a flight departure at London Stansted, why not come and have some fun? Any and all information available is listed below.", color=0x27b8d9)
    #    embedVar.set_image(url="https://db3pap001files.storage.live.com/y4muGhUMDCODteaxDNTUlisP-3QSm37g-uiHWPGp-nWml2va_JxYocCBJOcTOnrenX_aC8UYBQd6aEFQDi-ztW4Tzz0SYfrdygNhw0F3zcsUUr9c9_z_EQ3p6byBKdjqQpKtQ5iUUdbvJEtJxistSYObuCe5vtC7Eo3Pt6Yh4UalxNVorEzGEaXEArXGTavWnn9?width=3840&height=2010&cropmode=none")
    #    embedVar.add_field(name="Information", value="Check in opens: {}\nSecurity opens: {}\nGate opens: {}\nGate Closes: {}\nTakeoff: {}".format(checkin, security, gateOpen, gateClose, takeoff))
    #    embedVar.add_field(name="Join us!", value="Interested? Join the game via this link!\nhttps://bit.ly/tuistn")
    #    await channel.send(embed=embedVar)

class Debug(commands.Cog):
    """Debug tools to assist development, please do not use these commands on normal users as they may face issues with unexpected warnings/bans.\nAll commands in this list require the executor to have Administrator permissions within the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def debug(ctx, action):
        """Debug tools for testing new commands and events."""
        if action == "-01":
            channel = bot.get_channel(logchannel)
            if ctx.message.channel.guild.id == channel.guild.id:
                with open ('banlist', 'rb') as fp:
                    banlist = pickle.load(fp)
                if ctx.author.id in banlist:
                    try:
                        embedVar = discord.Embed(title="Banned.", description="Unfortunately you are banned in this server.", color=0x27b8d9)
                        await ctx.author.send(embed=embedVar)
                    except:
                        return
                    channel = bot.get_channel(logchannel)
                    embedVar = discord.Embed(title="Member join intercepted.", description="{} tried to join the server, but was banned because they are in the preemptive ban list.".format(ctx.author.id), color=0x27b8d9)
                    await channel.send(embed=embedVar)
                    #await ctx.author.ban()
                else:
                    channel = bot.get_channel(welcomechannel)
                    true_member_count = len([m for m in channel.guild.members if not m.bot])
                    embedVar = discord.Embed(title="Welcome!", description="<@!{}>, {}".format(ctx.author.id, ctx.author.name), color=0x27b8d9)
                    embedVar.add_field(name="Welcome to TUI!", value="We ask you read the rules before chatting. Have fun!", inline=True)
                    embedVar.add_field(name="Member count", value="{} members.".format(true_member_count), inline=True)
                    embedVar.set_image(url=welcomeimage)
                    await channel.send(embed=embedVar)
            #await ctx.channel.send("⚠ Something went wrong.")

    @commands.command()
    @commands.has_role(863837303688527922)
    async def fullreboot(self, ctx, code):
        """Flush/Recreate all files to do with tickets, bans, warnings, etcetera."""
        if code == "req":
            letters = string.ascii_letters + string.digits
            random1 = ''.join(random.choice(letters) for i in range(10))
            await ctx.channel.send("A code has been sent to this channel for verification. (⚠ THIS WILL COMPLETELY WIPE ALL OF THE LISTED: Support ticket lists, support ticket blocks, warnings of all users. The key is volatile and can be wiped in a standard reboot.)".format(random1))
            await ctx.channel.send("Here's the reset code requested for a reboot: `{}`".format(random1))
            passkeys.append(random1)
        elif code in str(passkeys):
            supportlist = ["placeholder"]
            blocklist = ["placeholder"]
            warnlist = ["placeholder"]
            with open('warnlist', 'wb') as fp1:
                pickle.dump(warnlist, fp1)
            with open('supportlist', 'wb') as fp2:
                pickle.dump(supportlist, fp2)
            with open('blocklist', 'wb') as fp3:
                pickle.dump(blocklist, fp3)
            await ctx.channel.send("Full reboot cleared.")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def listadd(self, ctx, member: discord.Member, reason):
        """Private debug tool."""
        warnlist.append(member.id)
        warnlist.append(reason)
        embedVar = discord.Embed(title="Warned {} successfully.".format(member.name), description="With reason: `{}`".format(reason), color=0x27b8d9)
        embedVar2 = discord.Embed(title="Warning from {} / {}".format(ctx.author.mention, ctx.author), description="`{}`".format(reason), color=0xff3a33)
        await member.send(embed=embedVar2)
        await ctx.send(embed=embedVar)
        with open('warnlist', 'wb') as fp:
            pickle.dump(warnlist, fp)
        warnlist.clear()

class Misc(commands.Cog):
    """All commands in this list require the executor to have Administrator permissions within the server, except those specified."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setstatus(self, ctx, val : int, *, arg):
        """Set the status of the bot to a given value. Val = 1: Playing, 2: Watching, 3: Listening to."""
        if val == 1:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=arg))
            embedVar = discord.Embed(title="Set Status", description="Successfully set status to playing {}".format(arg), color=0x34eb77)
            await ctx.channel.send(embed=embedVar)
        elif val == 2:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg))
            embedVar = discord.Embed(title="Set Status", description="Successfully set status to watching {}".format(arg), color=0x34eb77)
            await ctx.channel.send(embed=embedVar)
        elif val == 3:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg))
            embedVar = discord.Embed(title="Set Status", description="Successfully set status to listening to {}".format(arg), color=0x34eb77)
            await ctx.channel.send(embed=embedVar)
    
    @commands.command()
    async def membercount(self, ctx):
        """**Does not require administrator permissions to run.** Member count of the server, with and without bots."""
        member_count = len(ctx.guild.members)
        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        embedVar = discord.Embed(title="Current member count", description=ctx.guild.name, color=0x27b8d9)
        embedVar.add_field(name="Total member count: `{}`".format(true_member_count), value="Member count (including bots): `{}`".format(member_count), inline=False)
        await ctx.send(embed=embedVar)

class Ticket(commands.Cog):
    """All commands in this list require the executor to have Administrator permissions within the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reply(self, ctx, *arg):
        """Reply to a user's message in a ticekt, does not require quote marks."""
        embedVar = discord.Embed(title="Error", description="⚠ Untethered channel exception. Please use this command in an open ticket channel.\nIf this is a ticket channel, contact <@557284703393021983>", color=0xeb4034)
        await ctx.channel.send(embed=embedVar)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def close(self, ctx, *arg):
        """Close a ticket with a reason, the reason does not require quote marks."""
        embedVar = discord.Embed(title="Error", description="⚠ Untethered channel exception. Please use this command in an open ticket channel.\nIf this is a ticket channel, contact <@557284703393021983>", color=0xeb4034)
        await ctx.channel.send(embed=embedVar)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def block(self, ctx, *arg):
        """Block and close a ticket from a user, the user will be unable to open tickets until the Unblock command is initiated, see `!help unblock` for more details. The reason does not require quote marks."""
        embedVar = discord.Embed(title="Error", description="⚠ Untethered channel exception. Please use this command in an open ticket channel.\nIf this is a ticket channel, contact <@557284703393021983>", color=0xeb4034)
        await ctx.channel.send(embed=embedVar)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblock(self, ctx, member: discord.Member):
        """Remove ticket block from a user, requires ping."""
        with open ('blocklist', 'rb') as fp:
            blocklist = pickle.load(fp)
        member1 = '{}'.format(member.id)
        temp9 = await ctx.send("🔄 Finding block index...")
        print(blocklist)
        try:
            wid = int(blocklist.index(member1))
            blocklist.pop(wid)
            with open('blocklist', 'wb') as fp:
                pickle.dump(blocklist, fp)
            blocklist.clear()
            await temp9.edit(content="✅ Block removed for {}.".format(member.mention))
        except Exception as e:
            await temp9.edit(content="⚠ An error occured: `{}`".format(e))

class Moderation(commands.Cog):
    """All commands in this list require the executor to have Administrator permissions within the server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, trg):
        """Ban a user by member ID, preemptively or actively. No reason should be given."""
        try:
            trg = int(trg)
        except:
            embedVar = discord.Embed(title="Error", description="Please give a member ID for bans.", color=0x27b8d9)
            await ctx.channel.send(embed=embedVar)
        if type(trg) == int:
            if not(trg == 804773304472174643) or not(trg == ctx.author):
                try:
                    member = bot.get_user(trg)
                    try:
                        await member.ban()
                        embedVar = discord.Embed(title="Banned", description="{} was banned from the server.".format(member.mention), color=0x27b8d9)
                        await ctx.channel.send(embed=embedVar)
                    except:
                        await member.kick()
                        embedVar = discord.Embed(title="Kicked", description="{} could not be banned from this server due to an error, so was kicked instead, this does not mean that they will be able to mitigate preemptive blacklist banning.".format(member.mention), color=0x27b8d9)
                        await ctx.channel.send(embed=embedVar)
                    
                    with open ('banlist', 'rb') as fp:
                        banlist = pickle.load(fp)
                    banlist.append(trg)
                    embedVar = discord.Embed(title="Preemptively Banned", description="{} was also successfully banned preemptively from the server (Added to join blacklist). You'll need to unban this member using !unban to remove them from the preemptive ban list.".format(trg), color=0x27b8d9)
                    await ctx.channel.send(embed=embedVar)
                    with open('banlist', 'wb') as fp:
                        pickle.dump(banlist, fp)
                    banlist.clear()
                except:
                    with open ('banlist', 'rb') as fp:
                        banlist = pickle.load(fp)
                    banlist.append(trg)
                    embedVar = discord.Embed(title="Preemptively Banned", description="{} was successfully banned preemptively from the server (Added to join blacklist). You'll need to unban this member using !unban to remove them from the preemptive ban list.".format(trg), color=0x27b8d9)
                    await ctx.channel.send(embed=embedVar)
                    with open('banlist', 'wb') as fp:
                        pickle.dump(banlist, fp)
                    banlist.clear()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, channel : discord.TextChannel=None):
        """This command is being established actively, this command may not work or is not working for the time being."""
        # channel = channel or ctx.channel
        # role = ctx.guild.get_role(799021447049642034)
        # await channel.set_permissions(role, send_messages=False)
        # role = ctx.guild.get_role(799262171707080705)
        # await channel.set_permissions(role, send_messages=False)
        # role = ctx.guild.get_role(799021530549059625)
        # await channel.set_permissions(role, send_messages=False)
        # embedVar = discord.Embed(title="Channel locked.", description="This channel has been locked by moderators.", color=0xeb4034)
        # await channel.send(embed=embedVar)
        await channel.send("This command has temporarily been disabled. See `!help lock` for more information")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, trg):
        """Unban a user preemptively, not actively. No reason should be given."""
        try:
            trg = int(trg)
        except:
            embedVar = discord.Embed(title="Error", description="Please give a member ID for unbanning.", color=0x27b8d9)
            await ctx.channel.send(embed=embedVar)
        if type(trg) == int:
            if not(trg == 820713746593873973) or not(trg == ctx.author):
                try:
                    with open ('banlist', 'rb') as fp:
                        banlist = pickle.load(fp)
                    banlist.remove(trg)
                    embedVar = discord.Embed(title="Unbanned", description="{} was unbanned preemptively from the server (Removed from join blacklist).".format(trg), color=0x27b8d9)
                    await ctx.channel.send(embed=embedVar)
                    with open('banlist', 'wb') as fp:
                        pickle.dump(banlist, fp)
                    banlist.clear()
                except:
                    embedVar = discord.Embed(title="Error", description="Unable to find {} in preemptive ban list, unban users who were originally in the server by going into server settings.".format(trg), color=0x27b8d9)
                    await ctx.channel.send(embed=embedVar)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def banlist(self, ctx):
        """See a list of all banned member IDs, preemptive bans only."""
        with open ('banlist', 'rb') as fp:
            banlist = pickle.load(fp)
        users = str(banlist).replace(",", "\n")
        users = users.replace("'", "")
        users = users.replace('[', '')
        users = users.replace(']', '')
        users = users.replace('placeholder', '')
        embedVar = discord.Embed(title="Banned IDs", description="{}".format(users), color=0x27b8d9)
        await ctx.channel.send(embed=embedVar)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        """This command is being established actively, this command may not work or is not working for the time being."""
        # channel = channel or ctx.channel
        # role = ctx.guild.get_role(799021447049642034)
        # await channel.set_permissions(role, send_messages=False)
        # role = ctx.guild.get_role(799262171707080705)
        # await channel.set_permissions(role, send_messages=False)
        # role = ctx.guild.get_role(799021530549059625)
        # await channel.set_permissions(role, send_messages=False)
        # embedVar = discord.Embed(title="Channel locked.", description="This channel has been locked by moderators.", color=0xeb4034)
        # await channel.send(embed=embedVar)
        await channel.send("This command has temporarily been disabled. See `!help unlock` for more information")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a user with a reason. The rason does not require quote marks."""
        try:
            if member == None or member == ctx.message.author:
                await ctx.channel.send("Why did you just try to kick yourself?")
                return
            else:
                await member.kick(reason=reason)
                await ctx.channel.send("User successfully kicked")
        except:
            await ctx.channel.send("An error was raised and this command could not be completed.")



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        """Warn a user with a reason."""
        with open ('warnlist', 'rb') as fp:
            warnlist = pickle.load(fp)
        letters = "qwrtpsdfghjkzxcvbnmQWRTPSDFGHJKLZXCVNM23456789?!:;-+[]<>"
        random1 = ''.join(random.choice(letters) for i in range(3))
        while random1 in warnlist:
            random1 = ''.join(random.choice(letters) for i in range(3))
        identification = random1
        warnlist.append(member.id)
        warnlist.append(reason)
        warnlist.append(identification)
        try:
            embedVar2 = discord.Embed(title="Warning from {} / {}".format(ctx.author.mention, ctx.author), description="Warning: `{}`\nWarning ID: `{}`".format(reason, random1), color=0xff3a33)
            await member.send(embed=embedVar2)
            embedVar = discord.Embed(title="Warned {} successfully.".format(member.name), description="With reason: `{}`\nID: `{}`".format(reason, random1), color=0x27b8d9)
            await ctx.send(embed=embedVar)
        except:
            embedVar = discord.Embed(title="Warning added to {} successfully.".format(member.name), description="With reason: `{}`\nID: `{}`\n⚠ The user has their DMs disabled in this server or an error occured and thse user has not received the warning. The warning has been stored anyways.".format(reason, random1), color=0x27b8d9)
            await ctx.send(embed=embedVar)
        with open('warnlist', 'wb') as fp:
            pickle.dump(warnlist, fp)
        warnlist.clear()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warnings(self, ctx, member: discord.Member):
        """See warnings for a specific user."""
        with open ('warnlist', 'rb') as fp:
            warnlist = pickle.load(fp)
        temp5 = await ctx.send("🔄 Finding warnings...")
        t = -1
        count = 0
        embedVar = discord.Embed(title="Warnings for user {}".format(member.name), description=ctx.guild.name, color=0x27b8d9)
        if count == 0:
            while True:
                try:
                    count = count + 1
                    t = warnlist.index(member.id, t + 1)
                    embedVar.add_field(name="Warning `{}`".format(count), value="Reason `{}`, ID `{}`".format(warnlist[t+1], warnlist[t+2]), inline=False)
                except ValueError:
                    break
        count = count - 1
        if count == 0:
            await temp5.edit(content="✅ User has no warnings.")
        else:
            await temp5.edit(content="⚠ User has {} warning(s).".format(count))
            embedVar.add_field(name="Total warning count: `{}`".format(count), value="Nothing else to see here.", inline=False)
            await ctx.send(embed=embedVar)
        warnlist.clear()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rmwarning(self, ctx, wid):
        """Remove a warning from a user, using the unique warning ID, to find the correct warning ID, run `!warnings <user>` to find the warning and ID."""
        with open ('warnlist', 'rb') as fp:
            warnlist = pickle.load(fp)
        temp7 = await ctx.send("🔄 Finding warning ID...")
        try:
            loc = warnlist.index(wid)
            await temp7.edit(content="✅ Finding warning ID...\n🔄 Removing warning data...")
            warnlist.pop(loc-2)
            warnlist.pop(loc-2)
            warnlist.pop(loc-2)
            with open('warnlist', 'wb') as fp:
                pickle.dump(warnlist, fp)
            warnlist.clear()
            await temp7.edit(content="✅ Finding warning ID...\n✅ Removing warning data...\n✅ Warning removed.")
        except Exception as e:
            await temp7.edit(content="⚠ An error occured: `{}`".format(e))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def blacklist(self, ctx, *, arg):
        """Blacklist a RegEx from any messages in your server."""
        arg = str(arg)
        blacklistedlink[ctx.message.guild.id] = arg
        await ctx.send("Successfully temporarily blacklisted this RegEx.")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcomechannel)
    if member.guild.id == channel.guild.id:
        with open ('banlist', 'rb') as fp:
            banlist = pickle.load(fp)
        if member.id in banlist:
            try:
                embedVar = discord.Embed(title="Banned.", description="Unfortunately you are banned in this server.", color=0x27b8d9)
                await member.send(embed=embedVar)
            except:
                return
            await member.ban()
            channel = bot.get_channel(welcomechannel)
            embedVar = discord.Embed(title="Member join intercepted.", description="{} tried to join the server, but was banned because they are in the preemptive ban list.".format(member.id), color=0x27b8d9)
            await channel.send(embed=embedVar)
        else:
            channel = bot.get_channel(welcomechannel)
            true_member_count = len([m for m in channel.guild.members if not m.bot])
            embedVar = discord.Embed(title="Welcome!", description="<@!{}>, {}".format(member.id, member.name), color=0x27b8d9)
            embedVar.add_field(name="Welcome to US Net Hosting!", value="We ask you read the rules in <#799041393573232700> before chatting. Have fun!", inline=True)
            embedVar.add_field(name="Member count", value="{} members.".format(true_member_count), inline=True)
            embedVar.set_image(url=welcomeimage)
            await channel.send(embed=embedVar)

'''
@bot.event
def on_member_remove(member):
    if str(member.id) in str(supportlist):
        channelloc = supportlist.index(message.author.name)
        channel = bot.get_channel(supportlist[channelloc+1])
        embedVar = discord.Embed(title="`{}` left whilst ticket was open.".format(str(message.author)), description="If the member rejoins, the ticket will be operational again.", color=0xff3a33)
        await channel.send(embed=embedVar)
    else:
        print(member, " left the server")
'''

@bot.event
async def on_message_edit(before, message):
    if before.author == bot.user:
        return
    elif before.content != message.content:
        if blacklistedlink in message.content.lower():
            await message.delete()
        print(message.author, "edited a message from:", before.content, "to:", message.content)


@bot.event
async def on_message(message):
    print("From: {}: {}".format(message.author, message.content, message.guild))
    with open ('supportlist', 'rb') as ep:
        supportlist = pickle.load(ep)
    msg = message.content.lower()
    if message.author == bot.user:
        return
    else:
        try:
            if re.search(blacklistedlink[message.guild.id], msg):
                try:
                    await message.reply("The provided link/keyword is blacklisted.")
                except:
                    pass
                await message.delete()
        except Exception as e:
            print(e, " -- Continuing anyway.")
    if not message.guild:
        #embedVar = discord.Embed(title="Ticket system down.", description="The ticket system captcha is running into issues at the moment, and therefore cannot establish a ticket at this time. Sorry for any inconvenience.", color=0x27b8d9)
        #await message.channel.send(embed=embedVar)
        with open ('blocklist', 'rb') as fp:
            blocklist = pickle.load(fp)
        if str(message.author.id) in str(blocklist):
            await message.channel.send("Oh dear! Looks like you've been blocked from sending further ticket requests.")
        elif not(message.author.id in supportlist) and not(str(message.author.id) in passphraseusers):
            print(supportlist)
            #letters = string.ascii_letters + string.digits
            letters = "qwrtpsdfghjkzxcvbnmQWRTPSDFGHJKLZXCVNM234567892345678923456789"
            random2 = ''.join(random.choice(letters) for i in range(6))
            pseudo2 = ''.join(random.choice(letters) for i in range(6))
            pseudo3 = ''.join(random.choice(letters) for i in range(6))
            passphraseusers.append(str(message.author.id))
            passphrases.append(random2)
            base = Image.open("MintTemplate.png").convert("RGBA")
            W, H = (1080,400)
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255,255,255,0))

            # get a font
            fnt = ImageFont.truetype("TUI.ttf", 250)
            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text, full opacity
            w, h = d.textsize(random2, font=fnt)
            d.text((((W-w)/2)-100,((H-h)/2)-120), pseudo2, font=fnt, fill=(255,255,255,90))
            d.text((((W-w)/2)+100,((H-h)/2)+80), pseudo3, font=fnt, fill=(255,255,255,90))
            d.text(((W-w)/2,((H-h)/2)-20), random2, font=fnt, fill=(255,255,255,240))

            out = Image.alpha_composite(base, txt)

            out.save('temp.png')
            embedVar = discord.Embed(title="Open a ticket.", description="To confirm that you want to open a ticket, please enter the **bold opaque code** you can see in the image below (case sensitive): *Stuck? DM a moderator directly (If you're not a robot).*", color=0x27b8d9)
            file = discord.File("temp.png") # an image in the same folder as the main bot file
            embedVar.set_image(url="attachment://temp.png")
            #await message.channel.send("Type out and send the letters and numbers that you see to open your ticket:")
            #await message.channel.send(file=discord.File('/share/temp.png'))
            await message.channel.send(embed=embedVar, file=file)
        elif not str(message.author.id) in supportlist and str(message.content) in passphrases:
            passphrases.remove(message.content)
            reactto = await message.channel.send("Verified. Opening support ticket...")
            try:
                passphraseusers.remove(str(message.author.id))
                channel = bot.get_channel(welcomechannel)
                currentguild = channel.guild
                channel = await currentguild.create_text_channel('dm-support-ticket')
                await channel.set_permissions(currentguild.default_role, read_messages=False)
                support = get(currentguild.roles, id=supportteamid)
                await channel.set_permissions(support, read_messages=True, send_messages=True)
                supportlist.append(message.author.name)
                supportlist.append(channel.id)
                supportlist.append(message.author.id)
                with open('supportlist', 'wb') as ep:
                    pickle.dump(supportlist, ep)
                supportlist.clear()
                embedVar = discord.Embed(title="Support ticket opened successfully", description="Ticket opened by {}".format(str(message.author)), color=0x27b8d9)
                embedVar.add_field(name="A member of our support team will be here to assist you shortly.", value="Please be patient. In the meantime you can read how this works:\nNo commands are needed for this DM, all you have to do to talk to the staff is to message this bot. It's a direct conversation, so you don't need to crowd everything in one message.\nOnly one image attachment can be sent to the admins at a time.", inline=False)
                embedVar.set_image(url="https://images-ext-1.discordapp.net/external/Ab1QUU20B3hBS6D58SmZ5kWiY2ckSRIkzAZNGCKPc6Y/https/media.discordapp.net/attachments/878682720383926312/880725410411851786/image0.jpg")
                await message.channel.send(embed=embedVar)
                embedVar = discord.Embed(title="Support ticket Opened", description="Ticket opened by <@!{}>".format(message.author.id), color=0x27b8d9)
                embedVar.set_author(name="New ticket from {}".format(message.author.name), icon_url=message.author.avatar_url)
                embedVar.add_field(name="Word captcha code used by `{}`".format(message.author.name), value=message.content, inline=False)
                embedVar.add_field(name="Here are a few commands you can use:", value="`!reply <message>` - reply to the DM.\n\n`!rename <name>` - Change the ticket channel name\n\n`!close <reason>` - Closes the ticket and deletes the ticket channel\n\n`!block <reason>` - Filter out those annoying ticket spammers by blocking their names temporarily. Unblock the ticket abuser using `!unblock`.", inline=False)
                embedVar.add_field(name="Macros to speed up ticket resolutions:", value="**Key:\n`#` - Appears as a normal message.\n`ø` - Appears as warning.\n`÷` - Appears as embed/image.**\n\n`!welcome` - Displays a welcome to UKRPD support message. `#`", inline=False)

                await channel.send(embed=embedVar, content=f"<@&{supportteamid}>")
                #await channel.send("<@&>, a support ticket from {} has opened.\nHere are a few commands you can use:\n`!reply <message>` - reply to the DM.\n`!rename <name>` - Change the ticket channel name\n`!close <reason>` - Closes the ticket and deletes the ticket channel\n`!block <reason>` - Filter out those annoying ticket spammers by blocking their names temporarily. There is currently no unblock command, as this is for emergency use only.".format(str(message.author.mention)))
                logchannel1 = bot.get_channel(logchannel)
                embedVar = discord.Embed(title="Support ticket opened.", description="Ticket opened by {}".format(str(message.author.mention)), color=0x27b8d9)
                embedVar.add_field(name="Word captcha code used: `{}`".format(message.content), value="Channel: {}\nTake me there: <#{}>".format(channel.id, channel.id), inline=False)
                await logchannel1.send(embed=embedVar)
            except Exception as e:
                print(e)
                embedVar = discord.Embed(title="Support ticket failed to open.", description="The ticket system is currently down or experiencing internal issues, we're looking into the issue.", color=0xff3a33)
                await message.channel.send(embed=embedVar)
                logchannel1 = bot.get_channel(logchannel)
                embedVar = discord.Embed(title="Support ticket failed to open.", description="Ticket opened by {} failed to open due to `{}`.".format(str(message.author.mention,e)), color=0xff3a33)
                await logchannel1.send(embed=embedVar)
        else:
            channelloc = supportlist.index(message.author.name)
            channel = bot.get_channel(supportlist[channelloc+1])
            embedVar = discord.Embed(title="\n", description=message.content, color=0x7cc2bd)
            embedVar.set_author(name="From {}".format(message.author.name), icon_url=message.author.avatar_url)
            try:
                if ".png" in message.attachments[0].url.lower() or ".jpg" in message.attachments[0].url.lower() or ".jpeg" in message.attachments[0].url.lower() or ".gif" in message.attachments[0].url.lower() or ".webp" in message.attachments[0].url.lower():
                    embedVar.set_image(url=message.attachments[0].url)
                    await message.add_reaction('✅')
                    await channel.send(embed=embedVar)
            except:
                await message.add_reaction('✅')
                await channel.send(embed=embedVar)
    elif str(message.channel.id) in str(supportlist):
            if message.content.startswith("!close"):
                temp = await message.channel.send("🔄 Preparing to close ticket...")
                time.sleep(1)
                try:
                    async with message.channel.typing():
                        context = message.content.replace('!close ', '')
                        if context == "!close":
                            context = "No reason given."
                        channelloc = supportlist.index(message.channel.id)
                        channel = bot.get_user(supportlist[channelloc+1])
                        embedVar = discord.Embed(title="Support ticket closed.", description="Ticket closed by {}".format(message.author), color=0xff3a33)
                        embedVar.set_author(name="Closed by {}".format(message.author.name), icon_url=message.author.avatar_url)
                        embedVar.add_field(name="Reason: `{}`".format(context), value="UKRPC Moderation", inline=False)
                        closedVar = discord.Embed(title="Support ticket session closed.", description="Ticket session closed with {} for reason `{}`".format(channel.name, context), color=0xff3a33)
                        closedVar.set_author(name="Closed by {}".format(message.author.name), icon_url=message.author.avatar_url)
                        await channel.send(embed=embedVar)
                        channel = bot.get_channel(logchannel)
                        await channel.send(embed=closedVar)
                        await temp.edit(content="✅ Preparing to close ticket...")
                        temp2 = await message.channel.send("🔄 Removing user from live list...")
                        channelloc = supportlist.index(message.channel.id)
                        supportlist.remove(supportlist[channelloc+1])
                        supportlist.remove(supportlist[channelloc-1])
                        channelloc = supportlist.index(message.channel.id)
                        supportlist.remove(supportlist[channelloc])
                        with open('supportlist', 'wb') as fp:
                            pickle.dump(supportlist, fp)
                        supportlist.clear
                        #supportlist.remove(supportlist[channelloc]) - Breaks it for some odd reason.
                        await temp2.edit(content="✅ Removing user from live list...")
                        await message.channel.send("✅ Task completed successfully.")
                        await message.channel.send("🔄 Deleting channel in 5 seconds...")
                        time.sleep(5)
                        await message.channel.delete()
                except ValueError as e:
                    await temp1.edit(content="⚠ Preparing to close ticket...")
                    await message.channel.send("⚠ This channel is not currently tethered to an active ticket.\nThe user may have left the server, or the bot has had an update.")                        
                except Exception as e:
                    await temp.edit(content="⚠ Preparing to close ticket...")
                    time.sleep(1)
                    temp7 = await message.channel.send("⚠ Collecting error messages...")
                    time.sleep(0.25)
                    await temp7.edit(content="⚠ Something went wrong. Delete the channel manually and contact the head developer.\nSend this to the head developer: `{}`".format(e))
            elif message.content.startswith("!block"):
                try:
                    temp1 = await message.channel.send("🔄 Preparing to close ticket...")
                    async with message.channel.typing():
                        await temp1.edit(content="✅ Preparing to close ticket...")
                        channelloc = supportlist.index(message.channel.id)
                        channel = bot.get_user(supportlist[channelloc+1])
                        context = message.content.replace('!block ', '')
                        if context == "!block":
                            context = "No reason given."
                        logchannel1 = bot.get_channel(logchannel)
                        embedVar = discord.Embed(title="Uh oh!", description="All future ticket requests blocked by moderators.".format(message.author), color=0xff3a33)
                        embedVar.add_field(name="Reason: `{}`".format(context), value="UKRPC Moderation", inline=False)
                        await channel.send(embed=embedVar)
                        temp2 = await message.channel.send("🔄 Adding user to block list...")
                        blocklist = []
                        blocklist.append(str(supportlist[channelloc+1]))
                        with open('blocklist', 'wb') as fp:
                            pickle.dump(blocklist, fp)
                        blocklist.clear
                        channelloc = supportlist.index(message.channel.id)
                        embedVar = discord.Embed(title="User blocked from creating support tickets.", description="User blocked by {} for {}".format(str(message.author.mention), context), color=0x27b8d9)
                        embedVar.add_field(name="User blocked:", value="{}".format("<@!{}>, {}".format(supportlist[channelloc-1], supportlist[channelloc+1])), inline=False)
                        await logchannel.send(embed=embedVar)
                        await temp2.edit(content="✅ Adding user to block list...")
                        temp3 = await message.channel.send("🔄 Removing user from live list...")
                        supportlist.remove(supportlist[channelloc+1])
                        supportlist.remove(supportlist[channelloc-1])
                        channelloc = supportlist.index(message.channel.id)
                        supportlist.remove(supportlist[channelloc])
                        with open('supportlist', 'wb') as fp:
                            pickle.dump(supportlist, fp)
                        supportlist.clear
                        #supportlist.remove(supportlist[channelloc]) - Breaks it for some odd reason.
                        await temp3.edit(content="✅ Removing user from live list...")
                        await message.channel.send("✅ Task completed successfully.")
                        await message.channel.send("Deleting channel in 5 seconds...")
                        time.sleep(5)
                        await message.channel.delete()
                except ValueError as e:
                    await temp1.edit(content="⚠ Preparing to close ticket...")
                    await message.channel.send("⚠ This channel is not currently tethered to an active ticket.\nThe user may have left the server, or the bot has had an update.\nError code: `06`")
                except Exception as e:
                    await temp1.edit(content="⚠ Preparing to close ticket...")
                    await message.channel.send("⚠ Something went wrong. Delete the channel manually and contact the head developer.\nSend this to the head developer: `{}`".format(traceback.format_exc()))
            elif message.content.startswith("!rename"):
                context = message.content.replace('!rename ', '')
                if context == "":
                    context = "no-name-given"
                await message.channel.edit(name = context)
                await message.channel.send("Renamed channel to `{}` successfully.".format(context))
            elif message.content.startswith("!welcome"):
                channelloc = supportlist.index(message.channel.id)
                channel = bot.get_user(supportlist[channelloc+1])
                embedVar = discord.Embed(title="\n", description="Hi, thank you for contacting support, I will be dealing with your ticket today. How can I assist you?", color=0x7cc2bd)
                embedVar.set_author(name="From {}".format(message.author.name), icon_url=message.author.avatar_url)
                await message.add_reaction('✅')
                await channel.send(embed=embedVar)
                await message.channel.send(embed=embedVar)
            elif message.content.startswith("!reply"):
                try:
                    context = message.content.replace('!reply', '')
                    channelloc = supportlist.index(message.channel.id)
                    channel = bot.get_user(supportlist[channelloc+1])
                    embedVar = discord.Embed(title="\n", description=context, color=0x7cc2bd)
                    embedVar.set_author(name="From {}".format(message.author.name), icon_url=message.author.avatar_url)
                    try:
                        if ".png" in message.attachments[0].url.lower() or ".jpg" in message.attachments[0].url.lower() or ".jpeg" in message.attachments[0].url.lower() or ".gif" in message.attachments[0].url.lower() or ".webp" in message.attachments[0].url.lower():
                            embedVar.set_image(url=message.attachments[0].url)
                            await message.add_reaction('✅')
                            await channel.send(embed=embedVar)
                            await message.channel.send(embed=embedVar)
                    except:
                        await message.add_reaction('✅')
                        await channel.send(embed=embedVar)
                        await message.channel.send(embed=embedVar)
                except ValueError as e:
                    await message.channel.send("⚠ This channel is not currently tethered to an active ticket.\nThe user may have left the server, or the bot has had an update.\nTo troubleshoot: delete the ticket channel and inform the user to try again.\nError code: `06`")        
                except Exception as e:
                    await message.channel.send("⚠ Something went wrong. Don't delete the channel manually and contact the head developer.\nSend this to the head developer: `{}`".format(e))
    elif "<@!" in message.content:
        spamcounter = message.content
        if spamcounter.count("<@!") > 3:
            with open ('warnlist', 'rb') as fp:
                warnlist = pickle.load(fp)
            reason = "(AUTOMOD) Detected spam pinging of individual members."
            warnlist.append(message.author.id)
            warnlist.append(reason)
            embedVar = discord.Embed(title="AUTOMOD Warned {} successfully.".format(message.author.name), description="With reason: `{}`".format(reason), color=0xe6b919)
            embedVar2 = discord.Embed(title="Warning from {} / {}".format("AUTOMOD_BETA", "N/A"), description="`{}` - *Dyno may have banned you, which means you are unable to open tickets at this time, *This does not mean that this warning will be removed.**. *False warning? Open a ticket by sending a message to this bot, and get the warning removed.*".format(reason), color=0xff3a33)
            await message.author.send(embed=embedVar2)
            channellog = bot.get_channel(logchannel)
            await channellog.send(embed=embedVar)
            with open('warnlist', 'wb') as fp:
                pickle.dump(warnlist, fp)
            warnlist.clear()
        else:
            await bot.process_commands(message)
    else:
        await bot.process_commands(message)

bot.add_cog(Chat(bot))
bot.add_cog(Debug(bot))
bot.add_cog(Misc(bot))
bot.add_cog(Ticket(bot))
bot.add_cog(Moderation(bot))
bot.run(TOKEN)
