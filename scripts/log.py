""" Scripts responsible for logging """

import sys, os
import logging, logging.handlers
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
log_file = "info.log"
from config import Config

# Logging Levels #
##############
#  CRITICAL  #
#  ERROR     #
#  WARNING   #
#  INFO      #
#  DEBUG     #
##############


def get_console_handler():
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(formatter)
  return console_handler


def get_file_handler():
  file_handler = TimedRotatingFileHandler(Config.LOG_FILE, when='midnight')
  file_handler.setFormatter(formatter)
  return file_handler


def get_logger(logger_name):
  logger = logging.getLogger(logger_name)
  # better to have too much log than not enough
  logger.setLevel(logging.DEBUG)
  logger.addHandler(get_console_handler())
  logger.addHandler(get_file_handler())
  # with this pattern, it's rarely necessary to propagate the error up to parent
  logger.propagate = False
  return logger
