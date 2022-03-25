import cv2


# Crie nosso classificador de corpos


# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    
    # Passe o quadro para nosso classificador de corpos
    
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
