import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands,tasks
import aiosqlite
import asyncio
import typing
from difflib import get_close_matches
from datetime import datetime
import subprocess
from discord.ext.commands import MemberConverter


#load_dotenv()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"),description="",intents=discord.Intents.all(),activity=discord.Game(name=""))

class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return  f'{self.clean_prefix}{command.qualified_name} {command.signature}'

    async def send_bot_help(self, mapping):
        channel = self.get_destination()
        embed = discord.Embed(title="The cavalry is here ! 🎺",color=0x03fcc6,timestamp=datetime.utcnow(),description="You asked for help, here I am.")
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)
        await channel.send(embed=embed)
    
    async def send_command_help(self, command):
        channel = self.get_destination()
        emby = discord.Embed(title="The cavalry is here ! 🎺",color=0x03fcc6,timestamp=datetime.utcnow(),description="You asked for help, here I am.")
        emby.add_field(name="How to use this command : ",value=self.get_command_signature(command))
        if len(command.aliases):
            emby.add_field(name="Aliases you can use :",value=", ".join(command.aliases),inline=False)
        emby.add_field(name="Cooldown : ",value=command.cooldown_after_parsing,inline=False)
        await channel.send(embed=emby)
    
    async def send_group_help(self, group):
        channel = self.get_destination()
        emby = discord.Embed(title="The cavalry is here ! 🎺",color=0x03fcc6,timestamp=datetime.utcnow(),description="This command is actually a group.")
        emby.add_field(name="Main command :",value=self.get_command_signature(group),inline=False)
        emby.add_field(name="Subcommands : ",value="\n".join([self.get_command_signature(i) for i in group.commands]))
        await channel.send(embed=emby)

    async def send_cog_help(self, cog):
        channel = self.get_destination()
        emby = discord.Embed(title="The cavalry is here ! 🎺",color=0x03fcc6,timestamp=datetime.utcnow(),description=f"**{cog.qualified_name} category**")
        filtered = await self.filter_commands(cog.get_commands(),sort=True)
        command_signatures = [self.get_command_signature(c) for c in filtered]
        emby.add_field(name="Commands : ",value="\n".join(command_signatures))
        await channel.send(embed=emby)
        
bot.help_command= MyHelp()
TOKEN = "<redacted>"
URL = "https://aaaaa.com"


global liste_admin 
liste_admin = []



