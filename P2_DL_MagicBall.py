import random
from enchant.checker import SpellChecker


def spell_check(text):
    count = 0
    new_text = text.replace("coke", "")
    new_text1 = new_text.replace("cola", "")
    new_text2 = new_text1.replace("coca", "")
    checker = SpellChecker("en_US")
    checker.set_text(new_text2)
    for err in checker:
        if err:
            count += 1

    return count

def quick_bye():
    quick_bye_phrases = [
                 "\nI take that you have no question. Bye!\n",
                 "\nI take that as you have no question. Cya!\n",
                 "\nI guess that's a no.\n",
                 "\nMaybe you do have a question, and answered it like...\n"
                 "'I have a question.' I'm just a Magic 8 ball, so I can\n"
                 "only answer questions if you say something like 'yes'.\n",
                 "\nNo question? A bummer.\n",
                 "\nWell, no questions today!\n",
                 "\nGuess not.\n"
    ]
    return quick_bye_phrases[random.randrange(0, len(quick_bye_phrases))-1]

def initial_check(text):
    if text == "":
        ball_blank_phrase = [
            "That's... some question.\n",
            "How do I answer this?\n",
            "Blank question?\n",
            "There's no question?\n",
            "Did you use invisible text?\n",
            "Where did the question go?\n",
            "I don't see a question. Is there a bug?\n"
        ]
        print ""
        print(ball_blank_phrase[random.randrange(0, len(ball_blank_phrase))-1])
    elif "?" not in text and "!" not in text:
        ball_no_question_mark_phrases = [
            "I don't have eyes, but I can see that your 'question' has no question marks.\n",
            "Is that supposed to be a question?\n",
            "Searching for '?'... \n"
            "--------ERROR--------\n"
            "------NONE FOUND------\n",
            "Every question ends with a question mark!\n",
            "Do you need to type a '?' for it to be a question? \n"
            "Apparently, you do. That's kind of annoying... \n",
            "As a Magic 8 ball, its a shame I can't understand questions without a '?'\n",
            "Actually, I accept questions without a question mark.\n"
            "For example, I accept... 'Tell me a Fun Fact!'"
        ]
        print ""
        print(ball_no_question_mark_phrases[random.randrange(0, len(ball_no_question_mark_phrases))-1])
    elif text == "qqq":
        print ""
        print "Here are some example questions I can answer:\n" \
              "What is CocaCola?\n" \
              "Nutrition Facts?\n" \
              "What is in a bottle of CocaCola?\n" \
              "What are some Fun Facts?\n"
    elif spell_check(text) > 0:
        bad_english = [
            "I don't understand what you just typed.\n",
            "Is this supposed to be English?\n",
            "I can't read this.\n",
            "Spell_Checking... Mistakes Found.\n",
            "This doesn't make much sense.\n",
            "Sorry, I can't read this alien language.\n"
        ]
        print ""
        print(bad_english[random.randrange(0, len(bad_english)) - 1])
    else:
        return "pass"

def check_1(text):
    if   "coke" in text and "what" in text and "nutri" not in text and "fact" not in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "coke" in text and  "wut" in text and "nutri" not in text and "fact" not in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "coca" in text and "what" in text and "nutri" not in text and "fact" not in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "coca" in text and  "wut" in text and "nutri" not in text and "fact" not in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "cola" in text and "what" in text and "nutri" not in text and "fact" not in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "cola" in text and  "wut" in text and "nutri" not in text and "fact" not in text and "in" not in text and "sell" not in text:
        return "pass"
    else:
        return "fail"
def pass_1():
    say_1 = [
        "Also known as Coke, CocaCola is a carbonated soft drink.",
          "CocaCola is a drink created in 1886 by Dr. John S. Pemberton in Georgia.",
          "CocaCola is the most popular and most-selling soft drink in history!"
    ]
    return say_1[random.randrange(0, len(say_1)) - 1]
def check_2(text):
    if "coke" in text and "what" in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "coke" in text and  "wut" in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "coca" in text and "what" in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "coca" in text and  "wut" in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "cola" in text and "what" in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "cola" in text and  "wut" in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "in" in text:
        return "pass"
    else:
        return "fail"
