import tkinter as tk
from tkinter import messagebox

from reporting.report_generator import (
    generate_report
)

from gui.download_dialog import (
    DownloadDialog
)

from arduino.downloader import (
    download_last_session,
    download_all_data
)

class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "POE-A Thermal Monitoring Dashboard"
        )

        self.root.geometry(
            "500x250"
        )

        title = tk.Label(
            self.root,
            text="POE-A Thermal Monitoring Dashboard",
            font=("Arial", 14, "bold")
        )

        title.pack(
            pady=15
        )

        download_button = tk.Button(
            self.root,
            text="Download & Start Session",
            width=30,
            height=2,
            command=self.download_data
        )

        download_button.pack(
            pady=10
        )

        report_button = tk.Button(
            self.root,
            text="Generate PDF Report",
            width=30,
            height=2,
            command=self.generate_report
        )

        report_button.pack(
            pady=10
        )

        self.status_label = tk.Label(
            self.root,
            text="Ready"
        )

        self.status_label.pack(
            pady=15
        )

    def download_data(self):

        dialog = DownloadDialog(
            self.root
        )

        selection = dialog.show()

        if selection is None:
            return

        try:

            self.status_label.config(
                text="Downloading..."
            )

            self.root.update()

            if selection == "last_session":

                download_last_session()

                self.status_label.config(
                    text="Last session downloaded successfully"
                )

            elif selection == "all_data":

                download_all_data()

                self.status_label.config(
                    text="All data downloaded successfully"
                )

            messagebox.showinfo(
                "Success",
                "Download completed."
            )

        except Exception as error:

            self.status_label.config(
                text="Download failed"
            )

            messagebox.showerror(
                "Download Error",
                str(error)
            )
    
    def generate_report(self):
        try:
            self.status_label.config(
                text="Generating report..."
            )
            self.root.update()
            generate_report()
            self.status_label.config(
                text="Report generated successfully"
            )
            messagebox.showinfo(
                "Success",
                "PDF report generated."
            )
        except Exception as error:
            self.status_label.config(
                text="Error"
            )
            messagebox.showerror(
                "Error",
                str(error)
            )
    
    def run(self):
        self.root.mainloop()

        