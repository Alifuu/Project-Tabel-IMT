print ( "Kalkulator BMI")

inputTinggi = float(input("masukkan tinggi badan anda: "))
inputBerat = float(input("masukkan berat badan anda: "))
tinggiMeter = float(inputTinggi / 100)
# print (tinggiMeter)
hasilInput = inputBerat / (tinggiMeter * tinggiMeter)
print (hasilInput) 

data1 = "sangat kurus"
data2 = "kurus"
data3 = "normal"
data4 = "gemuk"
data5 = "sangat gemuk"

if hasilInput < 17 :
    print (data1)
elif hasilInput > 17 and hasilInput < 18.4 :
    print (data2)
elif hasilInput > 18.5 and hasilInput < 25.0: 
    print (data3)
elif hasilInput > 25.00 and hasilInput < 27.0 :
    print (data4)
elif  hasilInput > 27 and hasilInput < 50 :
    print (data5)
else : 
    print("Obesitas")    



