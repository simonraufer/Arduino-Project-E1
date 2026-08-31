from gui.main_window import (
    MainWindow
)

from utils.startup import (
    create_required_folders
)


create_required_folders()

app = MainWindow()

app.run()