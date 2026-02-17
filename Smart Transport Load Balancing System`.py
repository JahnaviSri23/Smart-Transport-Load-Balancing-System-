name = input("Enter full name: ")
L = 0
for ch in name:
    if ch != " ":
        L = L + 1

PLI = L % 3
n = int(input("Enter number of packages: "))
weights = []
for i in range(n):
    w = int(input("Enter weight: "))
    weights.append(w)

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

for w in weights:
    if w < 0:
        invalid_entries.append(w)
    elif w <= 5:
        very_light.append(w)
    elif w <= 25:
        normal_load.append(w)
    elif w <= 60:
        heavy_load.append(w)
    else:
        overload.append(w)

valid_before = 0
for w in weights:
    if w >= 0:
        valid_before = valid_before + 1

affected = 0

if PLI == 0:
    rule = "Rule A (Overload → Invalid)"
    for x in overload:
        invalid_entries.append(x)
        affected = affected + 1
    overload = []

elif PLI == 1:
    rule = "Rule B (Remove Very Light)"
    for x in very_light:
        affected = affected + 1
    very_light = []

else:
    rule = "Rule C (Keep only Normal & Heavy)"
    for x in very_light:
        invalid_entries.append(x)
        affected = affected + 1
    for x in overload:
        invalid_entries.append(x)
        affected = affected + 1
    very_light = []
    overload = []

final_valid = 0
for x in very_light:
    final_valid = final_valid + 1
for x in normal_load:
    final_valid = final_valid + 1
for x in heavy_load:
    final_valid = final_valid + 1
for x in overload:
    final_valid = final_valid + 1

print("\n------ SMART LOADING REPORT ------")
print("Name Length (L):", L)
print("PLI Value:", PLI)
print("Applied:", rule)
print("\nValid Weights Before PLI:", valid_before)
print("Final Valid Weights:", final_valid)
print("Affected Items:", affected)
print("\nFinal Loading Plan")
print("Very Light :", very_light)
print("Normal Load:", normal_load)
print("Heavy Load :", heavy_load)
print("Overload   :", overload)
print("Invalid    :", invalid_entries)
