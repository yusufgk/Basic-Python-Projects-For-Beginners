import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.geometry("300x300")
root.title("Sıcak Soğuk")
root.configure(bg="#156ba4")


pcsecim = random.randint(1,100)

tahminEntry = tk.Entry()
tahminEntry.pack()

def tahminet():
    
    tahmin = int(tahminEntry.get())
    
    global pcsecim
    
    if tahmin < 1 or tahmin > 100:
        messagebox.showerror(message="Lütfen 1 ila 100 arasında bir sayı giriniz")
    
    if pcsecim > tahmin :
        if 0 < tahmin - pcsecim <= 10:
            sonucLabel.config(text="Çok Sıcak")
        elif 10 <= pcsecim - tahmin <= 20:
            sonucLabel.config(text="Sıcak")
        elif  20 <= pcsecim - tahmin <= 50:
            sonucLabel.config(text="Soğuk")
        elif 50 <= pcsecim - tahmin <= 100: 
            sonucLabel.config(text="Çok Çok soğuk") 
     
     
    if tahmin > pcsecim :
        if 0 < tahmin - pcsecim <= 10:
            sonucLabel.config(text="Çok Sıcak")
        elif  10 < tahmin - pcsecim <= 20:
            sonucLabel.config(text="Sıcak")
        elif  20 <= tahmin - pcsecim <= 50:
            sonucLabel.config(text="Soğuk")
        elif 50 <= tahmin - pcsecim <= 100: 
            sonucLabel.config(text="Çok Çok soğuk")   
    
    
    if tahmin == pcsecim:
        messagebox.showinfo(message="DOĞRU TAHMİNNN :D")    
        
        
    tahminEntry.delete(0,tk.END)        
            
            
tahminButton = tk.Button(text="Tahmin Et",command=tahminet)  
tahminButton.pack()

sonucLabel = tk.Label(text="",bg="#156ba4")
sonucLabel.pack()



root.mainloop()


