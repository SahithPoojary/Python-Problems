import tkinter

blink_colors = ["red", "blue"]
current_blink_index = 0

def blink():
    global current_blink_index
    res.config(fg=blink_colors[current_blink_index])
    current_blink_index = (current_blink_index + 1) % len(blink_colors)
    res.after(500, blink)

def cal_bmi():
    global blink_colors, current_blink_index
    try:
        h = float(ht_value.get())
        w = float(wt_val.get())
        h1 = h / 100
        bmi = w / (h1 ** 2)

        if bmi < 18.5:
            status = "underweight"
            blink_colors = ["orange", "yellow"]
        elif 18.5 <= bmi <= 24.9:
            status = "normal weight"
            blink_colors = ["green", "blue"]
        else:
            status = "obesity"
            blink_colors = ["red", "purple"]

        current_blink_index = 0
        res.config(text=f"BMI IS {bmi:.2f} ({status})", bg="white")
        blink()

    except ValueError:
        res.config(text="Please enter valid numbers!", fg="red", bg="white")

root = tkinter.Tk()
root.geometry("500x500")
root.title("BMI Calculator")
root.config(bg="light blue")

head = tkinter.Label(root, text="BMI CALCULATOR", font=("Arial", 20, "bold"), bg="light blue")
head.pack(pady=20)

fr = tkinter.Frame(root, bg="light blue")
fr.pack(pady=10)

ht = tkinter.Label(fr, text="HEIGHT (in cm)", font=("Arial", 15), bg="white")
ht.grid(row=0, column=0, padx=5, pady=5)
ht_value = tkinter.Entry(fr)
ht_value.grid(row=0, column=1, padx=5, pady=5)

wt = tkinter.Label(fr, text="WEIGHT (in kg)", font=("Arial", 15), bg="white")
wt.grid(row=1, column=0, padx=5, pady=5)
wt_val = tkinter.Entry(fr)
wt_val.grid(row=1, column=1, padx=5, pady=5)

bt = tkinter.Button(root, text="Calculate", font=("Arial", 20, "bold"), fg="blue", bg="red", command=cal_bmi)
bt.pack(pady=20)

res = tkinter.Label(root, text="", font=("Arial", 20, "bold"), bg="white")
res.pack(pady=20)

root.mainloop()
