import os

from config import (
    APP_DATA_FOLDER,
    CONFIG_FOLDER,
    INPUT_FOLDER,
    MAP_FOLDER,
    TEMP_FOLDER,
    GRAPH_OUTPUT_FOLDER,
    REPORT_OUTPUT_FOLDER
)


def create_required_folders():
    """
    Create all required application folders.
    """

    folders = [

        APP_DATA_FOLDER,

        CONFIG_FOLDER,

        INPUT_FOLDER,

        MAP_FOLDER,

        TEMP_FOLDER,

        GRAPH_OUTPUT_FOLDER,

        REPORT_OUTPUT_FOLDER
    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )

    print("Application folders verified.")
