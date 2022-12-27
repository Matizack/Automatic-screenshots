# Automatic-screenshots
Aquí hay un ejemplo de código en Python que puede utilizarse para tomar capturas de pantalla en Windows:
Este código utiliza la biblioteca win32gui para obtener una handle de la ventana principal del escritorio
y para obtener el ancho y alto de la pantalla en pixels. Luego utiliza la biblioteca win32ui para crear 
un contexto de dispositivo y un contexto de memoria y un objeto de bitmap en memoria. Utiliza el método
BitBlt del contexto de dispositivo para copiar la pantalla en el objeto de bitmap en memoria y luego
utiliza el método SaveBitmapFile del objeto de bitmap para guardar la captura de pantalla
