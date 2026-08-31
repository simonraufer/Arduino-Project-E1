import os

# APP Names

REPORT_FILENAME_PREFIX = "POEA_Report"
PDF_TITLE= "POE-A Thermal Monitoring Report"
APP_NAME = "POE-A Thermal Monitoring Dashboard"

#Arduino 

ARDUINO_IP = "10.2.4.114"

# Application paths

APP_DATA_FOLDER = "POEA_Dashboard_Data"

CONFIG_FOLDER = os.path.join(APP_DATA_FOLDER, "config")
INPUT_FOLDER = os.path.join(APP_DATA_FOLDER, "input")
MAP_FOLDER = os.path.join(APP_DATA_FOLDER, "input/maps")
TEMP_FOLDER = os.path.join(APP_DATA_FOLDER, "input/temperatures")

GRAPH_OUTPUT_FOLDER = os.path.join(APP_DATA_FOLDER, "graphs")
REPORT_OUTPUT_FOLDER = os.path.join(APP_DATA_FOLDER, "reports")

# Graph settings

GRAPH_Y_MIN = 18
GRAPH_Y_MAX = 50

# Data filtering

INVALID_TEMPERATURE = -127