#Temp classifier
def classify_temperature(temp):
    if temp <= 0:
        return("Freezing")
    elif 0 <= temp <= 10:
        return("Very Cold")
    elif 10 <= temp <= 20:
        return("Cold")
    elif 20 <= temp <= 30:
        return("Moderate")
    elif 30 <= temp <= 40:
        return("Hot")
    else:
        return("Very Hot")
#Example
temperature = float(input("Enter the temperature: "))
classification = classify_temperature(temperature)
print("Temperature classification:", classification)