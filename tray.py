import sys
import threading

import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw


def create_image(width=64, height=64):
    """Create an eye-like icon."""

    print("Creating icon image")
    # Create a transparent image (RGBA mode with transparent background)
    image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Eye outline (white)
    draw.ellipse((width * 0.1, height * 0.2, width * 0.9, height * 0.8), fill="white")

    # Iris (colored part of the eye)
    draw.ellipse((width * 0.3, height * 0.3, width * 0.7, height * 0.7), fill="gray")

    # Pupil (black center)
    draw.ellipse((width * 0.4, height * 0.4, width * 0.6, height * 0.6), fill="black")

    # Highlight/reflection (small white dot)
    draw.ellipse((width * 0.45, height * 0.45, width * 0.5, height * 0.5), fill="white")

    print("Icon image created successfully")
    return image


def on_show(icon, item):
    print("Show option selected")
    icon.notify('You have selected "Show".')


def on_settings(icon, item):
    print("Settings option selected")
    icon.notify("Opening settings...")


def on_quit(icon, item, stop_event):
    print("Quit option selected")
    stop_event.set()


def create_menu(stop_event):
    print("Creating menu items")
    return (
        item("Show", on_show),
        item("Settings", on_settings),
        item("Quit", lambda icon, item: on_quit(icon, item, stop_event)),
    )


def run_tray_in_thread(stop_event):
    """Run the tray icon in a daemon thread and return the icon and thread."""

    print("Initializing tray icon in thread")
    icon = pystray.Icon(
        name="tray_demo",
        title="Tray Demo",
        icon=create_image(),
        menu=pystray.Menu(*create_menu(stop_event)),
    )

    def _run_icon():
        print("Starting tray icon in thread")
        icon.run()

    tray_thread = threading.Thread(target=_run_icon, daemon=True)
    print("Starting tray thread")
    tray_thread.start()
    print("Tray thread started")

    return icon, tray_thread


if __name__ == "__main__":
    print("Main program started")
    stop_event = threading.Event()
    print("Creating tray icon")
    icon, _ = run_tray_in_thread(stop_event)

    try:
        print("Entering main loop")
        while not stop_event.wait(0.1):
            pass

    except KeyboardInterrupt:
        print("Application terminated by user")
        stop_event.set()

    finally:
        if icon:
            print("Stopping tray icon")
            icon.stop()

        print("Application exiting")
        sys.exit(0)
