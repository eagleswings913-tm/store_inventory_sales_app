import ctypes
import sys
from PySide6.QtGui import QCursor, QGuiApplication

def set_title_bar_color(self, bgr_color: int):
    if sys.platform == "win32":
        hwnd = int(self.winId())
        # DWMWA_CAPTION_COLOR = 35 (Windows 11 Build 22000+)
        dwmwa_caption_color = 35
        color = ctypes.c_int(bgr_color)
        # type: ignore
        ctypes.windll.dwmapi.DwmSetWindowAttribute(                      # type: ignore[attr-defined]
            hwnd,
            dwmwa_caption_color,
            ctypes.byref(color),
            ctypes.sizeof(color)
        )

def center_on_cursor_screen(self):
    # Find the screen where the mouse cursor is currently located
    cursor_pos = QCursor.pos()
    target_screen = QGuiApplication.screenAt(cursor_pos)

    # Fallback to the primary screen if the cursor position isn't detected
    if target_screen is None:
        target_screen = QGuiApplication.primaryScreen()

    # Calculate and apply the center position
    available_geometry = target_screen.availableGeometry()
    frame_geometry = self.frameGeometry()
    center_point = available_geometry.center()
    frame_geometry.moveCenter(center_point)
    self.move(frame_geometry.topLeft())