try:
    num1 = float(input("ตัวเลขที่ 1 :"))
    num2 = float(input("ตัวเลขที่ 2 :"))
    op = input("เครื่องหมาย (+,-,*,/) :")

    if op not in ['+','-','*','/']:
        raise ValueError("เครื่องหมายต้องเป็น +,-,*,/ เท่านั้น")
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง : {error}")
except ZeroDivisionError:
    text = "ผิดพลาดไม่สามารถหารด้วยศูนย์ได้"
    print(text.upper())
else:
    print(f"ผลลัพธ์: {result}")
finally:
    print(f"จบการทำงาน")