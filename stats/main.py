import logging

import stats.util.logging as log
import stats.util.config as config

import stats.bot.bot as bot

def init():
	global logger
	log.init()
	config.load()
	bot.init()
	logger = logging.getLogger('stats-bot')

def entrypoint():
	init()
	bot.get_channels()
