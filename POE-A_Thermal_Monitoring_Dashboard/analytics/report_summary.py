def generate_report_summary(
    dataset,
    map_session_count
):

    all_start_times = []
    all_end_times = []

    total_samples = 0

    for sensor in dataset.sensors.values():

        all_start_times.append(
            sensor.data["Timestamp"].min()
        )

        all_end_times.append(
            sensor.data["Timestamp"].max()
        )

        total_samples += len(
            sensor.data
        )

    dataset_start = min(
        all_start_times
    )

    dataset_end = max(
        all_end_times
    )

    duration_hours = (
        dataset_end - dataset_start
    ).total_seconds() / 3600

    return {

        "sensor_count":
            len(dataset.sensors),

        "total_samples":
            total_samples,

        "dataset_start":
            dataset_start,

        "dataset_end":
            dataset_end,

        "duration_hours":
            duration_hours,

        "map_sessions":
            map_session_count
    }