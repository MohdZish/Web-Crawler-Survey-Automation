from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random


emotioncontrol = False
workcontrol = False
othercare = False
openness = False
adapt = False
askhelp = False
tookaction = False
techperson = False
extrawork = False
goodinfluence = False

emotionask = input("emotion control? ")
workcontrolask = input("work control? ")
othercareask = input("other people care? ")
opennessask = input("open with other? ")
adaptask = input("adapt to situaton? ")
askhelpask = input("Asked for help? ")
tookactionask = input("Took necessary actions? ")
techpersonask = input("Tech Person? ")
extraworkask = input("Work extra? ")
goodinfluenceask = input("Good Influence? ")

if emotionask == "y":
    emotioncontrol = True

if workcontrolask == "y":
    workcontrol = True

if othercareask == "y":
    othercare = True

if opennessask == "y":
    openness = True

if adaptask == "y":
    adapt = True

if askhelpask == "y":
    askhelp = True

if tookactionask == "y":
    tookaction = True

if techpersonask == "y":
    techperson = True

if extraworkask == "y":
    extrawork = True

if goodinfluenceask == "y":
    goodinfluence = True


driver = webdriver.Chrome(executable_path=r'D:\Zishan\Temp\chromedriver')
driver.get("https://dauphinem1.eu.qualtrics.com/jfe/form/SV_8djB8ud9xA5gmvb")
first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "QR~QID23")))


if emotioncontrol == True:

    for x in range(1, 4):
        first = driver.find_element_by_id("QID28~" + str(x) + "~true-result")
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", first, random.randint(5, 10));
    for x in range(4, 6):
        second = driver.find_element_by_id("QID28~" + str(x) + "~true-result")
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", second, random.randint(1, 5));
else:
    for x in range(1, 4):
        first = driver.find_element_by_id("QID28~" + str(x) + "~true-result")
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", first, random.randint(1, 5));
    for x in range(4, 6):
        second = driver.find_element_by_id("QID28~" + str(x) + "~true-result")
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", second, random.randint(1, 7));

#For RadioButtons --------------------
def check(variabletocheck):
    if variabletocheck == True:
        e1 = str(random.randint(3, 5))
        e2 = str(random.randint(1, 3))

    else:
        e1 = str(random.randint(1, 3))
        e2 = str(random.randint(3, 5))
    return e1, e2

def e1(variabletocheck):
    result = check(variabletocheck)
    e1fin = result[0]
    return e1fin

def e2(variabletocheck):
    result = check(variabletocheck)
    e1fin2 = result[1]
    return e1fin2


#part 2 work control -----------------
radiobtn = driver.find_element_by_id("QR~QID24~1~" + e2(workcontrol))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID24~2~" + e1(workcontrol))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID24~3~" + e1(workcontrol))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID24~4~" + e2(workcontrol))
driver.execute_script("arguments[0].checked = true;", radiobtn)


#part 3 othercare ------------------------
radiobtn = driver.find_element_by_id("QR~QID3~1~" + e2(othercare))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID3~2~" + e1(othercare))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID3~3~" + e1(othercare))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID3~4~" + e2(othercare))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID3~5~" + e1(othercare))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID3~6~" + e2(othercare))
driver.execute_script("arguments[0].checked = true;", radiobtn)



#For Sliders check2
def check2(variabletocheck2):
    if variabletocheck2 == True:
        e1slider = random.randint(6, 10)
        e2slider = random.randint(1, 6)

    else:
        e1slider = random.randint(1, 6)
        e2slider = random.randint(5, 10)
    return e1slider, e2slider

def e1slider(variabletocheck2):
    result = check(variabletocheck2)
    e1fin2 = result[0]
    return e1fin2

def e2slider(variabletocheck2):
    result = check(variabletocheck2)
    e1fin2 = result[1]
    return e1fin2


