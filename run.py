import random

class The_options:
    """Defines the options"""
    def __init__(self, number, country, capital, incorrect_1, incorrect_2):
        self.number = number
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2
    
    def the_question(self):
        """shows the repetative parts question with data in there"""
        print(f"\nQuestion {self.number}: What is the capital of {self.country}?\n")
        options = [self.capital, self.incorrect_1, self.incorrect_2]
        random.shuffle(options)
        print('A: ', options[0])
        print('B: ', options[1])
        print('C: ', options[2])
        return options

def the_instructions():
    input("\nWelcome to the capitals quiz, press Enter to continue\n")
    print("You shall be asked for the capital of 10 countries\n")
    print("You shall be given a choice of 3 cities in that country, listed as A, B and C\n")
    print("Please select either A, B or C\n")
    print("You shall be advised if that is the correct answer or not\n")
    print("If you select anything other than A, B or C, you shall be asked to make a choice again until you select A, B or C\n")
    input("Press Enter to continue\n")


def the_quiz():
    """the data"""
    dictionary = [
        {
            'country': 'the United States',
            'capital': 'Washington DC',
            'incorrect_1': 'Los Angeles',
            'incorrect_2': 'New York'
        },
        {
            'country': 'China',
            'capital': 'Beijing',
            'incorrect_1': 'Hong Kong',
            'incorrect_2': 'Shanghai'
        },
        {
            'country': 'Germany',
            'capital': 'Berlin',
            'incorrect_1': 'Hamburg',
            'incorrect_2': 'Munich'
        },
        {
            'country': 'Japan',
            'capital': 'Tokyo',
            'incorrect_1': 'Hiroshima',
            'incorrect_2': 'Osaka'
        },
        {
            'country': 'India',
            'capital': 'New Dheli',
            'incorrect_1': 'Chennai',
            'incorrect_2': 'Mumbai'
        },
        {
            'country': 'the United Kingdom',
            'capital': 'London',
            'incorrect_1': 'Birmingham',
            'incorrect_2': 'Manchester'
        },
        {
            'country': 'France',
            'capital': 'Paris',
            'incorrect_1': 'Lyon',
            'incorrect_2': 'Nice'
        },
        {
            'country': 'Italy',
            'capital': 'Rome',
            'incorrect_1': 'Milan',
            'incorrect_2': 'Naples'
        },
        {
            'country': 'Canada',
            'capital': 'Ottawa',
            'incorrect_1': 'Montreal',
            'incorrect_2': 'Toronto'
        },
        {
            'country': 'Brazil',
            'capital': 'Brasilia',
            'incorrect_1': 'Rio de Janerio',
            'incorrect_2': 'Sao Paulo'
        }
    ]

    score = 0

    for index, question in enumerate(dictionary):
        question = The_options(
            number = index + 1,
            country = question['country'],
            capital = question['capital'],
            incorrect_1 = question['incorrect_1'],
            incorrect_2 = question['incorrect_2']
        )
        options = question.the_question()
        while True:
            available_options = input("\nPlease select an option of A, B or C then press Enter:\n\n")
            if available_options.upper() not in ['A', 'B', 'C']:
                print("That is not a valid option, please select A, B or C\n\n")
            else:
                break

        if available_options.upper() == 'A' and options [0] == question.capital:
            print("Well done, that is the correct option")
            score += 1
            print("Your score is currently:", score)
        elif available_options.upper() == 'B' and options [1] == question.capital:
            print("Well done, that is the correct option")
            score += 1
            print("Your score is currently:", score)
        elif available_options.upper() == 'C' and options [2] == question.capital:
            print("Well done, that is the correct option")
            score += 1
            print("Your score is currently:", score)
        else:
            print("Sorry, that was not the correct option")
            print("Your score remains at:", score)

    print("\nThank your for playing the capitals quiz")
    print("\nYou scored:", score, "points out of 10\n")

the_instructions()  
the_quiz()