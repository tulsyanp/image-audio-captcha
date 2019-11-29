# implement evaluation function to check the prediction result and view summary report
# Note
#   1. Do not scramble while generating the captcha images
#   2. place the file in the project folder where train.py is present
#   3. use the command python evaluator.py --captcha-length 5  --predicted-output stuff.txt
# awk -F '[ ,.]' '$1==$4{correct++}END{print "Accuracy: " correct/NR * 100 "%"}' < output.txt

import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--captcha-length', help='Model name to use for classification', type=int)
    parser.add_argument('--predicted-output', help='Model name to use for classification', type=str)
    argument = parser.parse_args()

    if argument.captcha_length is None:
        print("kindly specify the number of characters used to create the captcha")
        exit(1)

    if argument.predicted_output is None:
        print("kindly specify the file that contains predicted results")
        exit(1)

    noPredicted = 0
    success = 0
    failure = 0
    analysis = [0] * (argument.captcha_length - 1)

    with open(argument.predicted_output) as f:
        results = f.readlines()
        results = [x.strip() for x in results]
        noPredicted = len(results)

        for result in results:
            resultArray = result.split('.png, ')
            if (resultArray[0] == resultArray[1]):
                success += 1
            else:
                failure += 1
                rArray = list(resultArray[0])
                preArray = list(resultArray[1])
                count = 0
                for index in range(argument.captcha_length - 1):
                    if (rArray[index] != preArray[index]):
                        count += 1
                analysis[count] += 1

        print("Number of captchas taken for prediction: " + str(noPredicted))
        print("Number succeded in predecting: " + str(success))
        print("Number failed in predecting: " + str(failure))
        accuracy = (success / noPredicted) * 100
        print("Model accuracy is " + str(accuracy) + "%")

        print("Failure analysis")
        for index in range(argument.captcha_length - 1):
            print(str(index + 1) + " Mismatch count is " + str(analysis[index]))


if __name__ == '__main__':
    run()
