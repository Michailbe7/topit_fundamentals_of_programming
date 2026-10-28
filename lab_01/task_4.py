student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

name = student[:4]
surname = student[5:]
print(name[0])
print(name[-1])
print(name)
print(surname)

print(student.upper())
print(student.lower())

initials = name[0] + "." + surname[0] + "."
print(initials)

print(course[::-1])

percent = completed / total * 100
by_percent = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
by_format = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
by_fstring = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"
print(by_percent)
print(by_format)
print(by_fstring)

symbol = "Я"
code_point = ord(symbol)
restored = chr(code_point)
encoded = symbol.encode("utf-8")
print(symbol)
print(code_point)
print(restored)
print(encoded)
print(len(encoded))