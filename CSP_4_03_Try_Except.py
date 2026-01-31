#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp

def sum(arr : list) -> int:
    sum = 0
    for i in arr:
        try:
            sum += i
        except TypeError:
            pass
    return sum

def cleanData(rawData : list) ->list:
    newList = []
    for i in rawData:
        try:
            newList.append(float(i))
        except (TypeError,ValueError):
            pass
    return newList

def unreliableCalculator(divisors : list) -> list:
    end = []
    for i in divisors:
        try:
            end.append(100/i)
        except TypeError:
            end.append("TypeError")
        except ZeroDivisionError:
            end.append("ZeroDivisionError")
    return end

def upperAll(arr : list) -> None:
    for i in range(len(arr)):
        try:
            arr[i] = arr[i].upper()
        except AttributeError:
            pass

    x = "hello"
    print(x)
    x = x.upper()
    print(x)


def firstItems(arr : list) -> list:
    end = []
    for i in arr:
        try:
            end.append(i[0])
        except TypeError:
            end.append(i)
    return end
