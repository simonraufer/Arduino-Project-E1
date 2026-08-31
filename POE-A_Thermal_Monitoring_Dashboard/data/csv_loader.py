import pandas as pd

#########################################################################################################

def load_map_file(filepath):
    """
    Load MAP_xxx.csv file.
    returns:
      map_id
      map:dataframe
    """

    # Read first line separately
    with open(filepath, "r") as file:
        first_line = file.readline().strip()

    # Example:
    # MapID,3

    parts = first_line.split(",")
    map_id = int(parts[1])

    # Skip metadata row
    map_df = pd.read_csv(filepath, skiprows=1)

    return map_id, map_df

#########################################################################################################

def load_temp_file(filepath):
    """
    Load TEMP_xxx.csv file.
    """

    temp_df = pd.read_csv(filepath)

    temp_df["Timestamp"] = pd.to_datetime(
        temp_df["Timestamp"], format="%Y/%m/%d %H:%M:%S"
    )

    return temp_df

#########################################################################################################

def build_sensor_mapping(map_df):
    """
    Converts:

        SensorIndex Address
        1           287024...
        2           283770...

    into:

        {
            "S1": "...", 
            "S2": "..."
        }
    """

    mapping = {}

    for _, row in map_df.iterrows():

        sensor_column = f"S{int(row['SensorIndex'])}"

        mapping[sensor_column] = row["Address"]

    return mapping