#ValueError Exception
try:
    age = int(input("กรอกอายุ: "))
    print(f"ปีหน้าคุณอายุ {age + 1} ปี")
except ValueError:
    print("กรุณากรอกเป็นอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")

#ZeroDivisionExcepion
try:
    numerator = float(input("กรอกตัวตั้ง : "))
    demominator = float(input("กรอกตัวหาร :"))

    result = numerator /denominator
    print(f"ผลลัพธ์ = {result}")

except ValueError:
    print(f"กรุณากรอกตัวเลยให้ถูกต้อง")

except ZeroDivisionError:
    print(f"ไม่สามารถหารด้วยศูนย์ได้")

