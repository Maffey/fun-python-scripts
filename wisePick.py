# COUNTERPICK - ENGLISH VERSION
print("This program is outdated. Please don't take the advice below seriously.")


# FUNCTION DEFINED
def counterpick(side, lane, position):
    # PRINT VARIABLES DEFINED. IN ORDER: CARRY SAFELANE, CARRY HARDLANE, SUPPORT SAFELANE, SUPPORT HARDLANE,
    # OFFLANE SAFELANE, OFFLANE HARDLANE, MID, JUNGLE
    cs = "Any kind of carry can work. But because mostly Radiant bot means jungle and the juke bots near towers," \
         " you can go for more risky heroes like Anti-Mage, Spectre or Medusa." \
         " Keep in mind that without proper support laning stage may go horribly."
    ch = "Pick carry that is good early, such as Slark or Mirana and go solo or ask for strong support" \
         " who can secure kills easily."
    ss = "Get courier, upgrade it ASAP and try to get boots. You should little babysit your hard carry" \
         " or any other hero you have on lane but then proceed to create space on map. If you have support" \
         " that can deal with jungle creeps (Sand King, Crystal Maiden)" \
         " make something out of it and farm for yourself basic items."
    sh = "You should buy wards and run fast to get vision over Dire jungle. You need strong core hero on lane." \
         " If that hero will be able to survive on his own, try to gank mid or bot."
    os = "It's kind of weird place for offlaner but you might want it in few situations but you have to understand" \
         " why you need it. First of all: You can benefit from jungle (Batrider, Dark Seer etc.); You can also" \
         " play close to tower thanks to ability to pull, which means you can pick hero that normally" \
         " would be weak offlaner."
    oh = "Try to get few last hits, but play safe. Get the every exp you can and when you will be able to fight," \
         " try to do so, to make space on the map."
    m = "Pick obviously hero that really benefit from safe solo lane like that." \
        " Most carries with good ultimates will work. Most offlanes will also work." \
        " It's up to what your team needs."
    j = "Going jungle means that no matter which role you chose, you won't really play that role." \
        " If you picked offlane or mid - well, it's weird. Jungler is either carry or support." \
        " Kind of. It's hard to explain so we will focus on two things that jungle provides: safe farm" \
        " and more heroes on map with solo exp. Many heroes will work - Chen, Enigma, Ursa." \
        " Just try to gank lane if your hero is able to do so."
    error_side = "Could not identify 'side'. Please try again."
    error_lane = "Could not identify lane. Please try again."
    error_pos = "Could not identify position. Please try again."

    if side == "radiant":  # RADIANT
        if lane == "top":  # HARDLANE
            if position == "carry":
                print(ch)
            elif position == "support":
                print(sh)
            elif position == "offlane":
                print(oh)
            else:
                print(error_pos)

        elif lane == "mid" or position == "mid":  # MID LANE
            print(m)

        elif lane == "bot":  # SAFELANE
            if position == "carry":
                print(cs)
            elif position == "support":
                print(ss)
            elif position == "offlane":
                print(os)
            else:
                print(error_pos)

        elif lane == "jungle":
            print(j)
        else:
            print(error_lane)



    elif side == "dire":  # DIRE
        if lane == "top":  # SAFELANE
            if position == "carry":
                print(cs)
            elif position == "support":
                print(ss)
            elif position == "offlane":
                print(os)
            else:
                print(error_pos)

        elif lane == "mid" or position == "mid":  # MID LANE
            print(m)

        elif lane == "bot":  # HARDLANE
            if position == "carry":
                print(ch)
            elif position == "support":
                print(sh)
            elif position == "offlane":
                print(oh)
            else:
                print(error_pos)
        elif lane == "jungle":
            print(j)
        else:
            print(error_lane)
    else:
        print(error_side)


# INPUTS FOR PROGRAM

team = input("What team you play on? Type 'radiant' or 'dire'")
place = input("What lane you chose? Type 'top', 'mid', 'jungle' or 'bot'")
role = input("Which role you are going for? Type 'carry', 'support', 'mid' or 'offlane'")
survey = input("What patch do you play on?")

try:
    file = open("wise_pick.txt", "a")
    file.write("Game patch: " + survey + "\n")
    counterpick(team, place, role)
finally:
    file.close()

    print("\nYou used Wise Pick v. 0.9 made by Matius on Python 3.5. \nLet the donger be with you.")
    input("\nPress ENTER to continue.")

    # CHANGELOG:
    # 0.1 - created
    # 0.2 - added polish version and made few corrections with 'side'
    # 0.3 - added 'jungle' as a lane; fixed bug causing to show "None" when executed
    # 0.4 - improvements to code; added easier way to close program (ENTER)
    # 0.5 - added question survey
    # 0.6 - code optimisation, upgrade from Python 2.7 to 3.5 removed polish version, fixed file.write
    # 0.7 - now catching inputs' errors
    # 0.8 - reconstruction of 'counterpick' function, additional block of code added
    # 0.9 - further optimisation

    # TO DO:
    # -add counting answers to survey.exe
    # -add while to 'counterpick'
    #
