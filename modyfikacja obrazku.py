import cv2
import numpy as np

# Wczytaj obrazek
image = cv2.imread(r'D:\Miecho\SDAcademy\Projekt\przyklad\01-0674F0CB68548DFC90257507B3323139.jpg')

# Konwertuj obrazek do przestrzeni kolorów HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definiuj zakres koloru szarego w przestrzeni HSV
lower_gray = np.array([0, 0, 100], dtype=np.uint8)
upper_gray = np.array([179, 50, 150], dtype=np.uint8)

# Utwórz maskę dla koloru szarego
mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)

# Odwróć maskę
mask_gray = cv2.bitwise_not(mask_gray)

# Konwertuj obrazek do skali szarości
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Nałóż maskę na obrazek w skali szarości
gray_masked = cv2.bitwise_and(gray, gray, mask=mask_gray)

# Konwertuj obrazek z powrotem do formatu BGR
result = cv2.cvtColor(gray_masked, cv2.COLOR_GRAY2BGR)

# Wyświetl obrazek wynikowy
cv2.imshow('Modified Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()