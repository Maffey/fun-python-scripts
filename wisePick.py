				#COUNTERPICK - ENGLISH VERSION
def eng_counterpick(side,lane,position):
    if side == "radiant": #RADIANT
        if lane == "top": #TOP LANE
            if position == "carry":
                print "Pick carry that is good early, such as Slark or Mirana and go solo Nor ask for strong support who can secure kills easily."
            if position == "support":
                print "You should buy wards and run fast to get vision over Dire jungle. You need strong core hero on lane. If that hero will be able to survive on his own, try to gank mid or bot."
            if position == "offlane":
                print "Try to get few last hits, but play safe. Get the every exp you can and when you will be able to fight, try to do so, to make space on the map."
                
                
                
        if position == "mid" or lane == "mid": # MID LANE
            print "Pick obviously hero that really benefit from safe solo lane like that. Most carries with good ultimates will work. Most offlanes will also work. It's up to what your team needs."
            
            
            
        if lane == "bot": #BOT LANE
            if position == "carry":
                print "Any kind of carry can work. But because mostly Radiant bot means jungle and the juke bots near towers, you can go for more risky heroes like Anti-Mage, Spectre or Medusa. Keep in mind that without proper support laning stage may go horribly."
            if position == "support":
                print "Get courier, upgrade it ASAP and try to get boots. You should little babysit your hard carry or any other hero you have on lane but then proceed to create space on map. If you have support that can deal with jungle creeps (Sand King, Crystal Maiden) make something out of it and farm for yourself basic items."
            if position == "offlane":
                print "It's kind of weird place for offlaner but you might want it in few situations but you have to understand why you need it. First of all: You can benefit from jungle (Batrider, Dark Seer etc.); You can also play close to tower thanks to ability to pull, which means you can pick hero that normally would be weak offlaner."
                
        if lane == "jungle": 
             print  "Going jungle means that no matter which role you chose, you won't really play that role. If you picked offlane or mid - well, it's weird. Jungler is either carry or support. Kind of. It's hard to explain so we will focus on two things that jungle provides: safe farm and more heroes on map with solo exp. Many heroes will work - Chen, Enigma, Ursa. Just try to gank lane if your hero is able to do so."

    

	if side == "dire": #DIRE
		if lane == "top": #TOP LANE
			if position == "carry":
				print "Any kind of carry can work. But because mostly Dire top means jungle and the juke bots near towers, you can go for more weak early heroes like Anti-Mage, Spectre or Medusa. Keep in mind that without proper support laning stage may go horribly."
			if position == "support":
				print "Get courier, upgrade it ASAP and try to get boots. You should little babysit your hard carry or any other hero you have on lane but then proceed to create space on map. If you have support that can deal with jungle creeps (Sand King, Crystal Maiden) make something out of it and farm for yourself basic items."
			if position == "offlane":
				print "It's kind of weird place for offlaner but you might want it in few situations but you have to understand why you need it. First of all: You can benefit from jungle (Batrider, Dark Seer etc.); You can also play close to tower thanks to ability to pull, which means you can pick hero that normally would be weak offlaner."
        	
        	
		if position == "mid" or lane == "mid": # MID LANE
			print "Pick obviously hero that really benefit from safe solo lane like that. Most carries with good ultimates will work. Most offlanes will also work. It's up to what your team needs."
                
                
		if lane == "bot": #BOT LANE
			if position == "carry":
				print "Pick carry that is good early such as Slark or Mirana and go solo or ask for strong support who can secure kills easily."
			if position == "support":
				print "You should buy wards and run fast to get vision over Radiant jungle. You need strong core hero on lane. If that hero will be able to survive on his own, try to gank mid or bot."
			if position == "offlane":
				print "Try to get few last hits, but play safe. Get the every exp you can and when you will be able to fight, try to do so, to make space on the map."

			if lane == "jungle": 
				print "Going jungle means that no matter which role you chose, you won't really play that role. If you picked offlane or mid - well, it's weird. Jungler is either carry or support. Kind of. It's hard to explain so we will focus on two things that jungle provides: safe farm and more heroes on map with solo exp. Many heroes will work - Chen, Enigma, Ursa. Just try to gank lane if your hero is able to do so."


	print "Thanks for using this app!"

                	#COUNTERPICK - WERSJA POLSKA
