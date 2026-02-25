import random
import time

min_ertek = 1
max_ertek = 6

max_ertek_valasz = input("Hany oldalu legyen a dobokocka? (alapertelmezett = 6) ")
 
if max_ertek_valasz != "" and max_ertek_valasz.isnumeric ():
    max_ertek = int(max_ertek_valasz)

def dobokocka_eldobasa():
    return random.randint(min_ertek, max_ertek)

def betoltes():
     print("Dobokocka eldobasa:")
     time.sleep(0.5)
    

while True:
        valasz = input("Eldobjuk a dobokockat? [i/n] ")
        
        if valasz == "i":
             betoltes()
             print(dobokocka_eldobasa())
        elif valasz =="n":
            print("Viszlat...")
            break
        else:
             print("Invalid bevitel! [i/n] ")

 
