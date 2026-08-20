import cv2

# Cargar la imagen
imagen = cv2.imread("R.jpg")

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar los bordes
bordes = cv2.Canny(gris, 100, 200)

# Guardar el resultado
cv2.imwrite("bordes.jpg", bordes)

print("Los bordes de la imagen fueron obtenidos correctamente.")
print("Resultado guardado como: bordes.jpg")



import cv2  # Importa la librería OpenCV para trabajar con imágenes

# Cargar la imagen
imagen = cv2.imread("R.jpg")  # Carga la imagen R.jpg y la guarda en la variable imagen

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convierte la imagen de color a escala de grises

# Detectar los bordes
bordes = cv2.Canny(gris, 100, 200)  # Detecta los bordes de la imagen usando los valores 100 y 200

# Guardar el resultado
cv2.imwrite("bordes.jpg", bordes)  # Guarda la imagen con los bordes en un archivo llamado bordes.jpg

print("Los bordes de la imagen fueron obtenidos correctamente.")  # Muestra un mensaje indicando que el proceso terminó correctamente
print("Resultado guardado como: bordes.jpg")  # Muestra el nombre del archivo donde se guardó el resultado