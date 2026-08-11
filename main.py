import sys
import asyncio

from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop

from nova.config import AppConfig
from nova.ui import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("Nova Launcher")
    app.setOrganizationName("Nova")
    config = AppConfig()

    window = MainWindow(config)
    window.show()

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()
