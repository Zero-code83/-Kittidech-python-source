print("2. Time Converter:")
#print("   - Ask user for seconds")
#print("   - Convert to hours, minutes, and remaining seconds")
#print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
#print()

#input
sec = int(input("Enter Seconds : "))

#process
hour = sec // 3600
sec_remin = sec % 3600
mins = sec_remin // 60
sec_remin = sec_remin % 60


#output
print(sec,"seconds =",hour,"hour,",mins,"minute,",sec_remin,"second")
print(f"{sec} seconds = {hour} hour, {mins} minute, {sec_remin} second")