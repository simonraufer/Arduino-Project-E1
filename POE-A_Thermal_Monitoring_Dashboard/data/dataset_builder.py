from data.csv_loader import (
    load_map_file, 
    load_temp_file, 
    build_sensor_mapping
)

from data.data_models import (
    Dataset,
    SensorHistory
)

from config import (
    INVALID_TEMPERATURE
)

import os
import pandas as pd

####################################################################################################

def build_dataset(map_file, temp_file):
    map_id, map_df = load_map_file(map_file)
    temp_df = load_temp_file(temp_file)
    mapping = build_sensor_mapping(map_df)
    sensors = {}

    for column in temp_df.columns:
        if column == "Timestamp":
            continue

        address = mapping.get(column)

        if address is None:
            continue

        sensor_df = pd.DataFrame({
            "Timestamp": temp_df["Timestamp"],
            "Temperature": temp_df[column]
        })

        # Remove invalid sensor readings
        sensor_df = sensor_df[
            sensor_df["Temperature"] != -127
        ]

        #remove NaN values
        sensor_df = sensor_df.dropna()

        sensors[address] = SensorHistory(
            address=address, 
            data=sensor_df
        )

    return Dataset(
        sensors=sensors,
        map_session_count=1
    )

####################################################################################################

def build_dataset_from_folder(input_folder):

    maps_folder = os.path.join(input_folder, "maps")
    temps_folder = os.path.join(input_folder, "temperatures")
    sensor_data = {}

    map_files = sorted(
        f for f in os.listdir(maps_folder)
        if f.upper().endswith(".CSV")
    )

    for map_file in map_files:
        map_path = os.path.join(
            maps_folder, map_file
        )

        map_id, map_df = load_map_file(
            map_path
        )
        print(f"Loading MapID {map_id}")
        print(f"Map file: {map_file}")

        temp_filename = f"TEMP_{map_id:03d}.CSV"
        temp_path = os.path.join(
            temps_folder,
            temp_filename
        )

        if not os.path.exists(temp_path):
            print(
                f"WARNING: Missing TEMP file for MapID {map_id}"
            )

            continue

        temp_df = load_temp_file(
            temp_path
        )

        print(f"Temperature samples: {len(temp_df)}")

        mapping = build_sensor_mapping(
            map_df
        )

        for column in temp_df.columns:

            if column == "Timestamp":
                continue

            address = mapping.get(column)

            if address is None:
                continue

            sensor_df = pd.DataFrame({
                "Timestamp": temp_df["Timestamp"],
                "Temperature": temp_df[column]
            })

            # Remove invalid temperatures
            sensor_df = sensor_df[
                sensor_df["Temperature"] != INVALID_TEMPERATURE
            ]

            #Remove NaN
            sensor_df = sensor_df.dropna()
            if address not in sensor_data:
                sensor_data[address] = []
            sensor_data[address].append(
                sensor_df
            )

    return finalize_dataset(
        sensor_data,
        len(map_files)
    )

####################################################################################################

def finalize_dataset(
        sensor_data, 
        map_session_count
):

    sensors = {}

    for address, dataframes in sensor_data.items():

        combined = pd.concat(
            dataframes, 
            ignore_index=True
        )
        combined = combined.sort_values(
            by="Timestamp"
        )

        combined = combined.drop_duplicates(
            subset="Timestamp", 
            keep="last"
        )

        combined = combined.reset_index(
            drop=True
        )

        sensors[address] = SensorHistory(
            address=address, 
            data=combined
        )

    print(
        f"{address}: "
        f"{len(dataframes)} dataframe(s)"
    )

    return Dataset(
        sensors=sensors,
        map_session_count=map_session_count
    )