def pass_2():
    say_2 = [
        "A bottle of Original CocaCola contains Carbonated water, high fructose corn syrup, caramel color, phosphoric acid, natural flavors, and caffeine!",
        "In a 7.5 fl oz bottle of Original CocaCola, there are 25 grams of sugar!",
        "In a 7.5 fl oz bottle of Original CocaCola, there are 21 milligrams of caffeine!",
        "In a 7.5 fl oz bottle of Original CocaCola, there are 90 Calories!",
        "In a 12 fl oz bottle of Original CocaCola, there are 39 grams of sugar!",
        "In a 12 fl oz bottle of Original CocaCola, there are 34 milligrams of caffeine!",
        "In a 12 fl oz bottle of Original CocaCola, there are 140 Calories!",
        "In a 16 fl oz bottle of Original CocaCola, there are 52 grams of sugar!",
        "In a 16 fl oz bottle of Original CocaCola, there are 45 milligrams of caffeine!",
        "In a 16 fl oz bottle of Original CocaCola, there are 190 Calories!",
        "In a 20 fl oz bottle of Original CocaCola, there are 65 grams of sugar!",
        "In a 20 fl oz bottle of Original CocaCola, there are 57 milligrams of caffeine!",
        "In a 20 fl oz bottle of Original CocaCola, there are 240 Calories!",
    ]
    return say_2[random.randrange(0, len(say_2)) - 1]
def check_3(text):
    if "coke" in text and "what" in text and "sell" not in text and "vanilla" in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "coke" in text and  "wut" in text and "sell" not in text and "vanilla" in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "coca" in text and "what" in text and "sell" not in text and "vanilla" in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "coca" in text and  "wut" in text and "sell" not in text and "vanilla" in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "cola" in text and "what" in text and "sell" not in text and "vanilla" in text and "cherry" not in text and "in" in text:
        return "pass"
    elif "cola" in text and  "wut" in text and "sell" not in text and "vanilla" in text and "cherry" not in text and "in" in text:
        return "pass"
    else:
        return "fail"
def pass_3():
    say_3 = [
        "A bottle of Vanilla CocaCola contains carbonated water, high fructose corn syrup, caramel color, phosphoric acid, natural flavors, and caffeine!",
        "In a 12 fl oz bottle of Vanilla CocaCola, there are 42 grams of sugar!",
        "In a 12 fl oz bottle of Vanilla CocaCola, there are 34 milligrams of caffeine!",
        "In a 12 fl oz bottle of Vanilla CocaCola, there are 150 Calories!",
        "In a 20 fl oz bottle of Vanilla CocaCola, there are 70 grams of sugar!",
        "In a 20 fl oz bottle of Vanilla CocaCola, there are 57 milligrams of caffeine!",
        "In a 20 fl oz bottle of Vanilla CocaCola, there are 260 Calories!",
    ]
    return say_3[random.randrange(0, len(say_3)) - 1]
def check_4(text):
    if "coke" in text and "what" in text and "sell" not in text and "vanilla" not in text and "cherry" in text and "in" in text:
        return "pass"
    elif "coke" in text and  "wut" in text and "sell" not in text and "vanilla" not in text and "cherry" in text and "in" in text:
        return "pass"
    elif "coca" in text and "what" in text and "sell" not in text and "vanilla" not in text and "cherry" in text and "in" in text:
        return "pass"
    elif "coca" in text and  "wut" in text and "sell" not in text and "vanilla" not in text and "cherry" in text and "in" in text:
        return "pass"
    elif "cola" in text and "what" in text and "sell" not in text and "vanilla" not in text and "cherry" in text and "in" in text:
        return "pass"
    elif "cola" in text and  "wut" in text and "sell" not in text and "vanilla" not in text and "cherry" in text and "in" in text:
        return "pass"
    else:
        return "fail"
