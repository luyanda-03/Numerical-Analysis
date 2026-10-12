from numerical import Error, Differentiation


def main():

    actual = 10
    approx = 10.9999

    x = (1, 1.01, 1.02, 1.03, 1.04)
    y = (1.27, 1.32, 1.38, 1.41, 1.47)

    print(Error.error(actual, approx))
    print(Error.abs_error(actual, approx))
    print(Error.relative_error(actual, approx))
    print(Error.percentage_error(actual, approx))
    print(Differentiation.first_diff_forward(x,y,1.02))
    print(Differentiation.first_diff_backward(x,y,1.04))
    print(Differentiation.central_diff(x,y,1.04))




if __name__ == "__main__":
    main()
 



    