f = "Perepis.txt"
count = 0

print("Фамилии жителей до 1978:")

with open(f, "r") as file:
    for line in file:
        parts = line.split(maxsplit=1)
        surname = parts[0]
        part = parts[1].split()
        year = int(part[-1].split('.')[-1])
        if year < 1978:
            print(surname)
            count += 1
print(count)
if count == 0:
    print("тест")

print("укажите диапозон лет: ")
start = int(input())
end = int(input())

with open(f,"r") as file: 
    for line in file: 
        parts = line.split()
        if len(parts) > 3: 
           fio = " ".join(parts[0:len(parts)-1])
           year = int(parts[-1].split('.')[-1]) 
           if start <= year <= end:
               print(f"фио {fio} год {year}")


