#12 month in a year
month = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
#Display month
month_number = int(input("Input the number of the month: "))
if month_number in month:
    print("Month: ", month[month_number])
else:
    print("Invalid month number, please input the number beetween 1-12")