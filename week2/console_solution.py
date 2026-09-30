# Lab 1 solution: IBM 1401 operator console

choice = ""
while choice != "0":
	print()
	print("IBM 1401 OPERATOR CONSOLE")
	print("=========================")
	print("1. Card reader check")
	print("2. Payroll batch run")
	print("3. Job time estimate")
	print("4. Core memory calculator")
	print("5. Two-digit date check")
	print("6. GCD (converted from FORTRAN)")
	print("7. Interest table (converted from FORTRAN)")
	print("8. Luhn check digit")
	print("0. Power down")
	print()
	choice = input("Select: ")

	if choice == "1":
		record = input("Record: ")
		length = len(record)
		if length == 80:
			print(f"Length: {length} -> OK")
		elif length < 80:
			print(f"Length: {length} -> SHORT, padded to 80")
		else:
			print(f"Length: {length} -> OVERFLOW, lost: '{record[80:]}'")
		digits = 0
		letters = 0
		spaces = 0
		for ch in record:
			if ch.isdigit():
				digits += 1
			elif ch.isalpha():
				letters += 1
			elif ch == " ":
				spaces += 1
		print(f"Digits: {digits}  Letters: {letters}  Spaces: {spaces}")

	elif choice == "2":
		count = int(input("How many employees? "))
		total_hours = 0.0
		total_pay = 0.0
		print()
		print("PAYROLL RUN          23/09/1961")
		print(f"{'NAME':<12}{'HOURS':>7}{'RATE':>10}{'PAY':>10}")
		for i in range(count):
			name = input("Name: ")
			hours = float(input("Hours: "))
			rate = float(input("Rate: "))
			if hours > 40:
				pay = 40 * rate + (hours - 40) * rate * 1.5
			else:
				pay = hours * rate
			total_hours += hours
			total_pay += pay
			print(f"{name:<12}{hours:>7.1f}{rate:>10.2f}{pay:>10.2f}")
		print("-" * 42)
		print(f"{'TOTAL':<12}{total_hours:>7.1f}{'':>10}{total_pay:>10.2f}")

	elif choice == "3":
		cards = int(input("Cards: "))
		lines = int(input("Lines: "))
		start_h = int(input("Start hour (0-23): "))
		start_m = int(input("Start minute: "))
		read_min = cards / 800
		print_min = lines / 600
		total_sec = round((read_min + print_min) * 60)
		h = total_sec // 3600
		m = (total_sec % 3600) // 60
		s = total_sec % 60
		print(f"Reading: {read_min:.1f} min, Printing: {print_min:.1f} min")
		print(f"Total: {h}:{m:02}:{s:02}")
		finish = (start_h * 3600 + start_m * 60 + total_sec) % (24 * 3600)
		fh = finish // 3600
		fm = (finish % 3600) // 60
		# seconds from the start time until the next 08:00
		until_morning = (8 * 3600 - (start_h * 3600 + start_m * 60)) % (24 * 3600)
		if total_sec <= until_morning:
			print(f"Finishes at {fh:02}:{fm:02} -> OK")
		else:
			print(f"Finishes at {fh:02}:{fm:02} -> LATE. Morning shift will not be happy.")

	elif choice == "4":
		memory = int(input("Memory (characters): "))
		records = int(input("Records: "))
		size = int(input("Characters per record: "))
		per_pass = memory // size
		passes = (records + per_pass - 1) // per_pass
		machines = 8_000_000_000 // memory
		print(f"Records per pass: {per_pass}")
		print(f"Passes needed: {passes}")
		print(f"An 8 GB laptop has the memory of {machines:,} of these machines.")

	elif choice == "5":
		dd = int(input("Day: "))
		mm = int(input("Month: "))
		yy = int(input("Year (2 digits): "))
		if yy <= 30:
			year = 2000 + yy
		else:
			year = 1900 + yy
		leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
		if mm == 2:
			days = 29 if leap else 28
		elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
			days = 30
		else:
			days = 31
		if mm < 1 or mm > 12:
			print("INVALID month")
		elif dd < 1 or dd > days:
			print(f"INVALID day for {mm:02}/{year}")
		else:
			note = " (leap year)" if leap else ""
			print(f"{dd:02}/{mm:02}/{year} -> VALID{note}")

	elif choice == "6":
		m = int(input("M: "))
		n = int(input("N: "))
		k = m % n            # K = M - (M/N)*N is just the remainder
		while k != 0:        # IF (K) 20, 30, 20: keep going unless zero
			m = n
			n = k
			k = m % n
		print(f"GCD IS {n}")

	elif choice == "7":
		p = float(input("Principal: "))
		r = float(input("Rate (%): "))
		nyrs = int(input("Years: "))
		print("YEAR   BALANCE   INTEREST")
		total = 0.0
		for i in range(1, nyrs + 1):
			amt = p * r / 100.0
			total += amt
			p += amt
			print(f"{i:4}{p:10.2f}{amt:10.2f}")
		print(f"TOTAL INTEREST{total:10.2f}")

	elif choice == "8":
		n = int(input("Number: "))
		original = n
		total = 0
		double = False
		while n > 0:
			d = n % 10
			if double:
				d *= 2
				if d >= 10:
					d -= 9
			total += d
			double = not double
			n //= 10
		if total % 10 == 0:
			print(f"{original} -> VALID")
		else:
			print(f"{original} -> INVALID")

	elif choice == "0":
		print("Powering down. Goodnight.")

	else:
		print("Invalid option")
