def calculate_electricity_cost(units):
    if units > 200:
        cost = (50 * 2.50) + (50 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00) + 25
        print("รายละเอียดค่าไฟ:")
        print(f"1-50 หน่วย : 125.00 บาท")
        print(f"51-100 หน่วย : 150.00 บาท")
        print(f"101-200 หน่วย : 125.00 บาท")
        print(f"201-{units} หน่วย : {((units - 200) * 4.00):.2f} บาท")
        print("ค่าบริการ : 25 บาท")
        print(f"รวมค่าไฟทั้งสิ้น {cost:.2f} บาท\n")
 
    elif units > 100:
        cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50) + 25
        print("รายละเอียดค่าไฟ:")
        print(f"1-50 หน่วย : 125.00 บาท")
        print(f"51-100 หน่วย : 150.00 บาท")
        print(f"101-{units} หน่วย : {((units - 100) * 3.50):.2f} บาท")
        print("ค่าบริการ : 25 บาท")
        print(f"รวมค่าไฟทั้งสิ้น {cost:.2f} บาท\n")
 
    elif units > 50:
        cost = (50 * 2.50) + ((units - 50) * 3.00) + 25
        print("รายละเอียดค่าไฟ:")
        print(f"1-50 หน่วย : 125.00 บาท")
        print(f"51-{units} หน่วย : {((units - 50) * 3.00):.2f} บาท")
        print("ค่าบริการ : 25 บาท")
        print(f"รวมค่าไฟทั้งสิ้น {cost:.2f} บาท\n")
 
    elif units >= 0:
        cost = (units * 2.50) + 25
        print("รายละเอียดค่าไฟ:")
        print(f"1-{units} หน่วย : {((units) * 2.50):.2f} บาท")
        print("ค่าบริการ : 25 บาท")
        print(f"รวมค่าไฟทั้งสิ้น {cost:.2f} บาท\n")
 
    else:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
 
choice = 0
while choice != 2:
    print("==== โปรแกรมคำนวณค่าไฟฟ้า ====")
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")
    choice = int(input("เลือกเมนู: "))
    print()
    if choice == 1:
        units = int(input("กรอกจำนวนหน่วยไฟฟ้า: "))
        print()
        calculate_electricity_cost(units)
    elif choice != 2:
        print("หากเลือกเมนูอื่น ให้แจ้งเมนูไม่ถูกต้อง\n")
        break
    