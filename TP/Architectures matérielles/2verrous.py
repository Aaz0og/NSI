from threading import Thread, Lock
R1_moteurs = Lock()
R2_Wifi = Lock()
R3_Camera = Lock()

def P1_pilotage_manuel():
    R1_moteurs.acquire()
    print("R1 acquis par le programme P1")
    R2_Wifi.acquire()
    print("R2 acquis par le programme P1")
    R2_Wifi.release()
    R1_moteurs.release()

def P2_envoi_flux_video():
    R2_Wifi.acquire()
    print("R3 acquis par le programme P2")
    R3_Camera.acquire()
    print("R3 acquis par le programme P2")
    R3_Camera.release()
    R2_Wifi.release()

def P3_auto_tests_materiel():
    R3_Camera.acquire()
    print("R3 acquis par le programme P3")
    R1_moteurs.acquire()
    print("R1 acquis par le programme P3")
    R1_moteurs.release()
    R3_Camera.release()
    


while True:
    p1 = Thread(target = P1_pilotage_manuel)
    p2 = Thread(target = P2_envoi_flux_video)
    p3 = Thread(target= P3_auto_tests_materiel)
    p1.start() # Lance calcul dans un processus léger à part.
    p2.start() # Lance calcul dans un processus léger à part.
    p3.start()
    p1.join()
    p2.join()
    p3.join()