def pol_counterpick(side,lane,position):
    if side == "radiant": #RADIANT
        if lane == "top": #TOP LANE
            if position == "carry":
                print "Wybierz postac dobra w poczatkowej fazie gry, taka jak Slark czy Mirana i idz na linie solo badz popros o dobrego supporta, ktory jest w stanie zapewnic zabojstwa"
            if position == "support":
                print "Powinienes kupic wardy i szybko ruszyc w kierunku lasu Mrocznych. Bedziesz potrzebowal wytrzymala postac na linii. Jesli postac core na twojej linii daje sobie sama rade, sprobuj zgankowac mid albo bot."
            if position == "offlane":
                print "Staraj sie zdobyc kilka last hitow, graj jednak ostroznie. Sprobuj zdobyc kazdy mozliwy punkt doswiadczenia, a kiedy bedziesz gotowy do walki, sprobuj takowa sprowokowac."
                
                
        if position == "mid" or lane == "mid": # MID LANE
            print "Wybierz postac, ktora potrafi wykorzystac zalety z solo exp oraz bycia dosc relatywnie bezpiecznym. Wiekszosc carry z dobrymi umiejetnosciami ostateczni zadziala. Postaci do offlane rowniez beda dzialac. Wszystko zalezy od tego, czego potrzebuje twoja druzyna."
            
            
            
        if lane == "bot": #BOT LANE
            if position == "carry":
                print "Kazdy rodzaj carry zadziala. Dlatego jednak, ze bot Swietlistych oznacza jungle i duzo miejsc do ucieczek blisko wiez, mozesz wziac postacie slabe w poczatkowej fazie gry, takie jak Anti-Mage, Spectre czy Medusa."
            if position == "support":
                print "Kup kuriera, pozniej go ulepsz i jak najszybciej zdobadz buty. Powinienes na poczatku robic za nianke dla swojego carry, nastepnie jednak zaczac 'robic miejsce na mapie'. Jezeli wziales supporta, ktory moze junglowac, wykorzystaj to (Sand King, Crystal Maiden)."
            if position == "offlane":
                print "Troche dziwne miejsce dla offlanera, jednak czasami bardzo przydatne. Musisz jednak wiedziec dlaczego. Przede wszystkim: twoja postac wiele zyskuje na posiadaniu blisko jungli (Batrider, Dark Seer, itp.); Mozesz rowniez grac blizej wiezy dzieki mozliwosci pullowania, co oznacza, ze mozesz wybrac postac, ktora normalnie mie bylaby zbyt dobrym offlanerem."

        if lane == "jungle": 
         	print  "Jezeli idziesz do jungli to tak naprawde niewazne jaka role wybrales - w jungli dziala to troche inaczej. Istnieje tu tylko support i carry, choc i tak nie do konca. Trudno to wytlumaczyc, wiec przejdzmy do konkretow. Musisz wiedziec czym jest jungla w Docie - czyli bezpiecznym miescem do farmienia oraz mozliwoscia zdobycia wiekszej ilosci doswiadczenia bohaterow. Wiele opcji jest w junglii - Chen, Enigma czy Ursa poradza sobie z latwoscia. Pamietaj, by gankowac, jesli masz odpowiednia postac."

                
                
    if side == "dire": #DIRE
        if lane == "top": #TOP LANE
            if position == "carry":
                print "Kazdy rodzaj carry zadziala. Dlatego jednak, ze top Mrocznych oznacza jungle i duzo miejsc do ucieczek blisko wiez, mozesz wziac postacie slabe w poczatkowej fazie gry, takie jak Anti-Mage, Spectre czy Medusa."
            if position == "support":
                print "Kup kuriera, pozniej go ulepsz i jak najszybciej zdobadz buty. Powinienes na poczatku robic za nianke dla swojego carry, nastepnie jednak zaczac 'robic miejsce na mapie'. Jezeli wziales supporta, ktory moze junglowac, wykorzystaj to (Sand King, Crystal Maiden)."
            if position == "offlane":
                print "Troche dziwne miejsce dla offlanera, jednak czasami bardzo przydatne. Musisz jednak wiedziec dlaczego. Przede wszystkim: twoja postac wiele zyskuje na posiadaniu blisko jungli (Batrider, Dark Seer, itp.); Mozesz rowniez grac blizej wiezy dzieki mozliwosci pullowania, co oznacza, ze mozesz wybrac postac, ktora normalnie mie bylaby zbyt dobrym offlanerem."
        
        
            if position == "mid" or lane == "mid": # MID LANE
                print  "Wybierz postac, ktora potrafi wykorzystac zalety z solo exp oraz bycia dosc relatywnie bezpiecznym. Wiekszosc carry z dobrymi umiejetnosciami ostateczni zadziala. Postaci do offlane rowniez beda dzialac. Wszystko zalezy od tego, czego potrzebuje twoja druzyna."
                
                
        if lane == "bot": #BOT LANE
            if position == "carry":
                print "Wybierz postac dobra w poczatkowej fazie gry, taka jak Slark czy Mirana i idz na linie solo badz popros o dobrego supporta, ktory jest w stanie zapewnic zabojstwa"
            if position == "support":
                print "Powinienes kupic wardy i szybko ruszyc w kierunku lasu Swietlistych. Bedziesz potrzebowal wytrzymala postac na linii. Jesli postac core na twojej linii daje sobie sama rade, sprobuj zgankowac mid albo bot."
            if position == "offlane":
                print "Staraj sie zdobyc kilka last hitow, graj jednak ostroznie. Sprobuj zdobyc kazdy mozliwy punkt doswiadczenia, a kiedy bedziesz gotowy do walki, sprobuj takowa sprowokowac"

        if lane == "jungle": 
         	print  "Jezeli idziesz do jungli to tak naprawde niewazne jaka role wybrales - w jungli dziala to troche inaczej. Istnieje tu tylko support i carry, choc i tak nie do konca. Trudno to wytlumaczyc, wiec przejdzmy do konkretow. Musisz wiedziec czym jest jungla w Docie - czyli bezpiecznym miescem do farmienia oraz mozliwoscia zdobycia wiekszej ilosci doswiadczenia bohaterow. Wiele opcji jest w junglii - Chen, Enigma czy Ursa poradza sobie z latwoscia. Pamietaj, by gankowac, jesli masz odpowiednia postac."



    print "Dzieki za skorzystanie z aplikacji!"        





