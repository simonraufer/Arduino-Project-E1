import os

from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image
)
from reportlab.lib.styles import (
    getSampleStyleSheet
)
from reportlab.lib.pagesizes import (
    A4, 
    landscape
)
from config import (
    GRAPH_OUTPUT_FOLDER,
    REPORT_OUTPUT_FOLDER,
    REPORT_FILENAME_PREFIX,
    PDF_TITLE
)

####################################################################################################

def export_pdf_report(
        dataset, 
        statistics, 
        summary,
        graph_folder=GRAPH_OUTPUT_FOLDER,
        output_file=None
):
    all_start_times = []
    all_end_times =[]

    for sensor in dataset.sensors.values():
        all_start_times.append(sensor.data["Timestamp"].min())
        all_end_times.append(sensor.data["Timestamp"].max())

    dataset_start = min(all_start_times)
    dataset_end = max(all_end_times)

    report_filename = (
        f"{REPORT_FILENAME_PREFIX}_"
        f"{dataset_start.strftime('%Y-%m-%d')}"
        f"_to_"
        f"{dataset_end.strftime('%Y-%m-%d')}.pdf"
    )

    if output_file is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        output_file = os.path.join(REPORT_OUTPUT_FOLDER, report_filename)

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True
    )

    document = SimpleDocTemplate(
        output_file,
        pagesize=landscape(A4)
    )

    styles = getSampleStyleSheet()

    elements = []

    # COVER PAGE ##################################

    elements.append(
        Paragraph(
            PDF_TITLE,
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Generated: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            f"Dataset Start: "
            f"{summary['dataset_start'].strftime('%Y-%m-%d %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Dataset End: "
            f"{summary['dataset_end'].strftime('%Y-%m-%d %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Monitoring Duration: "
            f"{summary['duration_hours']:.1f} Hours",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            f"Sensors Found: "
            f"{summary['sensor_count']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Samples: "
            f"{summary['total_samples']:,}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Map Sessions Found: "
            f"{summary['map_sessions']}",
            styles["Normal"]
        )
    )

    elements.append(
        PageBreak()
    )

    # SENSOR PAGES ############################################

    for address, stats in statistics.items():

        elements.append(
            Paragraph(
                f"Sensor Address: {address}",
                styles["Heading1"]
            )
        )

        elements.append(
            Spacer(1, 8)
        )

        elements.append(
            Paragraph(
                f"Samples: {stats['samples']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Minimum: {stats['minimum']:.2f} °C",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Average: {stats['average']:.2f} °C",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Maximum: {stats['maximum']:.2f} °C",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Start: {stats['start_time']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"End: {stats['end_time']}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )        

        graph_path = os.path.join(
            graph_folder,
            f"{address}.png"
        )

        if os.path.exists(graph_path):
            elements.append(
                Image(
                    graph_path, 
                    width=700,
                    height=250
                )
            )

        elements.append(
            PageBreak()
        )

    document.build(
        elements
    )

    print(
        f"PDF generated: {output_file}"
    )