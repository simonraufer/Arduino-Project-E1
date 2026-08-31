import tkinter as tk

class DownloadDialog:

    def __init__(self, parent):

        self.result = None

        self.window = tk.Toplevel(parent)

        self.window.title(
            "Download Data"
        )

        self.window.geometry(
            "300x200"
        )

        self.window.grab_set()

        self.selection = tk.StringVar(
            value="last_session"
        )

        tk.Label(
            self.window,
            text="Select Timeframe",
            font=("Arial", 12, "bold")
        ).pack(
            pady=10
        )

        tk.Radiobutton(
            self.window,
            text="Last Session",
            variable=self.selection,
            value="last_session"
        ).pack(
            anchor="w",
            padx=20
        )

        tk.Radiobutton(
            self.window,
            text="All Data",
            variable=self.selection,
            value="all_data"
        ).pack(
            anchor="w",
            padx=20
        )

        button_frame = tk.Frame(
            self.window
        )

        button_frame.pack(
            pady=20
        )

        tk.Button(
            button_frame,
            text="Download",
            command=self.download
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            button_frame,
            text="Cancel",
            command=self.window.destroy
        ).pack(
            side="left",
            padx=5
        )

    def download(self):

        self.result = (
            self.selection.get()
        )

        self.window.destroy()

    def show(self):

        self.window.wait_window()

        return self.result
