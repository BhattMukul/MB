'''This Program Is To Check Your Typing Speed'''

import datetime
import random
def Challenge(level,ch_lst):
    print(f"\nLevel : {level}")   # Level
    print('''Write The Sentence Below...
            PRESS ENTER WHEN YOU FINISHED\n''')
    enter=str(input("Press Enter To Start The Game ..."))   # to get the user ready
    if enter == '':   # press only enter to start the challenge
        print("Your Time Starts Now...")
        start=datetime.datetime.now()   # Time Starts Now
        index=random.randint(0,len(ch_lst)-1)     # To get the random sentence from the ch_lst provided for challenge
        challenge=ch_lst[index]    # The Sentence which will be given

        print('\n'+challenge)   # print the sentence for challenge
        chal_ans=str(input("\nAnswer : "))    # place where user can copy the above sentence

        end=datetime.datetime.now()   # As User will press enter after completion the time stops

        if chal_ans == challenge:    # condition if he copies the sentence same
            diff_time = end - start   # time for completion
            sec = diff_time.seconds    # how much seconds invested

            # count the words in the provided sentence
            challenge_lst=challenge.split(" ")
            word_count=len(challenge_lst)

            # calculation for speed in WORDS PER MINUTE
            speed=abs((word_count/sec)*60)

            print(f"You Have Completed The Given Challenge in {sec} Seconds")
            print(f"Your Speed : {speed} wpm")

            if level == 'Beginner':
                speed_beg=speed   # return value of speed to Beg() function
                return speed_beg

            elif level == 'Intermediate':
                speed_int=speed
                return speed_int    # return value of speed to Int() function

            elif level == 'Advance':
                speed_adv=speed
                return speed_adv    # return value of speed to Adv() function



        else:
            # if Answer is not as same as the given sentence
            print("Answer Does Not Matched !!!")
            return 1



def Beg():  # Beginner Level Function
    level = "Beginner"
    # all sentences which to be given randomly for challenge, and can be added more if required
    ch_lst = ["The quick brown fox jumps over the lazy dog.",
              "What a beautiful day, here in beautiful and sunny Hawaii.",
              "We climbed to the top of the mountain in just two hours.",
              "The family decided to go to an amusement park on Wednesday."]

    while True:
        print("\n-----Yours Speed Should Be Greater Than 25wps, recommended - >30wps-----")
        result = Challenge(level, ch_lst)  # call to the Challenge function providing level and all sentences
        if result < 25:  # condition for passing the challenge
            print("\nYou Are Not Eligible to Go to Next Level...!")
            continue   # To rerun The same level
        elif result in range(25,31):
            print("\nYou Are Eligible To Go to Next Level, but recommended to Try Again")
            # you can try again same level or can go to next
            try_again=str(input("Press Enter To Try Again or Press 'N' to Go to Next Level'"))
            if try_again == 'n' or try_again == 'N':
                break    # if not want to try again the loop breaks, else loop will execute
            else:
                continue
        elif result > 30:
            print("\nNow Moving To Next Level")
            break    # level clear and moving to next level

    Inter()    # moving to next level




def  Inter():
    # ALL PROCEDURE IS SAME AS BEGINNER LEVEL
    level = "Intermediate"
    ch_lst = ["There are so many places to go in Europe for a vacation Paris, Rome, Prague, etc.",
              "One morning I shot an elephant in my pajamas. How he got into my pajamas I'll never know.",
              "On the periodic table, the letters Fe serve as a symbol for the element (Iron).",
              "The surprise birthday party left him nonplussed; he had known about it for a week already."]

    while True:
        print("\n-----Yours Speed Should Be Greater Than 30wps, recommended - >35wps-----")
        result_int = Challenge(level, ch_lst)
        print(result_int)
        if result_int < 30:
            print("\nYou Are Not Eligible to Go to Next Level...!")
            continue
        elif result_int in range(30, 36):
            print("\nYou Are Eligible To Go to Next Level, but recommended to Try Again")
            try_again_int = str(input("Press Enter To Try Again or Press 'N' to Go to Next Level'"))
            if try_again_int == 'n' or try_again_int == 'N':
                break
            else:
                continue
        elif result_int > 35:
            print("\nNow Moving To Next Level")
            break

    Adv()    # moving to advance level


def Adv():
    level = "Advance"
    ch_lst = ["Truth be told, ! there & is no one * better at capturing % the agony and alarm of a woman in the ! throes of a nervous breakdown than Moore.",
              '"He who knows not, knows not ! he knows not ,is a fool, shun him. He who knows & not, knows he knows % not, is simple, teach him."',
              "How far you go in life depends * on your being tender $ with the young, compassionate @ with the aged, sympathetic with the striving and tolerant of the weak and strong. Because someday in your life you will have been all of these.",
              "Life is a succession of lessons %% which must be lived to be %*@ understood. All is riddle, ! and the key to a riddle is another riddle."]

    while True:
        print("\n-----Yours Speed Should Be Greater Than 35wps, recommended - >40wps-----")
        result_adv= Challenge(level, ch_lst)
        if result_adv < 35:
            print("\nYou Failed Your Speed should be greater than 25 wps")
            continue
        elif result_adv in range(35, 41):
            print("\nYou Have Passed, but recommended to Try Again")
            try_again_adv = str(input("Press Enter To Try Again or Type 'Exit' To Exit "))
            if try_again_adv == 'exit' or try_again_adv == 'Exit':
                break
            else:
                continue
        elif result_adv > 40:
            print("\nYou Passed The Challenge, Congo...")
            break


            #    GAME OVER




print("\nHello And Welcome To MB Typing Challenge\n") #intro part (optional)
print('''Here The Rules Are Simple
If You Complete The Given Challenge As Soon As Possible Then Accordingly You Can Proceed To Next Level

Levels as Follow:-
-- Beginner
-- Intermediate
-- Advance''')

ans=str(input("Wanna Start This Game ('yes' to start) : "))
ans_lst=['y','yes']
if ans.lower() in ans_lst:
    Beg()  # moves to beginner level (def Beg())


