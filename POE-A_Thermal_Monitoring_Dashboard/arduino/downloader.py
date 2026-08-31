import os
import requests
import time

from config import (
    ARDUINO_IP,
    MAP_FOLDER,
    TEMP_FOLDER
)


def start_new_session():

    requests.get(
        f"http://{ARDUINO_IP}/newsession",
        timeout=10
    )

def get_file_list():

    response = requests.get(
        f"http://{ARDUINO_IP}/filesjson",
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def download_file(filename):

    url = (
        f"http://{ARDUINO_IP}"
        f"/download?file={filename}"
    )

    response = requests.get(
        url,
        stream=True,
        timeout=600
    )

    response.raise_for_status()

    if filename.startswith("MAP_"):

        target_folder = MAP_FOLDER

    else:

        target_folder = TEMP_FOLDER

    os.makedirs(
        target_folder,
        exist_ok=True
    )

    filepath = os.path.join(
        target_folder,
        filename
    )

    with open(
        filepath,
        "wb"
    ) as file:

        for chunk in response.iter_content(
        chunk_size=4096
        ):  

            if chunk:

                file.write(chunk)

def download_last_session():

    clear_input_folders()

    start_new_session()

    time.sleep(2)

    file_list = get_file_list()

    inactive_maps = [

        entry["name"]

        for entry in file_list["maps"]

        if not entry["active"]
    ]

    latest_map = sorted(
        inactive_maps
    )[-1]

    latest_id = latest_map[
        4:7
    ]

    download_file(
        f"MAP_{latest_id}.CSV"
    )

    download_file(
        f"TEMP_{latest_id}.CSV"
    )

def download_all_data():

    clear_input_folders()

    start_new_session()

    time.sleep(2)

    file_list = get_file_list()

    for entry in file_list["maps"]:

        if not entry["active"]:

            download_file(
                entry["name"]
            )

    for entry in file_list["temperature"]:

        if not entry["active"]:

            download_file(
                entry["name"]
            )

def clear_input_folders():

    for folder in (
        MAP_FOLDER,
        TEMP_FOLDER
    ):

        if not os.path.exists(folder):

            continue

        for filename in os.listdir(folder):

            if filename.upper().endswith(".CSV"):

                filepath = os.path.join(
                    folder,
                    filename
                )

                os.remove(filepath)