#part 4 openness
slider = driver.find_element_by_id("QID29~1~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, random.randint(0, 5))

slider = driver.find_element_by_id("QID29~2~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, random.randint(1, 6))

slider = driver.find_element_by_id("QID29~3~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, random.randint(3, 11))

slider = driver.find_element_by_id("QID29~4~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, random.randint(3, 11))

#part 5 adaptabilty
def checking(variable):
    if variable == True:
        x = random.randint(5, 11)
    else:
        x = random.randint(3, 6)
    return x

def temp(variable):
    val = checking(variable)
    return val

slider = driver.find_element_by_id("QID5~1~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, temp(adapt))

slider = driver.find_element_by_id("QID5~2~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, temp(adapt))

slider = driver.find_element_by_id("QID5~3~true-result")
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, temp(adapt))

#part 6 virus deniability

radiobtn = driver.find_element_by_id("QR~QID6~1~" + str(random.randint(1, 2)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID6~2~" + str(random.randint(1, 2)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID6~3~" + str(random.randint(1, 2)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID6~4~" + str(random.randint(3, 5)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID6~5~" + str(random.randint(3, 5)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID6~6~" + str(random.randint(3, 5)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 7 asking help and actions ------------------------

radiobtn = driver.find_element_by_id("QR~QID7~1~" + e1(tookaction))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~2~" + e1(tookaction))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~3~" + e1(tookaction))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~4~" + e1(askhelp))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~5~" + e1(askhelp))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~6~" + e1(askhelp))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~7~" + e1(tookaction))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~8~" + e1(tookaction))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID7~9~" + e1(tookaction))
driver.execute_script("arguments[0].checked = true;", radiobtn)


#part 8 technology adaptability -----------------------

radiobtn = driver.find_element_by_id("QR~QID8~1~" + e2(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID8~2~" + e2(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID8~3~" + e2(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID8~4~" + e1(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID8~5~" + e1(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID8~6~" + e1(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 9 Influence -----------------------

radiobtn = driver.find_element_by_id("QR~QID9~1~" + e1(extrawork))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~2~" + e1(extrawork))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~3~" + e1(extrawork))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~4~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~5~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~6~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~7~" + str(random.randint(1, 4)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID9~8~" + str(random.randint(1, 4)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 10 Influence and technology  -----------------------

radiobtn = driver.find_element_by_id("QR~QID10~1~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID10~2~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID10~3~" + str(random.randint(1, 3)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID10~4~" + e2(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID10~5~" + e2(techperson))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 11 relationship  -----------------------

radiobtn = driver.find_element_by_id("QR~QID11~1~" + e1(openness))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID11~2~" + e1(openness))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID11~3~" + e2(openness))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID11~4~" + str(random.randint(1, 3)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID11~5~" + str(random.randint(1, 2)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 12 approach  -----------------------

radiobtn = driver.find_element_by_id("QR~QID12~1~" + e1(askhelp))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID12~2~" + str(random.randint(1, 5)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID12~3~" + e1(adapt))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID12~4~" + e1(adapt))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID12~5~" + e1(adapt))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID12~6~" + str(random.randint(1, 3)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 13 satisfaction  -----------------------

radiobtn = driver.find_element_by_id("QR~QID13~1~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)


#part 14 overall feel  -----------------------

radiobtn = driver.find_element_by_id("QR~QID14~1~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID14~2~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID14~3~" + str(random.randint(2, 4)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID14~4~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

radiobtn = driver.find_element_by_id("QR~QID14~5~" + e1(goodinfluence))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 15 gender -----------------------

radiobtn = driver.find_element_by_id("QR~QID15~" + str(random.randint(1, 2)))
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 16 age -----------------------
age = str(random.randint(1, 2))

radiobtn = driver.find_element_by_id("QR~QID16~" + age)
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 17 study -----------------------
if age == 1:
    study = str(random.randint(2, 3))
else:
    study = str(random.randint(4, 6))

radiobtn = driver.find_element_by_id("QR~QID17~" + study)
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 18 nationality-----------------------
nation = str(random.randint(1, 2))
radiobtn = driver.find_element_by_id("QR~QID18~" + nation)
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 19 tech -----------------------
if techperson == True:
    tech = str(random.randint(3, 5))
else:
    tech = str(random.randint(1, 3))

radiobtn = driver.find_element_by_id("QR~QID19~1~" + tech)
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 20 confinement -----------------------
if nation == 1:
    confinement = str(random.randint(4, 5))
else:
    confinement = str(random.randint(1, 3))

radiobtn = driver.find_element_by_id("QR~QID20~1~" + confinement)
driver.execute_script("arguments[0].checked = true;", radiobtn)

#part 21 work now -----------------------
radiobtn = driver.find_element_by_id("QR~QID21~1~" + str(random.randint(1, 5)))
driver.execute_script("arguments[0].checked = true;", radiobtn)


