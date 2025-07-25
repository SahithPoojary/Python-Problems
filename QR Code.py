# import qrcode
# a=qrcode.QRCode()
# text_mg="HELLO GUYSSSS"
# a.add_data(text_mg)
# a.make(fit=True)
# sahi=a.make_image(fill_color="red", back_color="white")
# sahi.save("sahi.png")
# print("Saved successfully")

# # ///// Linking QR Code with a text File///////////
# import qrcode
# def get_info():
#     file=open("QR.txt","r")
#     x=file.read()
#     return x
#
# a=qrcode.QRCode()
# text_mg=get_info()
# a.add_data(text_mg)
# a.make(fit=True)
# sahi=a.make_image(fill_color="red", back_color="white")
# sahi.save("sahi.png")
# print("Saved successfully")


# ///////Github to QR code////////////
# import qrcode
# github_link = "https://github.com/SahithPoojary?tab=repositories"
#
# a=qrcode.QRCode()
# a.add_data(github_link)
# a.make(fit=True)
# sahi=a.make_image(fill_color="white", back_color="black")
# sahi.save("SahithGithub.png")
# print("Saved successfully")

#

# import qrcode
# upi_id = "sahithpoojary1234@oksbi"  # replace with your actual UPI ID
# name = "Sahith Poojary"
# amount = "100"  # optional, you can leave blank
# upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"
# qr=qrcode.make(upi_link)
# qr.save("upi_payment.png")
# print("Saved successfully")

def nitte(n):
    c=0
    if(n<=1):
        return
    for i in range(n):
        nitte(i)
        print("hai")
        c=c+2
    print(c)
b=nitte(3)
print(b)