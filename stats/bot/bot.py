import csv
import discord
import logging
from discord.ext import commands

import stats.util.config as config

logger = logging.getLogger('stats-bot')

def init():
    global bot
    bot = discord.ext.commands.Bot(command_prefix='?')

def get_channels():
    logger.info("Starting bot...")
    bot.loop.create_task(get_ch())
    bot.run(config.creds['discord']['token'])

async def get_ch():
    await bot.wait_until_ready()
    logger.info("Getting data...")

    channel_stats = {}
    user_stats = {}

    total_count = 0
    channel_count = 0
    for channel in bot.get_all_channels():
        if not isinstance(channel, discord.channel.TextChannel):
            continue

        print(f"'{channel.name}'")

        async for message in channel.history(limit=None):
            if message.author.bot:
                continue

            name = f"{message.author.name}#{message.author.discriminator}"
            try:
                nick = message.author.nick
            except:
                nick = "<unknown>"

            if name in user_stats:
                user_stats[name][0] += 1
            else:
                user_stats[name] = [1, nick]

            channel_count += 1
            print(f" - {channel_count}", end='\r')

        channel_stats[channel.name] = channel_count
        total_count += channel_count
        channel_count = 0

        print("")

    logger.info("Saving stats...")
    save_users(user_stats)
    save_channel(channel_stats)

    logger.info("Stopping bot...")
    bot.loop.stop()


def save_channel(stats):
    OUTPUT_PATH = "channel_stats.csv"
    writer = csv.writer(open(OUTPUT_PATH, "w+"))
    writer.writerow(["Channel Name", "Message Count"])

    for [name, count] in stats.items():
        writer.writerow([name, count])


def save_users(stats):
    OUTPUT_PATH = "user_stats.csv"
    writer = csv.writer(open(OUTPUT_PATH, "w+"))
    writer.writerow(["User Name", "Nick Name", "Message Count"])

    for [name, [count, nick]] in stats.items():
        writer.writerow([name, nick, count])