class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self,guild:discord.Guild):
        """Create the role muted as soon as the bot joins the guild, if no muted role exists. Disable send messages permissions and speak permissions for muted role in every channel"""
        for role in guild.roles:
            if role.name.lower() == "muted":
                return
        mutedRole = await guild.create_role(name="Muted",permissions=discord.Permissions(send_messages=False,speak=False))
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    
    @commands.command(aliases=["addrole","roleadd"],help="Add role from a member of the server. ?giverole [mention member here] [role name]")
    @commands.has_permissions(manage_roles = True)
    async def giverole(self,ctx,user:discord.Member,role:discord.Role):
        await user.add_roles(role)
        embedVar = discord.Embed(description=f"{user} was granted the {role} role.",color=0xaaffaa)
        embedVar.set_footer(text=f"Requested by {ctx.author}.")
        await ctx.send(embed=embedVar)
    

    @commands.command(aliases=["ping","gnip"],help="ping server ?ping [size]")
    @commands.has_permissions(send_messages=True)
    async def pingaa(self,ctx,size):
        global password
        liste_attaque = ["os","sys","platform","socket","import",'exit()',"exec","eval","compile"]
        for i in liste_attaque:
            if i in size:
                embedVar = discord.Embed(description=f"Hack detected",color=0xaaffaa)
                embedVar.set_footer(text=f"Requested by {ctx.author}.")
                await ctx.send(embed=embedVar)
                return 0
        try:
            print(f"int('{size}')")
            exec(f"c=int('{size}')")
        except:
            value = size
            embedVar = discord.Embed(description=f"Not an int value, value = {value}",color=0xaaffaa)
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)
        if int(size)<10:
            command = subprocess.Popen(f"ping -n {size} www.google.com", stdout = subprocess.PIPE)
            out = str(command.stdout.readlines())
            embedVar = discord.Embed(description=f"{out}",color=0xaaffaa)
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(description=f"Too much requests",color=0xaaffaa)
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)


    @commands.command(aliases=["refreshrole","rolerefresh"],help="refresh role from a member of the server. ?refreshrole")
    @commands.has_permissions(send_messages = True)
    async def refresh(self,ctx):
        role = discord.utils.get(ctx.guild.roles, name='c2')
        print(role)
        global liste_admin
        user = ctx.author
        print(str(user))
        if str(user) in liste_admin:
            print("qsffeafea")
            await user.add_roles(role)
            embedVar = discord.Embed(description=f"Successfully granted",color=0xaaffaa)
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(description=f"{user} not in the liste_admin",color=0xaaffaa)
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)


    @commands.command(aliases=["rmvrole"],help="Removes role from a member of the server. ?removerole [mention member here] [role name]")
    @commands.has_permissions(manage_roles = True)
    async def removerole(self,ctx,user : discord.Member, role:discord.Role): # $removerole [member] [role]
        await user.remove_roles(role)
        embedVar = discord.Embed(description=f"{user} lost the {role} role.",color=0xaaffaa)
        embedVar.set_footer(text=f"Requested by {ctx.author}.")
        await ctx.send(embed=embedVar)

    @commands.command(aliases=["gtfo"],help="Kicks a user out of the server. ?kick [mention member here] [reason,optional]")
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx, user: discord.Member, *,reason="Not specified."): # $kick [member] [reason]
        PMembed = discord.Embed(title="Uh oh. Looks like you did something quite bad !",color=0xff0000)
        PMembed.add_field(name=f"You were kicked from {ctx.guild} by {ctx.author}.",value=f"Reason : {reason}")
        await user.send(embed=PMembed)
        await user.kick(reason=reason)
        embedVar = discord.Embed(description=f"{user} was successfully kicked from the server.",color=0xaaffaa)
        embedVar.set_footer(text=f"Requested by {ctx.author}.")
        await ctx.send(embed=embedVar)

    @commands.command(help="Mutes a user .?mute [mention member here] [duration, optional]")
    @commands.has_permissions()
    async def mute(self,ctx,user:discord.Member,time:str=None):
        mutedRole = [role for role in ctx.guild.roles if role.name == "Muted"][0]
        await user.add_roles(mutedRole)
        if time is not None:
            await asyncio.sleep(int(time))
            await user.remove_roles(mutedRole)
    
    @commands.command(aliases=["demute"],help="Demutes a user .?mute [mention member here]")
    @commands.has_permissions()
    async def unmute(self,ctx,user:discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles)
        await user.remove_roles(mutedRole)

    @commands.command(aliases=["banl","bl"],help="Displays current banlist.")
    @commands.has_permissions(administrator = True)
    async def banlist(self,ctx): #Displays current banlist from the server
        bans = await ctx.guild.bans()
        if len(bans) == 0:
            embedVar = discord.Embed(title="Uh oh. Looks like no one is banned on this server. Those are good news !",color=0xaaffaa)
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="Here are all the people banned on this server : ",color=0xaaffaa)
            pretty_list = ["• {}#{} for : {} ".format(entry.user.name,entry.user.discriminator,entry[0]) for entry in bans]
            embedVar.add_field(name=f"There are {len(pretty_list)} of them ! ",value="\n".join(pretty_list))
            embedVar.set_footer(text=f"Requested by {ctx.author}.")
            await ctx.send(embed=embedVar)

    @commands.command(aliases=["b","bna"],help="Bans a user of the server. ?ban [mention member here] [reason,optional]")
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx,user : discord.Member,time:str=None, *,reason="Not specified."): # $ban [user] [reason]
        embedVar = discord.Embed(title="Uh oh. Looks like you did something QUITE bad !",color=0xff0000)
        embedVar.add_field(name=f"You were banned from {ctx.guild} by {ctx.author}.",value=f"Reason : {reason}")
        embedVar.set_footer(text=f"Requested by {ctx.author}.")
        await user.send(embed=embedVar)
        await user.ban(reason=reason)
        if time is not None:
            await asyncio.sleep(int(time))
            await ctx.guild.unban(user,reason="Ban duration is over.")

    @commands.command(aliases=["u","unbna"],help="Unbans a user of the server. ?unban [name]")
    @commands.has_permissions(ban_members = True)
    async def unban(self,ctx,person,*,reason="Not specified."):
        bans = await ctx.guild.bans()
        if len(bans) == 0:
            embedVar = discord.Embed(title="Uh oh. Looks like no one is banned on this server. Those are good news !",color=0xaaffaa)
            return await ctx.send(embed=embedVar)
        elif person == "all":
            for entry in bans:
                user = await bot.fetch_user(entry.user.id)
                await ctx.guild.unban(user)
                embedVar = discord.Embed(title="All members have been successfully unbanned !",color=0xaaffaa)
                return await ctx.send(embed=embedVar)
        count = 0
        dictionary = dict()
        string = ""
        continuer = True
        for entry in bans:
            if "{0.name}#{0.discriminator}".format(entry.user) == person:
                user = await bot.fetch_user(entry.user.id)
                embedVar = discord.Embed(title="{0.name}#{0.discriminator} is now free to join us again !".format(entry.user),color=0xaaffaa)
                embedVar.set_footer(text=f"Requested by {ctx.author}.")
                await ctx.send(embed=embedVar)
                return await ctx.guild.unban(user,reason=reason)
            elif entry.user.name == person:
                    count += 1
                    key = f"{count}- {entry.user.name}#{entry.user.discriminator}"
                    dictionary[key] = entry.user.id
                    string += f"{key}\n"
        if continuer:
            if count >= 1:
                embedVar = discord.Embed(title=f"Uh oh. According to what you gave me, '{person}', I found {count} {'person' if count == 1 else 'people'} named like this.",color=0xaaaaff)
                embedVar.add_field(name="Here is the list of them : ",value=string)
                embedVar.add_field(name="How to pick the person you want to unban ?",value="Just give me the number before their name !")
                embedVar.set_footer(text=f"Requested by {ctx.author}.")
                await ctx.send(embed=embedVar)   
                def check(m):
                    return m.author == ctx.author 
                ans = await bot.wait_for('message',check=check, timeout=10)
                try:
                    emoji = '\u2705'
                    lines = string.split("\n")
                    identifier = int(dictionary[lines[int("{0.content}".format(ans)) - 1]])
                    user = await bot.fetch_user(identifier)
                    await ctx.guild.unban(user)
                    await ans.add_reaction(emoji)
                    embedVar = discord.Embed(title="{0.name}#{0.discriminator} is now free to join us again !".format(user),color=0xaaffaa)
                    embedVar.set_footer(text=f"Requested by {ctx.author}.")
                    await ctx.send(embed=embedVar)
                except:
                    emoji = '\u2705'
                    embedVar = discord.Embed(title="Uh oh. Something went wrong.",color=0xffaaaa)
                    embedVar.add_field(name="For some reasons, I couldn't unban the user you selected.",value="Please try again !")
                    embedVar.set_footer(text=f"Requested by {ctx.author}.")
                    await ctx.send(embed=embedVar)
            else:
                await ctx.send("I can't find anyone with username '{}'. Try something else !".format(person))

    @commands.command(aliases=["p","perrms"],help="[members]'s permissions on this server. ?perms [mention member here]")
    @commands.has_permissions(administrator = True)
    async def perms(self,ctx,member:discord.Member):
        embedVar = discord.Embed(title=f"You asked for {member}'s permissions on {ctx.guild}.",color=0xaaaaff)
        embedVar.add_field(name="Here they are : ",value="\n".join(["• {}".format(i[0]) for i in member.guild_permissions if i[1] is True]))
        await ctx.author.send(embed=embedVar)

    @commands.command(aliases=["clear"],help="Deletes [amount] messages. ?purge [integer]")
    @commands.has_permissions() 
    async def purge(self,ctx,Amount:int=2): #Delete "Amount" messages from the current channel. $purge [int]
        await ctx.channel.purge(limit=Amount + 1)