def pass_4():
    say_4 = [
        "A bottle of Cherry CocaCola contains carbonated water, high fructose corn syrup, caramel color, phosphoric acid, natural flavors, and caffeine!",
        "In a 12 fl oz bottle of Cherry CocaCola, there are 42 grams of sugar!",
        "In a 12 fl oz bottle of Cherry CocaCola, there are 34 milligrams of caffeine!",
        "In a 12 fl oz bottle of Cherry CocaCola, there are 150 Calories!",
        "In a 16 fl oz bottle of Cherry CocaCola, there are 56 grams of sugar!",
        "In a 16 fl oz bottle of Cherry CocaCola, there are 45 milligrams of caffeine!",
        "In a 16 fl oz bottle of Cherry CocaCola, there are 200 Calories!",
        "In a 20 fl oz bottle of Cherry CocaCola, there are 70 grams of sugar!",
        "In a 20 fl oz bottle of Cherry CocaCola, there are 57 milligrams of caffeine!",
        "In a 20 fl oz bottle of Cherry CocaCola, there are 260 Calories!",
    ]
    return say_4[random.randrange(0, len(say_4)) - 1]
def check_5(text):
    if   "coke" in text and "how" in text and "nutri" not in text and "in" not in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "sold" in text:
        return "pass"
    elif "coca" in text and "how" in text and "nutri" not in text and "in" not in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "sold" in text:
        return "pass"
    elif "cola" in text and "how" in text and "nutri" not in text and "in" not in text and "sell" not in text and "vanilla" not in text and "cherry" not in text and "sold" in text:
        return "pass"
    else:
        return "fail"
def pass_5():
    say_5 = [
        "There is over a 100 million bottles of Original CocaCola sold every day!",
        "A lot of Coke is sold. A lot.",
        "1.7 billion servings of Coke products are consumed every day.",
        "Over 26 billion cases of product was sold in 2011!",
    ]
    return say_5[random.randrange(0, len(say_5)) - 1]
def check_6(text):
    if   "coke" in text and "nutri" not in text and "fact" in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "coke" in text and "nutri" not in text and "fact" in text and "in" not in text and "sell" not in text:
        return "pass"
    elif "coke" in text and "nutri" not in text and "fact" in text and "in" not in text and "sell" not in text or "fun" in text:
        return "pass"
    elif "coke" in text and "nutri" not in text and "fact" in text and "in" not in text and "sell" not in text or "fun" in text:
        return "pass"
    else:
        return "fail"
