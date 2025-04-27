# Tray Demo

This repository contains `tray.py`, a simple and quick example of how to create a system tray icon in Python that is compatible with PyInstaller.

## Features

-   Creates a basic system tray icon using `pystray` and `Pillow` (PIL).
-   The icon has a context menu with "Show", "Settings", and "Quit" options.
-   Shows desktop notifications using `notifypy` when menu items are selected.
-   Runs the tray icon in a separate thread to avoid blocking the main application logic.
-   Includes a basic icon image generated with `Pillow`.

## Requirements

-   Python 3.6+
-   `pystray` library
-   `Pillow` library
-   `notifypy` library

## Installation

1. Clone this repository.
2. Install the required dependencies:

    ```bash
    pip install pystray Pillow notifypy
    ```

## Usage

Run the script directly:

```bash
python tray.py
```

The script will start and a system tray icon should appear. You can interact with it using the right-click context menu.

To stop the application, select "Quit" from the tray icon menu or press `Ctrl+C` in the terminal where the script is running.

## Packaging

You can package the script into a standalone executable using `PyInstaller`.

1. Install `PyInstaller`:

    ```bash
    pip install pyinstaller
    ```

2. Run the following command in the terminal from the project directory:

    ```bash
    pyinstaller --onefile --windowed tray.py
    ```

    - `--onefile`: Packages everything into a single executable file.
    - `--windowed` / `--noconsole`: Prevents a console window from appearing when the application is run (suitable for GUI/tray applications).

    This will create a `dist` directory containing the standalone executable.
