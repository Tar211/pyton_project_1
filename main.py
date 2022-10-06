
def story_1():

    Person_name=input("input Person name :  ")
    noun1=input("input noun :  ")
    adjective1=input("input adjective (feeling) :  ")
    verb1=input("input  verb :  ")
    adjective2=input("input adjective (feeling) :  ")
    animal1=input("input an animal :  ")
    verb2=input("input  verb :  ")
    color1=input("input color :  ")
    verb3=input("input verb + ing  :  ")
    adverb=input("input adverb + ly :  ")
    number1=input("input  number :  ")
    timee=input("measure of time:  ")
    color2=input("input  color :  ")
    animal2=input("input animal  :  ")
    number2=input("input number  :  ")
    silly=input("input silly word  :  ")
    noun2=input("input noun again :  ")

    story=" This weekend I am going camping with  "+ Person_name +". I packed my lantern, sleeping bag, and "+noun1+". I am so "+ adjective1+" to "+verb1+" in a tent. I am "+ adjective2+" we might see a(n) "+animal1+", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and "+verb2+". I have heard that the "+ color1+" lake is great for "+verb3+". Then we will "+adverb+" hike through the forest for "+ number1 +" "+ timee+". If I see a "+color2+" "+ animal2+" while hiking, I am going to bring it home as a pet! At night we will tell "+number2+" "+ silly+" stories and roast "+noun2+" around the campfire!!"

    return story

def story_2():

    number1=input("input  number :  ")
    Measure_of_time=input("input Measure of time :  ")
    Mode_of_Transportation=input("input  Mode of Transportation :  ")
    Adjective=input("input Adjective: ")
    Adjective2=input("input Adjective 2: ")
    noun1 = input("input noun :  ")
    color1=input("input color :  ")
    Part_of_the_body=input("input Part of the Body : ")
    Verb1=input("input verb: ")
    number2 = input("input  number :  ")
    noun2 = input("input noun :  ")
    noun3 = input("input noun :  ")
    Part_of_the_body2=input("input Part of the Body : ")
    verb1=input("input  verb :  ")
    noun4 = input("input noun :  ")
    Adjective3 = input("input Adjective 3: ")
    silly = input("input silly word  :  ")


    story="It was about "+number1+" "+ Measure_of_time +" ago when I arrived at the hospital in a "+Mode_of_Transportation+". The hospital is a/an "+Adjective +" place, there are a lot of "+(Adjective2)+" "+ noun1 +" here. There are nurses here who have "+color1+" "+ Part_of_the_body+". If someone wants to come into my room I told them that they have to "+Verb1+" first. I’ve decorated my room with "+number2+" "+ noun2+". Today I talked to a doctor and they were wearing a "+noun3+" on their "+Part_of_the_body2+". I heard that all doctors "+verb1+" "+ noun4 +" every day for breakfast. The most "+Adjective3+" thing about being in the hospital is the "+silly+" "+ noun1+" !"

    return story


def story_3():

    Person_name=input("input Person name :  ")
    adjective1 = input("input adjective (feeling) :  ")
    color1 = input("input color :  ")
    animal1 = input("input an animal :  ")
    place1=input("input place: ")
    adjective2 = input("input adjective (feeling) :  ")
    Magical_Creature1=input("input Magical Creature (Plural): ")
    adjective3 = input("input adjective (feeling) :  ")
    Magical_Creature2 = input("input Magical Creature (Plural): ")
    room=input("input room in a house: ")
    noun1=input("input noun :  ")
    noun2 = input("input noun 2 :  ")
    noun3 = input("input noun (Plural)3 :  ")
    noun4 = input("input noun (Plural)4 :  ")
    adjective4 = input("input adjective (feeling) :  ")
    number1 = input("input  number :  ")
    timee = input("measure of time:  ")
    verb_ing=input("input  verb (ending in ing):  ")
    adjective5 = input("input adjective (feeling) :  ")
    noun5 = input("input noun :  ")



    story="Dear "+Person_name+", I am writing to you from a "+adjective1+" castle in an enchanted forest. I found myself here one day after going for a ride on a "+color1+" "+ animal1 +" in "+place1+". There are "+adjective2+" "+ Magical_Creature1+" and "+adjective3+" "+ Magical_Creature2+" here! In the "+room +" there is a pool full of "+noun1+". I fall asleep each night on a "+noun2+" of "+noun3+" and dream of "+adjective4+" "+ noun4+". It feels as though I have lived here for "+number1+" "+ timee+". I hope one day you can visit, although the only way to get here now is "+verb_ing+" on a "+adjective5+" "+noun5 +"!!"

    return story





while True:
    choice = input("Choose one of our stories inputing 1,2 or 3 : ")
    if choice == "1" or choice == "2" or choice == "3":
        if choice == "1":
            print(story_1())
            break
        elif choice == "2":
            print(story_2())
            break
        elif choice == "3":
            print(story_3())
            break
    else:

        print("please choose numbers 1,2 or 3:")













