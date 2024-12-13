#used array to store temperature of last 7 days in ℃

temperature = [35,34,32,33,35,33,30]

def main():
    print("Average temprature")
    print("------------------")
    temp = sum(temperature) / len(temperature)
    print("The average temperatue is {} ℃".format(round(temp,2)))

if __name__ == "__main__":
    main()