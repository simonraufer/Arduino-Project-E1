def calculate_sensor_statistics(sensor_history):
    """
    Calculate statistics for a single sensor.
    """

    temperatures = sensor_history.data["Temperature"]

    return {
        "samples": len(temperatures), 
        "minimum": temperatures.min(), 
        "average": temperatures.mean(), 
        "maximum": temperatures.max(), 
        "start_time": sensor_history.data["Timestamp"].min(),
        "end_time": sensor_history.data["Timestamp"].max(),
        "duration_hours": (
            sensor_history.data["Timestamp"].max()
            -
            sensor_history.data["Timestamp"].min()
        ).total_seconds()/3600
    }

####################################################################################################

def calculate_dataset_statistics(dataset):
    """
    Calculate statistics for the entire dataset.
    """

    statistics = {}

    for address, sensor in dataset.sensors.items():

        statistics[address] = (
            calculate_sensor_statistics(sensor)
        )

    return statistics