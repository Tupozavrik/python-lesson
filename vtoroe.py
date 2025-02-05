
with open("111.txt", 'r') as file: 
    filesplit = [line.split() for line in file]


pobediteli_klassa = {}
for surname, name, klass, algebra, geometry in filesplit:
    total_score = int(algebra) + int(geometry)

    if klass not in pobediteli_klassa or total_score > pobediteli_klassa[klass][2]:
        pobediteli_klassa[klass] = (surname, name, total_score)

    elif total_score == pobediteli_klassa[klass][2]:
        pobediteli_klassa[klass] = (pobediteli_klassa[klass], surname, name, total_score)

best_algebra = {}
for surname, name, klass, algebra, geometry in filesplit:
    score = int(algebra)
    if 4 not in best_algebra or score > best_algebra[4][0]:
        best_algebra[4] = (score, [(surname, name, klass)])
    elif score == best_algebra[4][0]:
        best_algebra[4][1].append((surname, name, klass))

best_geometry = {}
for surname, name, klass, algebra, geometry in filesplit:   
    score = int(geometry)
    if 5 not in best_geometry or score > best_geometry[5][0]:
        best_geometry[5] = (score, [(surname, name, klass)])
    elif score == best_geometry[5][0]:
        best_geometry[5][1].append((surname, name, klass))

print("Победители по классам")
for klass, winner in pobediteli_klassa.items():
    print(f"Класс: {klass}")
    if isinstance(winner[0], str):  
        print(f"  Фамилия: {winner[0]}, Имя: {winner[1]}, Результат: {winner[2]}")
    else:  
        for i in range(0, len(winner), 3):
            print(f"  Фамилия: {winner[i]}, Имя: {winner[i+1]}, Результат: {winner[i+2]}")

print("\nЛучшие по алгебре")
for i, winners in best_algebra.values():
    for surname, name, klass in winners:
        print(f"Фамилия: {surname}, Имя: {name}, Класс: {klass}")

print("\nЛучшие по геометрии")
for i, winners in best_geometry.values():   
    for surname, name, klass in winners:
        print(f"Фамилия: {surname}, Имя: {name}, Класс: {klass}")