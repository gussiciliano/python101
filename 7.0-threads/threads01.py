import threading, time

def mi_thread(miNumero):
    while True:
        print("thread numero", num)
        time.sleep(miNumero)


if __name__ == "__main__":
    for num in range(1, 10):
        elThread = threading.Thread(target=mi_thread, args=(num,), daemon=True) # que pasa si saco la coma?x
        elThread.start()
    while True:
        pass
