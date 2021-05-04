def fill_list(list):
    #elements = [num1, num2, num3, num4]
    total = 0
    for x in range (len(list)):
        total += list[x]

    average = total/len(list)

    return(average)

def main():
    fill_list(1,2,3,4)

if __name__ == "__main__":
	main()
