import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from langdetect import detect, LangDetectException
from datetime import datetime
from bot.csgo import Csgo
from bot.meeting import Meeting

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CENSOR_PASSWORD = os.getenv('CENSOR_PASSWORD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.')
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

censored_channels = {}  # channels under censorship with the time determining how long

csgo_role_id = 866730183993983016

guild_id = 440149644429885461


# Testing commands
@slash.slash(name="test",
             description="Testowa komenda Pana Miłosza",
             guild_ids=[guild_id])
async def test_slash(ctx):
    await ctx.send(await test(ctx), hidden=True)


@bot.command(name='test', help='Test command')
async def test_prefix(ctx):
    await test(ctx)


async def test(ctx):
    await ctx.send('Pan Miłosz rozpoczął test')
    return 'Pan Miłosz testuje'


# Help commands
@slash.slash(name="help",
             description="Shows this message",
             guild_ids=[guild_id],
             options=[
                 create_option(
                     name="command",
                     description="Command",
                     option_type=3,
                     required=False)
             ]
             )
async def help_slash(ctx, **kwargs):
    if not check_censorship(ctx):
        await ctx.send(custom_help(ctx, **kwargs))
    else:
        await ctx.send('Why would I have a polish command?')


def custom_help(ctx, **kwargs):
    if 'command' in kwargs.keys():
        help_text = "```"
        help_text += '/'
        params = kwargs['command'].split()
        for i, param in enumerate(params):
            if param == params[-1]:
                cog = ctx.bot.get_cog(param.lower())
                if cog is None:
                    command = ctx.bot.get_command(kwargs['command'])
                    if command is None:
                        if len(params) > 1:
                            return f'Command "{params[i - 1]}" has no subcommand named {param}'
                        return f'No command called "{param}" found.'
                    help_text += f'{command.name} \n\n'
                    help_text += command.help
                    help_text += "```"
                    return help_text
                help_text += f'{param} \n\n'
                for com in cog.get_commands():
                    help_text += f"  {com.name}   "
                    help_text += f"{com.help} \n\n"
                help_text += 'Commands: \n'
                for com in cog.get_commands():
                    for c in com.commands:
                        help_text += f"  {c.name}   "
                        help_text += f"{c.help} \n"
                help_text += "Type /help command for more info on a command.\n"
                help_text += "You can also type /help category for more info on a category."
                help_text += "```"
                return help_text
            elif param != params[0]:
                cog = ctx.bot.get_cog(param.lower())
                if cog is None:
                    return f'Command {params[i - 1]} has no subcommand named {param}'
                help_text += f'{param} '
            else:
                cog = ctx.bot.get_cog(param.lower())
                if cog is None:
                    return f'No command called "{param}" found.'
                help_text += f'{param} '
    else:
        help_text = "```"
        for cog_name in ctx.bot.cogs:
            help_text += f'{cog_name}: \n'
            cog = ctx.bot.get_cog(cog_name)
            for com in cog.get_commands():
                help_text += f"{com.name}   "
                help_text += f"{com.help} \n"
        help_text += 'No Category: \n'
        for com in ctx.bot.commands:
            if com.cog is None:
                help_text += f'{com.name}   '
                help_text += f"{com.help} \n"
        help_text += "Type /help command for more info on a command.\n"
        help_text += "You can also type /help category for more info on a category."
        help_text += "```"
    return help_text


# English censorship
async def censor(ctx, password):
    """
    Restricts channel on which the command was send to accepting only english-language messages
    :param ctx: discord context object
    :param password: password to activate censorship
    :return: information about establishing censorship
    """
    if password == CENSOR_PASSWORD:
        if ctx.channel not in censored_channels.keys():
            censored_channels[ctx.channel] = datetime.now()
            await ctx.send(':flag_gb: English time! :flag_gb:')
            return "Censorship has been activated"
        else:
            censored_channels.pop(ctx.channel)
            await ctx.send('You can speak any language that you please. For now...')
            return "Censorship has been de-activated"
    else:
        return "Wrong password!"


def check_censorship(ctx):
    """
    Returns True if there is censorship active and should be applied, and False otherwise
    :param ctx:
    :return:
    """
    message = None
    if type(ctx) == discord.Message:
        message = ctx

    if message is not None:
        if message.channel in censored_channels.keys():
            if (datetime.now() - censored_channels[message.channel]).total_seconds() > 3600:
                censored_channels.pop(message.channel)
            else:
                try:
                    lang = detect(message.content)
                except LangDetectException:
                    lang = 'null'
                if lang == 'pl':
                    return True
        return False

    if ctx.message is None:
        if ctx.channel in censored_channels.keys():
            if (datetime.now() - censored_channels[ctx.channel]).total_seconds() > 3600:
                censored_channels.pop(ctx.channel)
            else:
                try:
                    lang = detect(ctx.data['options'][0]['value'])
                except LangDetectException:
                    lang = 'null'
                if lang == 'pl':
                    return True
        return False

    return check_censorship(ctx.message)


@slash.slash(name="censor", description="English only!", guild_ids=[guild_id])
async def censor_slash(ctx, password):
    await ctx.send(await(censor(ctx, password)), hidden=True)


@bot.command(name='censor', help='English only!')
async def censor_prefix(ctx, password):
    await censor(ctx, password)


# Bot events
@bot.event
async def on_ready():
    print("Connected to discord")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        if check_censorship(message):
            await message.delete()
            await message.channel.send(f'Why would I have a polish command?')
        return

    #  Censorship part
    if message.content[0:7] == '.censor':
        await message.delete()

    if check_censorship(message):
        await message.delete()

    #  GitHub Premium part
    if 'github' in message.content.lower() or 'premium' in message.content.lower():
        await message.channel.send('<@&845436232204943401> GitHub Premium')

    check_censorship(message)

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        if check_censorship(ctx):
            try:
                await ctx.message.delete()
            except discord.errors.NotFound:
                pass
    raise error


bot.add_cog(Csgo(bot))
bot.add_cog(Meeting(bot))
bot.run(TOKEN)
