# -*- coding: utf-8 -*-
print "Noir Clue"
print
print raw_input("It was a dark and stormy night. [Enter]")
print raw_input("Well, actually it was only sprinkling, and it was closer to dawn than anything else, but it was a dark dawn, made even darker by the events transpiring just as the sun peaked over the horizon. [Enter]")
print
print "*Crash!*"
print "*Scream!*"
print raw_input("U.I.P: Oh my god, Francis! Someone please help, oh lord! [Enter]")
print
print raw_input("Commissioner: We aren't certain about what it could be yet, probably a heart attack, but that doesn't make sense. We don't really have the time to look around, which is where you come into I guess… Just poke around a bit, we'll get back to you as soon we have some concrete test results. Oh, and please give my condolences to Harriet, Francis… Francis was a good one… Good Luck. [Enter]")
print
print raw_input("Your name is Clinton Weatherbee and you've been assigned your first investigation as a hired investigator. Granted it's a pretty open and shut case from where you're standing, but it's still yours, and you're going to do the best job you can, right down to the paper work. [Enter]")
print raw_input("All paperwork aside, you are currently standing on a muddy pathway leading up to a… 'cozy' or 'ramshackle' ranch house. It's a faint echo of what was likely a crown jewel of one of the many families that lost their wealth in the Downslide one or two decades back. Now it's fallen to disrepair, paint thinning and peeling from the recent rainshowers. [Enter]")
print raw_input("In the front of the house there stands Harriet, spouse of the victim. She's discussing the accident with several 'real' policemen. The whole reason why you and your firm were hired was because they couldn't give enough of a damn about it. The commissioner is only pulling an investigation as a favor to the victim. Let's show them how it's done. [Enter]")
print "Search Grounds"
print "Question Police"
print "Question Harriet"
print "Enter House"
QuestStart = raw_input(": ")
if QuestStart == "Search Grounds":
    print "You ignore the people and decide to search the area around the house."
    print
    print "If nature was waging war against humanity then this is the front lines. The yard is covered in unkempt grass and is bordered by overgrown bushes. At the side of the house there’s a door… thingy… but on the ground, kinda like the one Dorthy hid in in the wizard of oz, wait no, tried to hid in cause… whatever, it’s a basement door but on the ground. What do you want to look at first?"
    print "Ground Door"
    print "Grass"
    print "Bushes"
    print "Turn Back"
    SidePath1 = raw_input(": ")
    if SidePath1 == "Ground Door":
        if has1stkey == 1:
            print raw_input("As you walk over you just remembered that it's called a cellar. Anyway you wander over to the Cellar Door and remember the key you found earlier. [Enter]")                    
            print raw_input("You take the key out of your pocket and shove it in the lock (just like your prom night), it clicks open (not at all like your prom night) and you open the door and look down at the stairs leading to the cellar (strangely, also like your prom night) [Enter]")
            print raw_input("OH GOD WHAT IS THAT?? AAAAAAAAAAAAHHHH! Hah ha, just kidding, it's too dark to see anything here. You should probably find some sort of flashlight or candle before you do anything else, like walk into a dark room and trip over something. [Enter]")
        if has1stkey == 0:
            print "As you walk over you just remembered that it's called a cellar. Anyway you wander over to the Cellar Door, but upon closer examination you find that it's locked. Well, shit. What a waste of a command prompt. There's gotta be a key somewhere though. *HINT. HINT*"           
    if SidePath1 == "Bushes":
        
    else:
        SidePath1 = raw_input(": ")
else:
    QuestStart = raw_input(": ")

