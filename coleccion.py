import os

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
# Número de clases para el abecedario completo
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
number_of_classes = len(alphabet)
dataset_size = 100
# Captura de video
cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    letter = alphabet[j]
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('recoger data para posicion {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Presiona la letra Q para capturar la letra {letter}', (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
