import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import (
    GRAPH_Y_MAX,
    GRAPH_Y_MIN,
    GRAPH_OUTPUT_FOLDER
)

def generate_sensor_graph( address, sensor_history, output_folder):
    """
    Generate one graph per sensor.
    """

    os.makedirs(
        output_folder, 
        exist_ok=True
    )

    plt.figure(figsize=(16, 4))

    plt.plot(
        sensor_history.data["Timestamp"],
        sensor_history.data["Temperature"],
        linewidth=1
    )

    plt.title(f"Sensor {address}")

    plt.xlabel("Time")
    plt.ylabel("Temperature [°C]")

    plt.grid(True)

    ax = plt.gca()

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter( "%Y-%m-%d\n%H:%M:%S")
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.ylim(GRAPH_Y_MIN, GRAPH_Y_MAX)

    plt.tight_layout()

    filename = os.path.join(
        output_folder, f"{address}.png"
    )

    plt.savefig(
        filename, 
        dpi=300
    )

    plt.close()

####################################################################################################

def generate_dataset_graphs(dataset, output_folder= GRAPH_OUTPUT_FOLDER):
    """
    Generate graphs for all sensors.
    """
    clear_graph_folder(output_folder)

    for(address, sensor) in dataset.sensors.items():
        generate_sensor_graph(address, sensor, output_folder)

####################################################################################################

def clear_graph_folder(graph_folder):
    """
    Remove old graph PNGs before generating a new dataset.
    """

    if not os.path.exists(graph_folder):
        return

    for filename in os.listdir(graph_folder):
        if filename.lower().endswith(".png"):
            os.remove(
                os.path.join(
                    graph_folder,
                    filename
                )
            )
