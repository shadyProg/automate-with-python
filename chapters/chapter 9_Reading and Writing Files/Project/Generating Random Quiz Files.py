from pathlib import Path
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',

'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 
'Salt Lake City', 
'Vermont':'Montpelier', 
'Virginia': 'Richmond', 
'Washington': 'Olympia', 
'WestVirginia': 'Charleston', 
'Wisconsin': 'Madison', 
'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    nameFile = Path(str(quizNum)+'quiz.txt')
    quizFile = open(nameFile, 'a')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    #quizFile.write('''    ====Quiz==== ''')
    '''
    in book 
     quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
 answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    '''
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
# Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3) # =============== don`t understand
        answerOptions = wrongAnswers + [correctAnswer] # =============== 
        random.shuffle(answerOptions)
        for questionNum in range(50):
            quizFile.write(f'{questionNum + 1}. What is the capital of \
                        {states[questionNum]}?\n')    
            for i in range(4):
                quizFile.write(f" \{'ABCD'[i]}. { answerOptions[i]}\n")# =============== don`t understand
                quizFile.write('\n') # =============== don`t understand
                answerKeyFile.write(f"{questionNum + 1} \
                {'ABCD'[answerOptions.index(correctAnswer)]}")# =============== don`t understand
    quizFile.close()
    answerKeyFile.close()