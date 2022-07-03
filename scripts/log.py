""" Scripts responsible for logging """
import sys, os
import logging, logging.handlers
from logging.handlers import TimedRotatingFileHandler
formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
log_file = "info.log"

# Logging Levels #
##############
#  CRITICAL  #
#  ERROR     #
#  WARNING   #
#  INFO      #
#  DEBUG     #
##############

# Define Console Handler 
def get_console_handler():
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setFormatter(formatter)
  return console_handler

#Create Handlers(Filehandler with filename)
def get_file_handler():
  file_handler = TimedRotatingFileHandler(log_file, when='midnight', utc=True)
  file_handler.setFormatter(formatter)
  return file_handler

#Define Logger
def get_logger(logger_name):
  logger = logging.getLogger(logger_name)
  logger.setLevel(logging.DEBUG)
  logger.addHandler(get_console_handler())
  logger.addHandler(get_file_handler())
  logger.propagate = False
  return logger
