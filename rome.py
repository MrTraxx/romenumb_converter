print("Number has to be between 1 and 3999. For exit press ctl+c\n")

while True:
    try:
        decimal = int(input("Please enter a decimal number: "))
        if decimal < 1 or decimal > 3999:
            print("Number has to be between 1 and 3999")
            continue

        else:
            romenumb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
            dezinumb = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            roman = ""
            for dezi in range(len(dezinumb)):
                while decimal >= dezinumb[dezi]:
                    decimal -= dezinumb[dezi]
                    roman += romenumb[dezi]
            print("Roman numeral:", roman)
            continue
    except:
        break
