import cv2

#Use 0 para webcam
#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture(0)

if(vid.isOpened() == False):
    print("Não foi possível ler o feed")

height  = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)
 
out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
      
    # Capture o quadro do vídeo
    # a cada quadro
    #ret - boleano
    #frame - quadro do video

    ret, frame = vid.read()

    # Enquanto o valor de ret for True, ele
    # continua lendo o próximo quadro. Se o valor for False, isso significa
    # que todos os frames do vídeo foram lidos.

    cv2.imshow("Web cam", frame)
    
    out.write(frame)

    if cv2.waitKey(25) == 32:
        break

#Liberar o objeto da captura do vídeo
vid.release()

out.release()

#Fechar todas as janelas
cv2.destroyAllWindows()import cv2

#Use 0 para webcam
#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened() == False):
    print("Não foi possível ler o feed")

height  = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)
 
out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
      
    # Capture o quadro do vídeo
    # a cada quadro
    #ret - boleano
    #frame - quadro do video

    ret, frame = vid.read()

    # Enquanto o valor de ret for True, ele
    # continua lendo o próximo quadro. Se o valor for False, isso significa
    # que todos os frames do vídeo foram lidos.

    cv2.imshow("Web cam", frame)
    
    out.write(frame)

    if cv2.waitKey(25) == 32:
        break

#Liberar o objeto da captura do vídeo
vid.release()

out.release()

#Fechar todas as janelas
cv2.destroyAllWindows()