import logging
import os
from pathlib import Path
'''
logging.basicConfig(level=logging.DEBUG)

location = Path('./chapter 11_Debugging/test.txt')

def factorial(n):
    with open(location, "w") as file:

        msg = f'Start of factorial({n})'
        logging.debug(msg)
        file.write(msg + '\n')

        total = 1
        for i in range(1, n + 1):
            total *= i

        msg = f'i is {i}, total is {total}'
        logging.debug(msg)
        file.write(msg + '\n')

        msg = f'End of factorial({n})'
        logging.debug(msg)
        file.write(msg + '\n')
        file.close()

    return total

print(factorial(5))
logging.debug('End of program')
'''

# logging.basicConfig(level=logging.DEBUG) # basic config can intial for only one time, if you want to change the config you have to use logging.FileHandler
location = Path('./chapter 11_Debugging/log.txt')
logging.basicConfig(
    filename=location,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)# that right for one time if you want to change the config you have to use logging.FileHandler
'''
some of modes 
---------

logging.basicConfig(
    filename=location,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True  # 👈 يعيد تهيئة logging حتى لو كان متفعل قبل كده
)
------------------------------------------

logging.basicConfig(
    filename=location,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
in disable
logging.disable(logging.CRITICAL)
علشان توقفف كل الرسايل بدل ما انت تروح تمسح واحدة واحدة
طالما وقفت اعلى حاجة كدا اقل منه هيقف طبعا 
بس انت لو قفلت ال level 
اقل منه زي info 
فلسا بيعرض الاعلى منه
'''
logging.debug('Start of program')
def factorial(n):

    logging.debug('Start of factorial(%s%%)' % (n))

    total = 1
    i=1
    for i in range(1 , n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

    logging.debug('End of factorial(%s%%)' % (n))

    return total
print(factorial(5))
logging.debug('End of program')