# INPUTS FOR PROGRAM
language = raw_input("What language you prefer? Type 'english' or 'polski'. Jaki jezyk preferujesz? Wpisz 'english' albo 'polski'")

 
import time # FINAL PROCESS
if language == "english":
	team = raw_input("What team you play on? Type 'radiant' or 'dire'")
	place = raw_input("What lane you chose? Type 'top', 'mid', 'jungle' or 'bot'")
	role = raw_input("Which role you are going for? Type 'carry', 'support', 'mid' or 'offlane'")
	eng_counterpick(team,place,role)
if language == "polski":
	team = raw_input("Po jakiej stronie jestes? Wpisz 'radiant' albo 'dire'")
	place = raw_input("Jaka linie wybrales? Wpisz 'top', 'mid', 'jungle' albo 'bot'")
	role = raw_input("Jaka role wybrales? Wpisz 'carry', 'support', 'mid' albo 'offlane'")
	pol_counterpick(team,place,role)

print "You used Wise Pick v. 0.4 made by Matius."
raw_input("Press ENTER to continue. Nacisnij ENTER.")
time.sleep(0.5)
print "Good luck!"

'''

CHANGELOG:
	0.1 - created
	0.2 - added polish version and made few corrections with side
	0.3 - added 'jungle' as a lane; fixed bug causing to show "None" when executed
	0.4 - improvements to code; added easier way to close program (ENTER)

 '''