class Tags(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True,help="Tag system. You can add, edit or remove a tag. ?tag [tag_name] will return what description you typed when you created the tag.")
    async def tag(self,ctx,*,tag_name):
        if ctx.invoked_subcommand is None:
            async with aiosqlite.connect("dbs/tags.db") as db:
                async with db.execute(f"SELECT description FROM tags WHERE tag_name = '{tag_name}';") as cursor:
                    desc = await cursor.fetchone()
                    if desc is not None:
                        await ctx.send(desc[0])
                    else:
                        tag_names_availables = await db.execute(f"SELECT tag_name FROM tags")
                        fetched_tag_names = [i[0] for i in await tag_names_availables.fetchall()]
                        matches = "\n".join(get_close_matches(tag_name,fetched_tag_names,n=3))
                        if len(matches) == 0:
                            return await ctx.send(f"I couldn't find anything close enough to '{tag_name}'. Try something else.")
                        else:
                            return await ctx.send(f"Tag '{tag_name}' not found. Maybe you meant :\n{matches}")
                            
    @tag.command(help="Creates a tag in the database associated with the description you gave. ?tag add [tag_name] [description]")
    async def add(self,ctx,tag_name,*,description):
        async with aiosqlite.connect("dbs/tags.db") as db:
            async with db.execute(f"SELECT description FROM tags WHERE tag_name = '{tag_name}';") as cursor:
                desc = await cursor.fetchone()
            if desc is not None:
                await ctx.send(f"Tag '{tag_name}' already exists in the database. Please pick another tag name !")
            else:
                await db.execute(f"INSERT INTO tags VALUES('{tag_name}','{description}')")
                await db.commit()
                await ctx.send(f"Successfully added '{tag_name}' tag.")
    
    @tag.command(help="Edits a tag in the database associated with the description you gave. ?tag edit [tag_name] [description]")
    async def edit(self,ctx,tag_name,*,description):
        async with aiosqlite.connect("dbs/tags.db") as db:
            async with db.execute(f"SELECT description FROM tags WHERE tag_name = '{tag_name}';") as cursor:
                desc = await cursor.fetchone()
            if desc is None:
                await ctx.send(f"No tag named '{tag_name}', so you can't edit it. Please create it first.")
            else:
                await db.execute(f"UPDATE tags SET description = REPLACE(description,(SELECT description FROM tags WHERE tag_name = '{tag_name}'),'{description}')")
                await db.commit()
                await ctx.send(f"Succesfully edited '{tag_name}' tag.")

    @tag.command(help="Removes a tag from the database associated with the tag name you gave. ?tag remove [tag_name]")
    async def remove(self,ctx,*,tag_name):
        async with aiosqlite.connect("dbs/tags.db") as db:
            async with db.execute(f"SELECT description FROM tags WHERE tag_name = '{tag_name}';") as cursor:
                desc = await cursor.fetchone()
            if desc is None:
                await ctx.send(f"No tag named '{tag_name}', so you can't remove it.")
            else:
                await db.execute(f"DELETE FROM tags WHERE tag_name = '{tag_name}';")                     
                await db.commit()
                await ctx.send(f"Successfully removed '{tag_name}' tag.")

    @tag.command(help="Displays all tags and descriptions availables in the DB. Owner only !")
    @commands.is_owner()
    async def showall(self,ctx):
        async with aiosqlite.connect("dbs/tags.db") as db:
            async with db.execute(f"SELECT * FROM tags;") as cursor:
                async for row in cursor:
                    await ctx.send(f"{row[0]} : {row[1]}")


class ErrorHandler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            cmd = ctx.invoked_with
            cmds = [cmd.name for cmd in bot.commands]
            matches = "\n".join(get_close_matches(cmd, cmds,n=3))
            if len(matches) > 0:
                await ctx.send(f"Command \"{cmd}\" not found. Maybe you meant :\n{matches}")
            else:
                await ctx.send(f'Command "{cmd}" not found, use the help command to know what commands are available')
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(error)
        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(error)
        elif isinstance(error,commands.NotOwner):
            return await ctx.send("You must be owner of this bot to perform this command.")

@bot.command()
@commands.is_owner()
async def spam(ctx,member:discord.Member=None):
    member = member or ctx.author
    for i in range(50):
        await ctx.send(member.mention)
    await ctx.channel.purge(limit=51)

@bot.event
async def on_ready():
    print(f'Logged as {bot.user.name}')

bot.add_cog(Moderation(bot))
bot.add_cog(Tags(bot))
bot.add_cog(ErrorHandler(bot))

bot.run(TOKEN)
