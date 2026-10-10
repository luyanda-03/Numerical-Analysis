from numerical import Error


def main():

    actual = 10
    approx = 10.9999

    print(Error.error(actual, approx))
    print(Error.abs_error(actual, approx))
    print(Error.relative_error(actual, approx))
    print(Error.percentage_error(actual, approx))

if __name__ == "__main__":
    main()
 



    