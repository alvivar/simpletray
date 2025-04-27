import sys
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from notifypy import Notify


def create_image(width=64, height=64):
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


def notification(title, message):
    print(f"Sending notification: Title='{title}', Message='{message}'")
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.send()


def on_show(icon, item):
    print("Show option selected")
    notification("Show Action", "You selected the 'Show' option.")


def on_settings(icon, item):
    print("Settings option selected")
    notification("Settings Action", "You selected the 'Settings' option.")


def on_quit(icon, item):
    print("Quit option selected")
    icon.stop()


def create_menu():
    print("Creating menu items")
    return (
        item("Show", on_show),
        item("Settings", on_settings),
        item("Quit", on_quit),
    )


def setup(icon):
    print("Icon setup complete.")
    icon.visible = True


if __name__ == "__main__":
    print("Main program started")
    image = create_image()
    menu = create_menu()

    icon = pystray.Icon(
        name="tray_demo",
        title="Tray Demo",
        icon=image,
        menu=pystray.Menu(*menu),
    )

    print("Starting tray icon...")
    icon.run(setup=setup)

    print("Application exiting")
    sys.exit(0)
