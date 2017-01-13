'''Created by kayode.oguntimehin on 11/01/2017.'''


class NumberToWord:
    def __init__(self):
        self.result = ""

    def ConvertToWord(self, input_value):
        inputlength = len(input_value)
        response = ""

        if inputlength > 3:
            response = self.thousandandabovevalue(input_value)
        elif inputlength > 0 and inputlength <= 3:

            if inputlength == 1:
                response = NumberToWord.UnitValue(input_value)
            if inputlength == 2:
                response = NumberToWord.tensvalue(input_value)
            if inputlength == 3:
                response = NumberToWord.hundredsvalue(input_value)

        return response

    @staticmethod
    def UnitValue(input_value):
        unitwordmap = {}
        unitwords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        unitwordlength = len(unitwords)
        for i in range(0, unitwordlength):
            unitwordmap[i + 1] = unitwords[i]

        return unitwordmap[int(input_value)]

    @staticmethod
    def tensvalue(input_value):
        tens10_19wordmap = {}
        tenswordmap = {}
        tens10_19 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        tens10_19words = ["ten", "eleven", "twelve",
                          "thirteen", "fourteen", "fifteen",
                          "sixteen", "seventeen", "eighteen",
                          "nineteen"]
        tens10_19wordlength = len(tens10_19words)
        for i in range(0, tens10_19wordlength):
            tens10_19wordmap[i + 10] = tens10_19words[i]

        tensnumbers = [20, 30, 40, 50, 60, 70, 80, 90]
        tenswords = ["twenty", "thirty",
                     "forty", "fifty", "sixty",
                     "seventy", "eighty", "ninety"]
        for i in range(0, len(tensnumbers)):
            tenswordmap[tensnumbers[i]] = tenswords[i]

        if int(input_value) in tens10_19:
            return tens10_19wordmap.get(int(input_value))
        else:
            firstelement = str(input_value)[0]
            secondelement = str(input_value)[1]
            tensinword = ""

            arval = [2, 3, 4, 5, 6, 7, 8, 9]
            if int(firstelement) in arval:

                checktensval = int(firstelement) * 10
                tensinword += tenswordmap.get(checktensval)
                return tensinword + " " + NumberToWord.UnitValue(secondelement)
            else:
                return "Invalid Number"

    @staticmethod
    def hundredsvalue(input_value):
        arrVal = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        firstchar = int(input_value[0])
        lasttwochar = input_value[1:]
        lasttwocharformatted = int(lasttwochar)
        firsthundred = NumberToWord.UnitValue(firstchar)
        hundred = "hundred"
        if int(input_value) in arrVal:
            return firsthundred + " " + hundred
        else:
            if len(str(lasttwocharformatted)) > 1:
                return firsthundred + " " + hundred + " and " + NumberToWord.tensvalue(lasttwocharformatted)
            else:
                return firsthundred + " " + hundred + " and " + NumberToWord.UnitValue(lasttwocharformatted)

    @staticmethod
    def thousandandabovevalue(input_value):
        inputLength = len(str(input_value))
        thousand = "thousand"
        million = "million"
        billion = "billion"
        trillion = "trillion"
        zillion = "zillion"

        if inputLength == 4 or inputLength == 5 or inputLength == 6:
            return NumberToWord.manipulategreaterthanthousand(input_value, inputLength - 3, inputLength - 3, inputLength, thousand)
        elif inputLength == 7 or inputLength == 8 or inputLength == 9:
            return NumberToWord.manipulategreaterthanthousand(input_value,inputLength - 6, inputLength - 6, inputLength, million)
    @staticmethod
    def manipulategreaterthanthousand(input_value, secondindex, indexfrom, indexto, unittype):
        numberToWord = ""
        firstValue = input_value[0: secondindex]
        kval = firstValue
        firstValInWord = ""
        othernumbersVal = ""

        if len(str(firstValue)) == 1:
            firstValInWord = NumberToWord.UnitValue(firstValue)

        elif len(str(firstValue)) == 2:
            firstValInWord = NumberToWord.tensvalue(firstValue)

        elif len(str(firstValue)) == 3:
            firstValInWord = NumberToWord.hundredsvalue(str(firstValue))

        else:
            return "Invalid Number"

        firstnumber = firstValInWord + " " + unittype + ", "
        numberToWord += firstnumber

        if unittype == "thousand":
            othernumbersVal = str(input_value)[indexfrom: indexto]
            if int(str(othernumbersVal[0])) > 0:
                numberToWord += NumberToWord.hundredsvalue(othernumbersVal)
            elif int(str(othernumbersVal[0: 1]) == 0 and int(str(othernumbersVal[1: 2])) > 0):
                numberToWord += "and " + NumberToWord.tensvalue(othernumbersVal)
            elif int(str(othernumbersVal[0: 1])) == 0 and int(str(othernumbersVal[1: 2]) > 0) and int(
                            str(othernumbersVal[2: 3]) > 0):
                numberToWord += "and " + NumberToWord.UnitValue(othernumbersVal)
            else:
                strval = NumberToWord[0: len(numberToWord) - 2]
                numberToWord = ""
                numberToWord += strval

        elif unittype == "million":
            othernumbersVal = str(input_value)[indexfrom: indexto]
            if int(str(othernumbersVal[0])) > 0:
                numberToWord += NumberToWord.thousandandabovevalue(int(othernumbersVal))
            elif int(str(othernumbersVal[0: 1]) == 0 and int(othernumbersVal) != 0):
                newOtherNumbersVal = int(othernumbersVal)
                newOtherNumbersLenght = len(str(newOtherNumbersVal))
                appendVal = ""
                if newOtherNumbersLenght == 5 or newOtherNumbersLenght == 4:
                    numberToWord += NumberToWord.thousandandabovevalue(newOtherNumbersVal)
                elif newOtherNumbersLenght == 3:
                    numberToWord += NumberToWord.hundredsvalue(str(newOtherNumbersVal))
                elif newOtherNumbersLenght == 2:
                    appendVal = "and" + NumberToWord.tensvalue(newOtherNumbersVal)
                    numberToWord += appendVal
                elif newOtherNumbersLenght == 1:
                    appendVal = "and" + NumberToWord.UnitValue(newOtherNumbersVal)
                    numberToWord += appendVal
                numberToWord += "and " + NumberToWord.tensvalue(othernumbersVal)

            else:
                strval = NumberToWord[0: len(numberToWord) - 2]
                numberToWord = ""
                numberToWord += strval

        return numberToWord.replace(", and", " and ")
