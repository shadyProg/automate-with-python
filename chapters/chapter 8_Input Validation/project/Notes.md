> واخد بالك من طريقة كتابة الكود بتاعت ال mult  طريقة حلوا انك تستقبل فقط الصحيح و متشيش البرنامج غير لما input يدخلك صح او ينتهي الوقت 


https://pyinputplus.readthedocs.io/en/latest/


1. Does PyInputPlus come with the Python Standard Library?

2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?

3. What is the difference between inputInt() and inputFloat()?

4. How can you ensure that the user enters a whole number between 0 and

99 using PyInputPlus?

5. What is passed to the allowRegexes and blockRegexes keyword arguments?

6. What does inputStr(limit=3) do if blank input is entered three times?

7. What does inputStr(limit=3, default='hello') do if blank input is entered

three times?


  

1. No. PyInputPlus is a third-party module and doesn’t come with the

Python Standard Library.

2. This optionally makes your code shorter to type: you can type pyip

.inputStr() instead of pyinputplus.inputStr().

3. The inputInt() function returns an int value, while the inputFloat()

function returns a float value. This is the difference between returning

4 and 4.0.

4. Call pyip.inputint(min=0, max=99).

5. A list of regex strings that are either explicitly allowed or denied

6. The function will raise RetryLimitException.

7. The function returns the value 'hello'.