import pyinputplus as pyip
import random ,time
numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    # prompt = f'#{questionNumber} : {num1} x {num2} '
    try:
    # Right answers are handled by allowRegexes.
    # Wrong answers are handled by blockRegexes, with a custom message.
    #that code very simple anthor will you write
        pyip.inputStr(prompt,allowRegexes=['^%s$' % (num1 * num2)],blockRegexes=[('.*', 'Incorrect!')],
timeout=8, limit=3)
        
        
        # that my code not good like writer coding
        """
        InputAnswer = pyip.inputNum(prompt,timeout=8, limit=3)
    
        if InputAnswer == num1*num2:
            print('Correct!')
            correctAnswers += 1
        else :
            print('Incorrect!')
        """
        

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    except KeyboardInterrupt:
        print('\n Don`t Run Loser !')
        break
    else:
    # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1


    time.sleep(1) # Brief pause to let user see the result.
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

