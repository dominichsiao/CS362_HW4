def fill_list(num1, num2, num3, num4):
    elements = [num1, num2, num3, num4]
    total = 0
    for x in range (4):
        total += elements[x]

    average = total/4

    return(average)

def main():
    fill_list(1,2,3,4)

if __name__ == "__main__":
	main()
