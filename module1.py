import csv
from datetime import datetime

# function calculates statistics on gender and age characteristics


FILE = "BD.csv" # file where the data is located

def getPercentageByGenderAndAge():

#    FILE = "BD.csv" # file where the data is located
    RESULTFILE = "results.csv" # file, where the results of execut the program
    numberOfDepities = -1 # the first line is information
    countOfWomen = 0
    countOfMen = 0

    # age groups for women

    group0_28Women = 0
    group29_44Women = 0
    group45_59Women = 0
    group60Women = 0

    # age groups for men

    group0_28Men = 0
    group29_44Men = 0
    group45_59Men = 0
    group60Men = 0 

    unknownBirthDate = 0 # people with unknown birth date

    youngestAge = 100
    oldestAge = 0


    now = datetime.now()
    year = now.year

    # count people in a cycle

    with open(FILE, 'r', newline="") as file:
        listOfStructureByAverageAge = {}
        structure = ""
        countInStructure = 1
        age = 0
        totalAge = 0
        reader = csv.reader(file)
        unknownBirthDate = -1
        for row in reader:
            numberOfDepities += 1
            
            if(row[6].isdigit()): # if birthday exist

                age = int(year) - int (row[6])

                # Identification of the oldest and the youngest of the deputies

                if(age > oldestAge):
                    oldestAge = age
                    oldestDeputy = str(row[1] + " " + row[2] + " " + row[3] + " / структура: " + row[0])
                else:
                    if(age < youngestAge):
                        youngestAge = age
                        youngestDeputy = str(row[1] + " " + row[2] + " " + row[3] + " / структура:  " + row[0])


                # distribution of women by age group

                if(row[3].endswith("а")):
                    countOfWomen += 1
                
                    if(age < 29 ):
                        group0_28Women += 1
                    elif(age < 45):
                        group29_44Women += 1
                    elif(age < 60):
                        group45_59Women += 1
                    else:
                        group60Women +=1 

                # distribution of men by age group

                else:

                    if(age < 29 ):
                        group0_28Men += 1
                    elif(age < 45):
                        group29_44Men += 1
                    elif(age < 60):
                        group45_59Men += 1
                    else:
                        group60Men +=1 

            else: 
                #men = str(row[1] + " " + row[2] + " " + row[3] + " " + row[8])
                #rint(men)
                unknownBirthDate += 1


            if(row[0] == structure):

                countInStructure += 1
                totalAge += age
              
            else:
             
                averageAge = totalAge/countInStructure
                averageAge = round(averageAge, 1)
                listOfStructureByAverageAge[structure] = averageAge
                totalAge = age
                structure = row [0]
                countInStructure = 1

            #print(structure + " " + str(countInStructure) + " " + str(totalAge) + " " + row[1])

    averageAge = totalAge/countInStructure
    averageAge = round(averageAge, 1)
    listOfStructureByAverageAge[structure] = averageAge


    # percentage ratios of women by age

    percentOfWomen0_28 = round(group0_28Women/numberOfDepities * 100, 1)
    percentOfWomen29_44 = round(group29_44Women/numberOfDepities * 100, 1)
    percentOfWomen45_59 = round(group45_59Women/numberOfDepities * 100, 1)
    percentOfWomen60 = round(group60Women/numberOfDepities * 100, 1)

    # percentage ratios of men by age

    percentOfMen0_28 = round(group0_28Men/numberOfDepities * 100, 1)
    percentOfMen29_44 = round(group29_44Men/numberOfDepities * 100, 1)
    percentOfMen45_59 = round(group45_59Men/numberOfDepities * 100, 1)
    percentOfMen60 = round(group60Men/numberOfDepities * 100, 1)

    # whole statistic by gender characteristics

    countOfMen = numberOfDepities - countOfWomen
    percentOfWomen = round(countOfWomen/numberOfDepities * 100, 1)
    percentOfMen = round(100 - percentOfWomen, 1)

    # dctionary like "structure - average age of employeer"

    listOfStructureByAverageAge.pop('')
    listOfStructureByAverageAge.pop('Structure')

    # forming a document with results
    
    results = [
        ["Количество депутатов", numberOfDepities],
        ["женщин", countOfWomen],
        ["мужчин", countOfMen],
        ["женщин в возрасте до 28 лет", group0_28Women],
        ["женщин в возрасте с 29 до 44 лет", group29_44Women],
        ["женщин в возрасте с 45 до 59 лет", group45_59Women],
        ["женщин старше 60 лет", group60Women],
        ["мужчин в возрасте до 28 лет", group0_28Men],
        ["мужчин в возрасте с 29 до 44 лет", group29_44Men],
        ["мужчин в возрасте с 45 до 59 лет", group45_59Men],
        ["мужчин старше 60 лет", group60Men],
        ["самый старший депутат", oldestDeputy, "возраст", oldestAge],
        ["самый младший депутат", youngestDeputy, "возраст", youngestAge],
    ]

    with open(RESULTFILE, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(results)


    print("количество депутатов: " + str(numberOfDepities))
    print("количество женщин: " + str(countOfWomen))
    print("количество мужчин: " + str(countOfMen))
    print("процент женщин: " + str(percentOfWomen) + "%")
    print("процент мужчин: " + str(percentOfMen) + "%")
#    print("сейчас идёт " + str(year) + " год\n")

    print("\nженщин в возрасте до 28 лет: " + str(group0_28Women) + "\nженщин в возрасте с 29 до 44 лет: " + str(group29_44Women) + "\nженщин в возрасте с 45 до 59 лет: " + 
        str(group45_59Women) + "\nженщин, старше 60 лет: " + str(group60Women))
    print("\nмужчин в возрасте до 28 лет: " + str(group0_28Men) + "\nмужчин в возрасте с 29 до 44 лет: " + str(group29_44Men) + "\nмужчин в возрасте с 45 до 59 лет: " + 
        str(group45_59Men) + "\nмужчин, старше 60 лет: " + str(group60Men))
    print("\nдепутаты с неизвестной датой рождения: " + str(unknownBirthDate))


    print("\nпроцент женщин в возрасте до 28 лет: " + str(percentOfWomen0_28) + "%" + "\nпроцент женщин в возрасте с 29 до 44 лет: " + str(percentOfWomen29_44) + "%" 
        + "\nпроцент женщин в возрасте с 45 до 59 лет: " + str(percentOfWomen45_59) + "%" + "\nпроцент женщин, старше 60 лет: " + str(percentOfWomen60) + "%")
    print("\nпроцент мужчин в возрасте до 28 лет: " + str(percentOfMen0_28) + "%" + "\nпроцент мужчин в возрасте с 29 до 44 лет: " + str(percentOfMen29_44) + "%"
        + "\nпроцент мужчин в возрасте с 45 до 59 лет: " + str(percentOfMen45_59) + "%" + "\nпроцент мужчин, старше 60 лет: " + str(percentOfMen60) + "%")


    print("самый старший депутат: " + oldestDeputy + " / возраст: " + str(oldestAge))
    print("самый младший депутат: " + youngestDeputy + " / возраст: " + str(youngestAge) + "\n")


    print(listOfStructureByAverageAge)

    return numberOfDepities, percentOfWomen, percentOfMen, percentOfMen0_28, percentOfMen29_44, percentOfMen45_59, percentOfMen60,
    percentOfWomen0_28, percentOfWomen29_44, percentOfWomen45_59, percentOfWomen60, youngestDeputy, oldestDeputy, unknownBirthDate, listOfStructureByAverageAge
        
        
#def analizEducation():







getPercentageByGenderAndAge()


    



