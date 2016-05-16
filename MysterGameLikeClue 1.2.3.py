#from goto import goto, comefrom, label
# -*- coding: utf-8 -*-
import os
import time
has1stkey = 0
questmaterials = 0
hascasefile = 0

print
print "Noir Clue"
print
print raw_input("It was a dark and stormy night. [Enter]")
print raw_input("Well, actually it was only sprinkling, and it was closer to dawn than anything else, but it was a dark dawn, made even darker by the events transpiring just as the sun peaked over the horizon. [Enter]")
print
print "*Crash!*"
print "*Scream!*"
print raw_input("U.I.P: Oh my god, Francis! Someone please help, oh lord! [Enter]")
print
print raw_input("Commissioner: We aren't certain about what it could be yet, the cause of death just doesn’t seem natural, but it doesn't line up with anything we know about. We don't really have the time to look around, which is where you come into I guess... Just poke around a bit, we'll get back to you as soon we have some concrete test results. Oh, and please give my condolences to Harriet, Francis... Francis was a good man... Good Luck. [Enter]")
print
print raw_input("Your name is Clinton Weatherbee and you've been assigned your first investigation as a hired investigator. Granted it's a pretty open and shut case from where you're standing, but it's still yours, and you're going to do the best job you can, right down to the paper work. [Enter]")
print raw_input("All paperwork aside, you are currently standing on a muddy pathway leading up to a... 'cozy' or 'ramshackle' ranch house. It's a faint echo of what was likely a crown jewel of one of the many families that lost their wealth in the Downslide one or two decades back. Now it's fallen to disrepair, paint thinning and peeling from the recent rainshowers, shingles falling off the roof, and what seems to be mold growing in the walls. [Enter]")
def FirstOption():
    print raw_input("In the front of the house there stands Harriet, spouse of the victim. She's discussing the accident with several 'real' policemen. The whole reason why you and your firm were hired was because they couldn't give enough of a damn about it. The commissioner is only pulling an investigation as a favor to the victim. Let's show them how it's done. [Enter]")
    print "Search Grounds"
    print "Question Police"
    print "Question Harriet"
    print "Enter House"
print FirstOption()
QuestStart = raw_input(": ")
while QuestStart != "Search Grounds" or QuestStart != "Question Police" or QuestStart != "Question Harriet" or QuestStart != "Enter House":
       QuestStart = raw_input("(Type an actual answer please): ")
       if QuestStart == "Search Grounds" or QuestStart == "Question Police" or QuestStart == "Question Harriet" or QuestStart == "Enter House":
           break
if QuestStart == "Search Grounds":
    print "You ignore the people and decide to search the area around the house."
    print
    print "If nature was waging war against humanity then this is the front lines. The yard is covered in unkempt grass and is bordered by overgrown bushes. At the side of the house there’s a door… thingy… but on the ground, kinda like the one Dorthy hid in in the wizard of oz, wait no, tried to hid in cause… whatever, it’s a basement door but on the ground. What do you want to look at first?"
    print
    print "Ground Door"
    print "Grass"
    print "Bushes"
    print "Turn Back"
    SidePath1 = raw_input(": ")
    while SidePath1 != "Ground Door" or SidePath1 != "Grass" or SidePath1 != "Bushes" or SidePath1 != "Turn Back":
       SidePath1 = raw_input("(Type an actual answer please): ")
       if SidePath1 == "Ground Door" or SidePath1 == "Grass" or SidePath1 == "Bushes" or SidePath1 == "Turn Back":
           break
    if SidePath1 == "Ground Door":
        if has1stkey == 1:
            print raw_input("As you walk over you just remembered that it's called a cellar. Anyway you wander over to the Cellar Door and remember the key you found earlier. [Enter]")                    
            print raw_input("You take the key out of your pocket and shove it in the lock (just like your prom night), it clicks open (not at all like your prom night) and you open the door and look down at the stairs leading to the cellar (strangely, also like your prom night) [Enter]")
            print raw_input("OH GOD WHAT IS THAT?? AAAAAAAAAAAAHHHH! Hah ha, just kidding, it's too dark to see anything here. You should probably find some sort of flashlight or candle before you do anything else, like walk into a dark room and trip over something. [Enter]")
            EndSide1 = raw_input("Type 'Return' to go back: ")
        if EndSide1 == "Return":
            print FirstOption()
            QuestStart = raw_input(": ")
        if has1stkey == 0:
            print "As you walk over you just remembered that it's called a cellar. Anyway you wander over to the Cellar Door, but upon closer examination you find that it's locked. Well, shit. What a waste of a command prompt. There's gotta be a key somewhere though. *HINT. HINT*"           
            EndSide1 = raw_input("Type 'Return' to go back: ")
        if EndSide1 == "Return":
            print FirstOption()
            QuestStart = raw_input(": ")
    elif SidePath1 == "Bushes":
        print "After a couple of cuts and bruises you come up with… A Plastic Bag! Amazing"
        print raw_input("After rummaging around for awhile you find… Absolutely nothing. Great.")
        print "On your way back from the bushes you find a quarter. Score!"
        EndSide1 = raw_input("Type 'Return' to go back: ")
        if EndSide1 == "Return":
            print FirstOption()
            QuestStart = raw_input(": ")
    elif SidePath1 == "Grass":
        print "You look through the grass and find a key! Hopefully it unlocks something nearby, for what's a key without a lock? A life without problems? Actually a life without problems sounds pretty good right now."
        has1stkey = 1
        questmaterials = 1
        print "Small Key added to the Inventory"
        EndSide1 = raw_input("Type 'Return' to go back: ")
        if EndSide1 == "Return":
            print FirstOption()
            QuestStart = raw_input(": ")
    elif SidePath1 == "Turn Back":
        print FirstOption()
        QuestStart = raw_input(": ")
    else:
        SidePath1 = raw_input(": ")
