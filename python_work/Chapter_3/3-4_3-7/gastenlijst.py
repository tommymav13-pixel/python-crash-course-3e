## This program prints a welcome message for each guest in the list.  
#   Opdracht 3-4
gastenlijst = ['Alice', 'Bob', 'Charlie', 'David']
print(gastenlijst)
for gast in gastenlijst:
    print("Beste, " + gast + "!\nBij deze ben je uitgenodigd voor een diner op zaterdagavond om 19:00!")

#  Opdracht 3-5
print("Helaas kan Charlie niet komen naar het diner.")
gastenlijst.remove('Charlie')
gastenlijst.append('Eve')
print(gastenlijst)
for gast in gastenlijst:
    print("Beste, " + gast + "!\nBij deze ben je uitgenodigd voor een diner op zaterdagavond om 19:00!")

#  Opdracht 3-6
print("Goed nieuws! Ik heb een grotere tafel gevonden, dus ik kan meer gasten uitnodigen.")
gastenlijst.insert(0, 'Frank')
gastenlijst.insert(3, 'Grace')
gastenlijst.append('Heidi')
print(gastenlijst)
for gast in gastenlijst:
    print("Beste, " + gast + "!\nBij deze ben je uitgenodigd voor een diner op zaterdagavond om 19:00!")   

#   Opdracht 3-7
print("Ik kan helaas maar 2 personen uitnodigen.")
popgast1 = gastenlijst.pop()
print(f"Excuses, {popgast1}, maar ik kan je helaas niet meer uitnodigen.") 
popgast2 = gastenlijst.pop()
print(f"Excuses, {popgast2}, maar ik kan je helaas niet meer uitnodigen.")
popgast3 = gastenlijst.pop()
print(f"Excuses, {popgast3}, maar ik kan je helaas niet meer uitnodigen.")
popgast4 = gastenlijst.pop()
print(f"Excuses, {popgast4}, maar ik kan je helaas niet meer uitnodigen.")
popgast5 = gastenlijst.pop()
print(f"Excuses, {popgast5}, maar ik kan je helaas niet meer uitnodigen.")

print(gastenlijst)
for gast in gastenlijst:
    print(f"Beste, {gast}, je bent nog steeds uitgenodigd voor het diner.")  

del gastenlijst[0]
del gastenlijst[0]
print(gastenlijst) 

