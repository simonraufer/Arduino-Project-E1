from config import INPUT_FOLDER

from data.dataset_builder import (
    build_dataset_from_folder
)

from analytics.dataset_statistics import (
    calculate_dataset_statistics
)

from analytics.report_summary import (
    generate_report_summary
)

from plotting.graph_generator import (
    generate_dataset_graphs
)

from reporting.pdf_exporter import (
    export_pdf_report
)


def generate_report():

    dataset = build_dataset_from_folder(
        INPUT_FOLDER
    )

    statistics = calculate_dataset_statistics(
        dataset
    )

    summary = generate_report_summary(
        dataset,
        dataset.map_session_count
    )

    generate_dataset_graphs(
        dataset
    )

    export_pdf_report(
        dataset,
        statistics,
        summary
    )

    return True