def pass_6():
    say_6 = [
        "Fun Fact #01: In 1985, CocaCola became the first soft drink in space!",
        "Fun Fact #02: When Coca-Cola first launched it was marketed as a nerve tonic that relieves exhaustion.",
        "Fun Fact #03: Coca Cola is sold in more than 200 countries.",
        "Fun Fact #04: The first bottle of Coke contained an average of 9 milligrams of cocaine",
        "Fun Fact #05: Coca leaves, an ingredient used in the manufacturing of Coca Cola are imported from Peru.",
        "Fun Fact #06: There are only two countries in the world where Coca-Cola is not sold: Cuba and North Korea.",
        "Fun Fact #07:  A can of Coke will sink in water whereas a can Diet Coke will float.",
        "Fun Fact #08: CocaCola owns over 3,500 different beverages!",
        "Fun Fact #09: Cocaine was removed from CocaCola in 1903",
        "Fun Fact #10: The name CocaCola was made by Frank Robinson.",
        "Fun Fact #11: Mexicans are the biggest drinkers of Coke in the world.",
        "Fun Fact #12: The unique logo of CocaCola was penned by Frank Robinson, and continues to be used today.",
        "Fun Fact #13: CocaCola is the second most recognized term in the world, after the 'Ok' hand gesture!",
        "Fun Fact #14: On average, Mexicans drink 745 Coke beverages a year and Americans drink 401 Coke products a year.",
        "Fun Fact #15: CocaCola used to contain real cane sugar. Now it just contains high fructose corn syrup.",
        "Fun Fact #16: Coke says the 'perfect' temperature to serve its drink is from 34 to 38 degrees Fahrenheit.",
        "Fun Fact #17: Coke's brand is worth over $83.8 billion",
        "Fun Fact #18: All the CocaCola bottle stacked in a tower would reach the moon over 2,000 times!",
        "Fun Fact #19: Coca-Cola owns over half of all soft drinks sold",
        "Fun Fact #20: Coke invented the six-pack in 1932 to encourage people to drink more Coke. ",
        "Fun Fact #21: In the 1980s, an obscene image was hidden into one of the ice cubes in a Coca-Cola ad in South Australia.\n"
        " The company recalled and destroyed all of the posters, and the artist responsible for the image was fired and sued.",
        "Fun Fact #22: Dr. Pepper is bottled by both Coca-Cola and Pepsi, depending on the location in USA.",
        "Fun Fact #23: There are over 10,000 CocaCola soft drinks consumed every second!",
        "Fun Fact #24: In the 90's, Coca Cola had a plan to have their vending machines automatically raise or lower the \n"
        " price of a soda according to that day's temperature, but didn't go through with it.",
        "Fun Fact #25: Farmers Union Iced Coffee outsells Coca-Cola in South Australia \n"
        "making it the only place in the world where a milk drink outsells a cola product.",
        "Fun Fact #26: The red and white label of Coca Cola is recognized by about 94% of world's population.",
        "Fun Fact #27: Someone once tried to sell of Coca Cola's secret ingredients \n"
        "to Pepsi but Pepsi refused and instead reported the incident to Coca Cola and FBI.",
        "Fun Fact #28: Coca Cola is responsible for inventing the current widely used image of Santa Claus. \n"
        "An artist painted that image in one of Coca Cola's Christmas advertisements and it went viral.",
        "Fun Fact #29: CocaCola used to contain cocaine in it!",
        "Fun Fact #30: Because men associated Diet Coke with women, Coca-Cola created Coke Zero for men.",
        "Fun Fact #31: Only 3.1% of all beverages consumed around the world are Coca-Cola products.",
        "Fun Fact #32: In 2001, Coca-Cola ran a program called H2NO - A campaign to\n"
        " teach waiters at Olive Garden how to get customers to say 'No' to H2O",
        "Fun Fact #33: CocaCola came up with Coke cans for easier shipment to armed forces overseas",
        "Fun Fact #34: CocaCola owns VitaminWater, SmartWater, CocaCola, Sprite, MezzoMix, \n"
        "Dasani water, Fanta, MinuteMaid, Nestea, Monster, MelloYello, Fruitpoia, Ciel, \n"
        "Powerade, Simply Orange, Fresca, Fuze Tea, Honest Tea, and Odwalla."

    ]
    return say_6[random.randrange(0, len(say_6)) - 1]

def main():
    still_asking_questions = 1
    print ""
    print "Magic 8 Ball speaking. Do you have a question?"
    first_line = raw_input("Input: ")
    first_line = first_line.lower()
    if "yes" in first_line or "yeah" in first_line or "yep" in first_line or "yeh" in first_line or "yah" in first_line:
        print "\nWell, I can only answer questions about CocaCola."
        print "If you can't figure out the types of questions I can answer, type: qqq"
        print "Ask away!\n"
        while still_asking_questions == 1:
            question = raw_input("Question: ")
            question = question.lower()
            print ""
            if initial_check(question) != "pass":
                pass
            elif check_1(question) == "pass":
                print(pass_1())
            elif check_2(question) == "pass":
                print(pass_2())
            elif check_3(question) == "pass":
                print(pass_3())
            elif check_4(question) == "pass":
                print(pass_4())
            elif check_5(question) == "pass":
                print(pass_5())
            elif check_6(question) == "pass":
                print(pass_6())
            else:
                print "Sorry, I don't know how to answer that. :(\n"
            print ""
            ask_another_maybe = 1
            ask_another = raw_input("Another question? (Yes/No) : ")
            ask_another = ask_another.lower()
            while ask_another_maybe == 1:
                if "no" in ask_another or "nah" in ask_another:
                    still_asking_questions = 0
                    ask_another_maybe = 0
                elif "yes" in ask_another or "yeah" in ask_another or "yep" in ask_another or "yeh" in ask_another or "yah" in ask_another:
                    still_asking_questions = 1
                    ask_another_maybe = 0
                else:
                    print "I don't understand this input. :/"
                    ask_another = raw_input("Another question? (Yes/No) : ")
                    ask_another = ask_another.lower()
    elif "?" in first_line:
        print "I asked if you had a question, not for you to ask me one!"
    else:
        print(quick_bye())


main()