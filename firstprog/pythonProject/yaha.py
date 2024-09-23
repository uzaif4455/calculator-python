def welcome():
    print("hello you are welcome")
print(__name__)   #aur ye bata ta hai ki  agar output mai ye ata hai (__main__) toh ye hi origin file hai

if __name__=="__main__":     #jab hum ye likhte hai kisi bhi program me toh dusre program me jab ye file import karenge to is k waja se do output nahi ayenge
    welcome()