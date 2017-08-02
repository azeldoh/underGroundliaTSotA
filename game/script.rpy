# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")
define a = Character("Ainz")
define z = Character("Big Z")
define e = Character("Echozy")
define c = Character("Cpt. Hardhead")
define t = Character("Torturer")
define d = Character("Dark Lord")
define r = Character("Ruler of the Universe")
define m = Character("Master of Disaster")
define g = Character("George")
define o = Character("Oglaf")
define h = Character("Gabriel")
define k = Character("King Marionette")
define x = Character("Trio")
define n = Character('Unnamed Necromancer')

image tlo1 = "images/backgrounds/tlo1ognisko.png"
image tlo2 = "images/backgrounds/tlo2mapa.png"
image tlo3 = "images/backgrounds/tlo3mgla.png"
image tlo4 = "images/backgrounds/tlo4bezmgly.png"
image tlo5 = "images/backgrounds/tlo5proces.png"
image tlo6 = "images/backgrounds/tlo6salatortur.png"
image tlo7 = "images/backgrounds/tlo7rebelsi.png"
image tlo8 = "images/backgrounds/tlo8cmentarz.png"
image tlo9 = "images/backgrounds/tlo9salatronowa.png"
image tlo10 = "images/backgrounds/tlo10salatronowabeztrio.png"
image tlo11 = "images/backgrounds/tlo11bankiet.png"
image tlo12 = "images/backgrounds/tlo12bankietnekruch.png"
image tlo12h = "images/backgrounds/tlo12happyend.png"
image zgon = "images/backgrounds/ded.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene tlo1 with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    p "Guys, I still can't belive we survived that mess"
    a "Well, yeah. Technically we survived it, but both Z and Echo are in bad shape."
    z "Ainz, didn't I tell you to look after yourself first? I'm totally fine, my back just hurts a bit after falling down. That's all."
    e "Yeah, old grumpy is right. We're both fine. You on the other hand look like one giant bloody mess."
    a "How many times do I have to tell you I accidentally slipped into this red paint barrel? ACCIDENTALLY!"

    menu:

        "Haha, no worries mate, Echo was just kidding!": 

            jump justkidding

        "And I though you did it on a purpose.": 

            jump purpose

    label justkidding:

        a "Yaya, of course."

        jump backtobusiness

    label purpose:

        a "Smarty as always?"

        jump backtobusiness

    label backtobusiness:
    p "Whatever - let's go back to business - do we know what's our next target?"
    z "Big Boss sent this a moment ago - we're supposed to remove a threat near the Tree of The Wiseman."
    e "Phew, at least it seems to be close one this time. Shall we move out P?"
    p "Just after Ainz takes a bath."
    a "..."

    scene tlo2 with dissolve
    "*1 hour from the capital of underGroundlia - late evening*"
    p "So we're supposed to protect the king's minister?"
    z "Seems like it. But it's kinda weird, I remember seing 'Remove a threat' on this paper..."
    e "That's weird but it clearly says protect minister. Didn't you imagine this Z?"
    z "I'm sure it said 'Remove a threat'."
    a "Guys, I don't like it. Something's fishy here. Why would they want us to defend anyone? With our reputation? Cmon."
    a "Everyone knows we're the best when it comes to killing - but defending others? Remember last five fools who wanted us to defend them?"
    z "We all do."
    e "Yeah..."
    p "I also don't like it but this time it's an order. Those previous ones just wanted to hire us. This time we have no choice."
    p "So pack your things and lets go. It says minister expects us to wait for him at Tree of The Wiseman and he's supposed to show there with his guards at midnight."
    a "Midnight? The hell, I thought we're going there during day."
    p "That's what orders say."
    a "I sincerly don't like this."
    e "We all do Ainz. We all do."
    menu:

        "...":
            jump fog

        "We may aswell become deserters.":
            jump nodeserters

    label nodeserters:
        a "Orders are orders. Even if we don't like them."
        z "Indeed."
        e "P, you didn't have to mention it. You know we won't do it."
        jump fog

    

    label fog:

    scene tlo3 with dissolve

    "*Tree of The Wiseman - Midnight, heavy fog*"
    p "Aaand we're here, how long till midnight?"
    e "About a minute."
    z "As always great timing!"
    a "So where is the minister?"
    p "Seems we have to wait for him. Lets sit down then and hope we'll see them thru the fog."
    "*Amazingly strong wind starts to blow*"
    p "What the... Lay down and grab something!"
    "*Wind was so strong that our heroes' only choice not to be blown away was to lay on ground. For some reason ground here was very slippery. After a while both wind and fog were gone to reveal something our heroes would never want to see.*"
    "Meanwhile" "Guards! Search the area! They must be nearby!"

    scene tlo4 with dissolve

    z "...watch out guys."
    a "No... just. No."
    e "I guess those are the ones..."
    z "No doubt it's the minister and his guards. Or at least what's left from them. And we're all covered with their blood..."
    "Guard" "Someone is standing near the Tree of The Wiseman!"
    c "Hey you! Have you seen the m..."
    "Clouds move a bit and moon shines at its fullest at the Tree of The Wiseman"
    c "Oh my god... Guards! Surround and capture them!"

    scene tlo5 with dissolve
    "*Next day, early morning.*"
    c "You have not only killed our king's minister but you've also carried request for his death made by rebel leaders!"
    c "By the authority given to my by our beloved King I hereby sentence you to death for treason."
    c "Giving such scum as you last words is way too much. Begone from my sight."
    c "Torturer, make sure they suffer, afterwards execute them."

    scene tlo6 with dissolve
    "*Several days later*"
    t "Aaand time'a for tha last one. As far'a I know you'va been their capta' so I've made'a sure you seen'a your traitor team suffer first. Must have been'a show, eh scum?"
    "*Torturer removes scraps of cloth from Player's mouth*"
    t "Wanna share'a something before I rip ya'r tongue off?"
    menu:
        "*spits on torturer*":
            jump spit1
        "We were innocent.":
            jump whocares1

    label spit1:
        t "<Cleaning his face> Ya'rll get very special treatment."
        "Player hears some turmoil from the outside"
        t "*Starts searching  for something in the drawer*"
        jump arrow1
    
    label whocares1:
        t "Who cares."
        "Player hears some turmoil from the outside"
        t "One for tongue... two fo' eyes... five fo' nose..."

    label arrow1:
    "*The door to torture chamber opened, torturer didn't notice it happen until arrow pierced his heart.*"
    "*Three characters enter the chamber*"
    g "Look what do we have here."
    g "Three dead bodies and... holy wowie, I recognize them! Those guys were from our kingdom's assasins squad!"    
    g "Why would they end up here... this one is still alive, Oglaf! Check him! Maybe we'll find out what's going on!"
    o "He's beaten up badly, dehydrated but seems like still can move."
    h "How did you end up here? Hey, I'm talking to you!"
    p "*Stares at newcomers not knowing if this is real or not*"
    h "*gives water to Player which he immediately drinks*"
    g "Care to talk now? We saved your life man. At least for now."
    p "See.. those three.. here? Those were.. my comrades.. my closest comrades."
    g "Yeah, this I know. I also know you were from assasins squad. But right now we can't do anything about your comrades so focus on answering my questions."  
    g "Why did you end up here?"
    p "We've.. been set up. Don't know who.. did this.. but when we arrived.. at destination.. minister was dead.. They thought we.. did it.."
    p "paper we got mission.. changed its text.. 'your mission.. defend minister' to.. 'remove.. threat.. near the.. of The Wiseman..'. Signed.. rebel.. leaders."
    g "I don't remember signing such note."
    p "So it's.. you.. the traitors.. who tried to.. the king.."
    g "We forgot to introduce ourselves. We're George, Oglaf and Gabriel. The rebel leaders. And you've been our enemy."
    g "For now you'll live. You're coming with us."
    p "Can.. you at least.. let me bury.. them?"
    g "We'll take their bodies."
    p "Thank.. you..."
    "*Player looses consciousness*"

    scene tlo7 with dissolve

    "*Several days later*"
    g "To think Trio would get rid of their best assasins. Wondering what those fools are planning."
    h "Whatever they plan is we will reach the king before it happens. Old fool won't be of any use for them."
    o "So about their leader - whats your verdict?"
    g "He's the same as us. Betrayed by them. Loyal till the end. I'd say killing him wouldn't be of any use."
    g "Did he wake up?"
    o "Last time I checked he was still unconscious. I'll go and take a look."
    "*Medics tent*"
    o "Oh, good to see you awake."
    p "My comrades, did you bury them?"
    o "Yes."
    p "And that dumb captain?"
    o "Dead."
    p "In this case do whatever to me."
    o "You're free to go wherever you want, but first come and join us. We have to talk a bit."
    o "Sister - is he fine enough to go to the command hq?"
    "Sister" "Better is he stays here for today."
    menu:
        "I can go.":
            jump likegeorge
        "...":
            jump silentone

    label likegeorge:
    "Sister" "You can't."
    o "Hah. Just like George. Stay here, we'll come to you."
    jump hq

    label silentone:
    o "hmm... Then we'll come here later today"
    jump hq


    label hq:
    "*sometime later*"
    p "So you've also been set up?"
    g "Like we said, Trio, which you've known as a Big Boss betrayed us."
    h "They set us up like a bunch of fools."
    o "Everyone thought we tried to kill the king, whereas we tried to protect king from them."
    g "Right now it's not the king who rules over underGroundlia. It's trio."
    g "You must have become dangerous for them so they removed you."
    g "That's how they work."
    h "You could not know it but we've all been spy masters. Leaders of the spy guild, directly operated by the king himself."
    g "So here you are, an outcast, just like us."
    g "Choice is up to you - either join us and try to save the king from those three bastards or go wherever you want to."
    g "Problem with second choice is everyone thinks you've became a traitor. And they want you dead."
    h "Aswell as trio. If they find out you're alive you won't have anywhere to go."
    p "So basically it's either join you or try to survive."
    g "Yes."
    menu:
        "If avenging my comrades means joining you - so be it.":
            jump joined_rebels
        "I'll try my luck.":
            jump ded_explo

    label joined_rebels:
    g "Our side goal except freeing entire kingdom from trio is to make every peasant a free man - that's how we got support from them. Are you fine with this?"
    p "Do as you want, my goal is trio alone."
    g "So be it. Welcome aboard."

    "*Month later*"
    "*Rebels managed to conquer several outposts near underGroundlia*"
    "*Gabriel and Oglaf managed to find out location of secret passage to king's chambers. They almost paid the highest price for this knowledge, barely surviving.*"
    "*Before passing out they managed to give the password which one has to say near the entrance to the hidden passage at the cemetery*"
    "*The password is: Otkin Adarab Utaalk*"
    g "You gotta remember the password, I already forgot how it sounds."
    p "No problem, I will."
    g "So Gabriel and Oglaf will need a lot of time to heal now. It's up you and me now."
    p "Think we can make it together?"
    g "We can."
    p "How powerful is the trio?"
    g "When it comes to physical strenght? They are weaklings. You alone could kill hundred of them without getting tired."
    g "But they posses some magical skills. And noone has a clue how strong they are."
    p "There's a chance they were controlling wind back then when..."
    g "Yes, it could have been them."
    p "They don't deserve to live."
    g "We both know it."
    g "So - in the end only us two are fighters - Oglaf and Gabriel should rest."
    g "We'll take care of trio. We can easily make it with this hidden passage. Just kill those bastards and finally be free."
    g "On a sidenote - wanna know what names they have?"
    menu:
        "Nah, no point in knowing it.":
            jump hidden_passage_password
        "Go on.":
            jump drm

    label drm:
    g "We knew those guys are nuts but their names.."
    g "First calls himself Dark Lord, despite being albino weakling."
    g "Another one calls himself... The Ruler of the Universe."
    p "The what?"
    g "Seems he likes rulers. Or he's even more nuts than the first one."
    g "Last one names himself Master of Disaster. This one at least knows he's useless."
    p "So seems trio, or big boss as I've known them is just a bunch of lunatics?"
    g "Up to you to decide. Yet they got us exiled. And some of us killed. Another name you might not be familiar with is King's name."
    p "Wasn't it Arthur?"
    g "Arthur is his fake name. His true name is.. Marionette."
    p "You're kidding, right?" 
    g "No, I'm deadly serious."
    p "Lets end this madness."

    
    label hidden_passage_password:

    scene tlo8 with dissolve

    "*Cemetery, right next to the entrance to the hidden passage*"
    g "So it's time to say the password. Hope you remember it."

    p "I'm sure it was Otkin Adarab U.. Oh damn."
    g "Don't tell me you forgot it!"
    p "Utkatk, Utalkt or Utaalk... One of those words. Goddamnit."
    g "Better choose the right one."
    menu:
        "Utkatk":
            jump nothinghappens1
        "Utalkt":
            jump nothinghappens2
        "Utaalk":
            jump right_answer
        "<*thinking* I will try to trick it.> Ut#caughing#":
            jump ded_skeletons
    
    label nothinghappens1:
    g "Seems like it's wrong password, try again. At least nothing bad happened."
    menu:
        
        "Utalkt":
            jump nothinghappens3
        "Utaalk":
            jump right_answer
        "<*thinking* I will try to trick it.> Ut#caughing#":
            jump ded_skeletons

    label nothinghappens2:
    g "Seems like it's wrong password, try again. At least nothing bad happened."
    menu:
        "Utkatk":
            jump nothinghappens3
        "Utaalk":
            jump right_answer
        "<*thinking* I will try to trick it.> Ut#caughing#":
            jump ded_skeletons

    label nothinghappens3:
    g "Try again! Or think something out!"
    menu:
        "Utaalk":
            jump right_answer
        "Utyhuyhu":
            jump ded_skeletons
        "<*thinking* I will try to trick it.> Ut#caughing#":
            jump ded_skeletons

    label right_answer:
    "*The doors to the hidden passage open*"
    
    scene tlo9 with dissolve

    "*Hour later*"
    "*Hidden passage, right next to entrance to the throne room*"
    p "Who'd think it would lead us right to the throne room."
    g "Yeah, quite surprising. So what now?"
    p "We'll wait a bit and observe."
    "*Some time later King shows up, slowly sits on the throne.*"
    "*Short while after trio shows up.*"
    g "What the... they are carrying daggers!"
    x "Hello dear king, it's the the time to say goodbye."
    g "*<whispering> Did you notice he said 'the' twice? Told ya they are nuts.*"
    p "Shhh!"
    x "UnderGroundia will become cleansed from every living thing. And you're the one who cleansing will begin at."
    k "Guards!"
    x "You're alone my dear king, noone is going to help you. We've sent every guard to fight rebels. And you didn't notice a thing. Such a fool as you cannot be the king!"
    x "The time has come."
    "*Trio starts to walk towards king*"
    p "Wait for them to pass us, then you take one on the right, I take the left one."
    p "..."
    p "GO!"
    "*Player and George jumped at backs on unexpecting enemies killing them instantly.*"
    "*Before they reached the last one, who was walking several metres in front of others he managed to say some words*"
    "*Player is not sure what he tried to say, but it was something like 'We've been f..'"
    "*Yet before he finished his head was cut down after powerful slash of George.*"

    scene tlo10 with dissolve
    
    k "I cannot belive in what I've just seen!"
    g "Your Majesty, we're glad you are fine. Seems we've reached you in the right moment."
    k "Indeed, now who are you?"
    g "My King, don't you remember me?"
    "*George moves closer to the king*"
    k "Stop right there. Don't thread any closer."
    g "Yes, your majesty."
    k "Remind me, who you are."
    g "George, along with Oglaf and Gabriel we've been your most loyal servants. The spy masters. Those three set us up, framed as traitors."
    "*As you've also known king for a long time his behavior seems unusual, do you want to move closer and take a look at the king?*"
    menu:
        "*Move closer and observe king*":
            jump notbreathing
        "Stand still":
            jump failed_banque

    label notbreathing:
        "*Even though king shouted for you to stop you've went close enough to notice he doesn't seem like he's breathing*"
        "*You also notice King doesn't look too good. Like he's aged a lot since you he've seen him for the last time and it was only several months ago.*"
        jump fla

    label failed_banque:
    p "And I'm the former leader of assasins. Trio too set us up. I'm the last survivor."
    k "I understand, I've made a mistake by giving them so much power. By saving my life you've earned right for one request for each of you."
    k "I shall hear your requests at banque tommorow. Banque especially for you and your followers."
    k "Now go, take those notes <king throws 2 paper rolls> - one of them pardons you and your people."
    k "Another one shall be delivered to earl Black, now go."

    "*Short while after leaving throne room*"
    g "I'm glad trio is dead and we've saved the king."
    p "I'm also glad they are no more. They were actual lunatics. Although king seems weird."
    g "That's true. Maybe we should investigate him a bit before moving on?"
    menu:
        "I don't think it's necessary":
            jump earlblack
        "Let's do it":
            jump lastchance

    label lastchance:
    "*Player and George sneaked back to the throne room, unnoticed by the king they managed to reach close enough to see he doesn't seem like he's breathing and he's in horrible physical shape.*"
    "*They escaped unnoticed and headed towards chambers belonging to Earl Black.*"
    jump beforebanque

    label earlblack:
    "*After being shown both papers and hearing recent events earl Black belived George and Player*"
    "*Earl mentioned he's worried about the king as he hasn't been allowing anyone close to him since several weeks*"
    "*He sets up banque for the next day, glad rebellion is ending and his former friends weren't traitors*"
    
    scene tlo11 with dissolve

    "*Banque*"
    p "There are a lot of full plated guards here, my friend."
    g "Yes, but it can be explained - king still might be in a shock after yesterdays events."
    p "Let's hope it's the reason."
    k "Come my saviors, as I promised I shall hear your requests now."
    g "Your majesty. My request concers freedom of peasants."
    k "You don't have to finish, they are free from now on."
    g "Thank you, yout Majesty"
    p "<thinking>*Somethings not right. Something's definitely not right.*"
    k "And you?"
    p "My King, as I already avenged my comrades my only request now is to become a knight."
    k "So you became a knight."
    p "My King, rite requires you to personally tap my shoulder with a sword."
    k "I'm not bound by rites."
    p "King I knew would never say that."
    "*Clap clap*" "Loud echo goes through the room"
    "*Doors close, blocking everyone inside*"
    "*King collapses, when he hits the ground his bones pierce cloth he was wearing, his rotten flesh looks like he's been dead for several weeks*"
    "*Guards start to walk to George and Player*"
    
    scene tlo12 with dissolve

    "*Dark clothed character walks to throne and kicks kings rotten body out of it.*"
    n "Was it so easy to see through?"
    p "You didn't even bother to try to act like a king."
    n "Maybe I could have observed for a while before killing him."
    "*Guards are getting closer, Player notices they are undead*"
    g "And trio? Who were those guys?"
    n "Fools who belived I will make them immortal."
    n "By the way - you didn't even have to kill them. They'd die a few seconds later."
    n "But as you came to *kings* rescue I couldn't miss this opportunity to gather you all at once. And slaughter you all."
    n "Minions, you shall feast upon their dead bodies."
    "*Everyone fought for their lives but they had no weapons. To make things worse they got outnumbered really fast as every dead defender became necromancers minion.*"
    "*In the end necromancer's minions slaughtered everyone inside*"
    "*underGroundlia became the land of the dead.*"
    scene ded
    "*Bad ending 3/3*"
    return

    label fla:
    p "And I'm the former leader of assasins. Trio too set us up. I'm the last survivor."
    k "I understand, I've made a mistake by giving them so much power. By saving my life you've earned right for one request for each of you."
    k "I shall hear your requests at banque tommorow. Banque especially for you and your followers."
    k "Now go, take those notes <king throws 2 paper rolls> - one of them pardons you and your people."
    k "Another one shall be delivered to earl Black, now go."

    "*Short while after leaving throne room*"
    p "Errr.. what the hell. King being like 'here, take this paper you are pardoned now go?'"
    g "Don't ask me. It's like he doesn't recognize us at all. He's also changed a lot. And trio.."
    p "They were actual lunatics."
    g "This all looks like some lunacy. Whatever, lets bring this paper to earl Black and see what happens. I've known him for years and he's always been loyal to the king."
    jump beforebanque

    label beforebanque:
    "*After being shown both papers and hearing recent events earl Black belived George and Player*"
    "*Earl mentioned he's worried about the king as he hasn't been allowing anyone close to him since several weeks*"
    "*He sets up banque for the next day, glad rebellion is ending and his former friends weren't traitors*"
   
    
    "*One hour before banque*"
    p "I have a bad feeling, something's not right with the king."
    g "Yes, I've also noticed it."
    p "Did you notice he seemed like he wasn't breathing?"
    g "No, maybe you just imagined this."
    p "He also is in horrible shape. It's been only several months since I've seen him for the last time and he looks like walking dead."
    p "Here, hide this special holy needle. I'll have other with me. I got them from the highest priest's artifacts stash."
    p "When only one is used it can kill any undead, when both are used any being with even smallest particle of death magic will die."
    g "Artifact Needle?! Death magic?!"
    p "Just take it. In worst case it will only be uncomfortable for you, in best it might save our lives."

    scene tlo11 with dissolve

    "*Banque*"

    p "There are a lot of full plated guards here, my friend."
    g "Yes, but it can be explained - king still might be in a shock after yesterdays events."
    p "Let's hope it's the reason."
    k "Come my saviors, as I promised I shall hear your requests now."
    g "Your majesty. My request concers freedom of peasants."
    k "You don't have to finish, they are free from now on."
    g "Thank you, your Majesty"
    p "*<thinking> I have to trick him somehow*"
    k "And you?"
    p "My King, as I already avenged my comrades my only request now is to become a knight."
    k "So you became a knight."
    p "My King, rite requires you to personally tap my shoulder with a sword."
    k "I'm not bound by rites."
    p "King I knew would never say that."
    "*Clap clap*" "Loud echo goes through the room"
    "*Doors close, blocking everyone inside*"
    "*King collapses, when he hits the ground his bones pierce cloth he was wearing, his flesh looks like he's been dead for several weeks*"
    "*Guards start to walk to George and Player*"
    
    scene tlo12 with dissolve

    "*Dark clothed character walks to throne and kicks kings rotten body out of it.*"
    n "Was it so easy to see through?"
    p "You didn't even bother to try to act like a king."
    n "Maybe I could have observed for a while before killing him."
    "*Guards are getting closer*"
    g "And trio? Who were those guys?"
    n "Fools who belived I will make them immortal."
    n "By the way - you didn't even have to kill them. They'd die a few seconds later."
    n "But as you came to *kings* rescue I couldn't miss this opportunity to gather you all at once. And slaughter you all."
    n "Minions, you shall feast upon their dead bodies."
    p "George, now or never!"
    "*George and Player start running towards necromancer*"
    "*Player gets hit by spell, which slows him down a bit, George managed to hit necromancer with needle, tearing his flesh, but finally pushing it inside necromancers leg*"
    n "You actually think this will do anything to me?"
    "*Player reaches necromancer, hits him with his needle, piercing his body*"
    "*Both George and Player are thrown to the ground be a huge force*"
    p "Remember the highest priest whom we had to murder for trio? I took some of his blessed insignias. Along with blessed needles. It was really easy to hide them."
    "*Before being able to say anything necromancer turned into dust along with his minions.*"
    scene tlo12h with fade
    "*Good ending*" "underGroundlia is saved!"
    return

    label ded_skeletons:
        "*Earth starts to shake*"
        "*Our heroes try to run away, but rising army of the dead catches them through the ground*"
        "*Unable to move they are slaughtered by the dead army they summoned themselves*"
        scene ded with dissolve
        "Bad ending 2/x"
    return

    label ded_explo:
        "*After two weeks of trying to survive in hostile territory and being unable to even get close to the Trio Player gets discovered while sleeping. By a farm boy.*"
        scene ded with dissolve
        "*Hour later he's hanged on the tree. Traitor is dead.*"
        "Bad ending 1/x"
    return
    # This ends the game.

    
