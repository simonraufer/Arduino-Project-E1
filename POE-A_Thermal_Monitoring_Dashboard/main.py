from data.dataset_builder import (
    build_dataset_from_folder
)

from analytics.report_summary import (
    generate_report_summary
)

from analytics.dataset_statistics import (
    calculate_dataset_statistics
)

from plotting.graph_generator import (
    generate_dataset_graphs
)

from reporting.pdf_exporter import (
    export_pdf_report
)

dataset = build_dataset_from_folder(
    "input"
)

statistics = calculate_dataset_statistics(
    dataset
)

summary = generate_report_summary(dataset, dataset.map_session_count)
generate_dataset_graphs(dataset)
print("Graphs generated.")

export_pdf_report(
    dataset, 
    statistics,
    summary
)

print()
print("DATASET SUMMARY")
print("================")
print()

print(
    f"Sensors Found: "
    f"{len(dataset.sensors)}"
)

print()

for address, stats in statistics.items():

    print(f"Address: {address}")

    print(
        f"Samples: "
        f"{stats['samples']}"
    )

    print(
        f"Min: "
        f"{stats['minimum']:.2f} °C"
    )

    print(
        f"Average: "
        f"{stats['average']:.2f} °C"
    )

    print(
        f"Max: "
        f"{stats['maximum']:.2f} °C"
    )

    print(
        f"Start: "
        f"{stats['start_time']}"
    )

    print(
        f"End: "
        f"{stats['end_time']}"
    )

    print()