elif QuestStart == "Question Police":
    print "There are two policemen… er officers, considering that one of them's a girl, they're talking about the Case."
    
    print raw_input("You pretend to be writing something as the police discuss. [Enter]")
    print raw_input("P1: So then I pour the egg and vegetable mix into the fry pan and saute for about... [Enter]")
    print raw_input("P2: You know I love you're cooking, and breakfast foods, but I have to ask, what does this have to do with the case? [Enter]")
    print raw_input("P1: Oh, yeah, well there's a cast iron skillet in the kitchen and you know how I love those so I got thinking and... [Enter]")
    print raw_input("P2: ...and we should really just compare notes [Enter]")
    print raw_input("P1: You for it. None of the people on the grounds seem to have anything to tell us. Some give off some weird vibes, but hey, who doesn't after a death. What about you? [Enter]")
    print raw_input("P2: I couldn't find anything of note around here. Might be something in the cellar, I couldn't get in. Probably not though, I looked through the window and only saw some fruit preserves. Gotta keep busy somehow, eh? I can't imagine being in this property all alone, makes sense why he took so many folks in. Anyway I saw one... Hey! [Enter]")
    print "Oh shit oh crap oh shit"
    print raw_input("P2: You're the hired P.I. right? We'll be going pretty soon but if you need any advice we can share what we have. [Enter]")
    if questmaterials >= 1:
        print raw_input("P1: Hey P.I., you wanna compare notes? [Enter]")
        if has1stkey == 1:
            print "P1: A key without a lock is like a life without problems, not the reason why we became police officers."
    EndSide1 = raw_input("Type 'Return' to go back: ")
    if EndSide1 == "Return":
        print FirstOption()
        QuestStart = raw_input(": ")
elif QuestStart == "Question Harriet":
    raw_input("Harriet looks visibly shaken, he was the one who discovered the body only six hours ago after all. [Enter]")
    print "Harriet: Oh, you're the private detective right? Good morning Sir."
    print "Still very polite though."
    raw_input("What do you want to ask? [Enter]")
    def SideOptions():
        askedHarall = 0
        SP2options = {"Possible Motive", "Discovery of Body", "How He's Getting Along"}
        print SP2options
    SidePath2 = raw_input(": ")
    if SidePath2 == "Possible Motive":
        raw_input("Harriet: I wouldn't really know. Francis never made any enemies and I can't really imagine anyone hating him enough to kill him. [Enter]")
        askedHarall += 1
        SP2options.append("Why do you think it was a murder?")
        SideOptions()
        SidePath2 = raw_input(": ")
    elif SidePath2 == "Why do you think it was a murder?":
        print "Harriet looks insulted"
        raw_input("Harriet: Did you even read the Case File? He had three direct wounds to the chest, that doesn't happen naturally. [Enter]")
        print "You remember that you do, indeed, have the Case File on you."
        hascasefile = 1
        questmaterials = 1
        print "Case File added to the Inventory"
        askedHarall += 1
        SideOptions()
        SidePath2 = raw_input(": ")
    elif SidePath2 == "Discovery of Body":
        print "Harriet: I came downstairs around 5 am this morning, I entered the kitchen looking for Francis, by then... he was already dead.  I didn't see anything, but the window was broken."
        askedHarall += 1
        SideOptions()
        SidePath2 = raw_input(": ")
    elif SidePath2 == "How He's Getting Along":
        raw_input("Harriet: The house has always been pretty empty due to Francis being gone so often, but now it's just... echoes. [Enter]")
        print "Well... that's depressing."
        askedHarall += 1
    if askedHarall == 4:
        raw_input("There's nothing else you can ask right now. [Enter]")
    else:
        SideOptions()
        SidePath2 = raw_input(": ")
    raw_input("Harriet: You're free to go through the house, it's a bit of a mess, it's not like I was expecting people to show up. Please don't harrass my house guests though, they've been through enough already. [Enter]")
elif QuestStart == "Enter House":
    if askedHarall >= 1:
        raw_input("You enter the house, there's a stairway going up, and a door right below the second floor landing, an entryway to the living room on the right, and to the left there is A PIT TO HELL [Enter]")
        FirstHouseOptions = {"Stairway", "Door", "Living Room", "HELL PIT", "Leave"}
        HousePath1 = raw_input(: )
        if HousePath1 == "HELL PIT":
            print "You enter Hell, it's empty, all the sinners must be elsewhere, you walk to the hell castle and sit on the throne, congrats, you now rule hell." 
            print "(GAME OVER)"
            print "Ending: The American Dream"
        if HousePath1 == "Leave":
            print "You just… leave, not just the house but the entire area, you just straight up start walking. Fuck being a private investigator, fuck everything. You live the rest of your life on a farm, you find someone you love and you settle down and have two kids, you forget the investigation and your life as a private investigator, but somehow, you’re happy… Until aliens take over your planet of course."
            print "(GAME OVER)"
            print "Ending: This Ain't Signs"
    if HousePath1 == "Door":
        raw_input("You go through the door. [Enter]")
    if HousePath1 == "Living Room":
        raw_input("You walk into the living room. [Enter]")
    elif askedHarall == 0:
        print "Harriet: Just who are you?"
        SideOptions()
        SidePath2 = raw_input(": ")
else:
    QuestStart = raw_input(": ")
