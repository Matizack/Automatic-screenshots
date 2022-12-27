import win32gui
import win32ui
import win32con
import win32api

def screenshot():
  # Obtiene una handle de la ventana principal del escritorio
  hdesktop = win32gui.GetDesktopWindow()
  # Obtiene el ancho y alto de la pantalla en pixels
  width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
  height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
  # Crea un contexto de dispositivo para la ventana del escritorio
  desktop_dc = win32gui.GetWindowDC(hdesktop)
  img_dc = win32ui.CreateDCFromHandle(desktop_dc)
  # Crea un contexto de memoria para la captura de pantalla
  mem_dc = img_dc.CreateCompatibleDC()
  # Crea un objeto de bitmap en memoria
  screenshot = win32ui.CreateBitmap()
  screenshot.CreateCompatibleBitmap(img_dc, width, height)
  mem_dc.SelectObject(screenshot)
  # Copia la pantalla en el objeto de bitmap en memoria
  mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)
  # Guarda la captura de pantalla en un archivo
  screenshot.SaveBitmapFile(mem_dc, "screenshot.bmp")
  # Limpia los objetos y contextos de memoria
  mem_dc.DeleteDC()
  win32gui.DeleteObject(screenshot.GetHandle())

# Toma una captura de pantalla
screenshot()
