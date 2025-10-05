def main_menu():
	print("""
		1. Phone book
		2. Messages
		3. Chat
		4. Call register
		5. Tones
		6. Settings
		7. Call divert
`		8. Games
		9. Calculator
		10. Reminders
		11. Clock
		12. Profiles
		13. SIM Service
		14. Exit

	""")

	menu = input("Enter any number from 1- 14: ")

	match menu :
		case "1" : phone_book()
		case "2" : messages()
		case "3" : chat()
		case "4" : call_register()
		case "5" : tones()
		case "6" : setting()
		case "7" : call_divert()
		case "8" :  game()
		case "9" : calculator()
		case "10" : reminder()
		case "11" : clock()
		case "12" : profiles()
		case "13" : sim_service()
		case "14" : print("Exiting")
		case _ : 
			print("You entered wrong number")
			main_menu()	

			
def phone_book():
	print("phone book")

	print(""" 
		PHONE BOOK MENU:
				 
		1 -> search
	   	2 -> Service Nos
	  	3 -> Add name
		4 -> Erase
	   	5 -> edit
	  	6 -> Assign tone
	    	7 -> Send  b'card
	    	8 -> options
	    	9 -> Speed dials
	    	10 -> Voice tags
		11 -> Back to main menu
		""")
	phone_book = input("Press any key from 1 - 10: ")
		
	match phone_book :
		case "1" : search() 
		case "2" : service_nos()
		case "3" : add_name()
		case "4" : erase()
		case "5" : edit()
		case "6" : assign_tone()
		case "7" : send_b()
		case "8" : option()
		case "9" : speed_dials()
		case "10" : voice_tags()
		case "11" : main_menu()
		case _ : 
			print("You entered wrong number") 
			phone_book() 
						
def search():
	print("Search")
	search = input("Press 0 to back to phone book menu: ")
	match search :
		case "0" : phone_book()
			 

def service_nos():
	print("Service nos")
	service = input("Press 0 to back to phone book menu: ")
	match service :
		case "0" : phone_book()

def add_name():
	print("Add name")
	add = input("Press 0 to back to phone book menu: ")
	match add :
		case "0" : phone_book() 

def erase():
	print("Erase")
	erase = input("Press 0 to back to phone book menu: ")
	match erase :
		case "0" : phone_book()
		
def edit():
	print("edit")
	edit = input("Press 0 to back to phone book menu: ")
	match edit :
		case "0" : phone_book()

def assign_tone():
	print("assign tone")
	assign = input("Press 0 to back to phone book menu: ")
	match assign :
		case "0" : phone_book()	

def send_b():
	print("Send B'card")
	send = input("Press 0 to back to phone book menu: ")
	match send :
		case "0" : phone_book()
				

def option():
	print("Options")

	print(""" 
		OPTION MENU
		1 -> Type of view 
		2 -> Memory Status
		3 -> Back to phone_book
		""")

	options = input("press any key from 1 - 2: ")
			
	match options :
		case "1" : type()
		case "2" :  memory()
		case "3" : phone_book() 
		case _ : 
			print("You entered wrong") 
			option()


def type():
	print("Type of view")
	type = input("press 0 to go back to option menu")
	match type :
		case "0" :  option()
		case _  : 
			print("You entered wrong")
			type()

def memory():
	print("Memory status")
	memory = input("press 0 to go back to option menu")
	match memory :
		case "0" :  option()
		case _ : 
			print("You entered wrong")
			memory()
	



def speed_dial():
	print("Speed dials")
	speed = input("Press 0 to back to phone book menu: ")
	match speed :
		case "0" : phone_book()

def voice_tags():
	print("Voice tags")
	speed = input("Press 0 to back to phone book menu: ")
	match voice :
		case "0" : phone_book()		










def messages():
	print("Messages")
		
	print("""
			MESSAGE MENU:
				 
		1 -> Write messages
	   	2 -> Inbox
	  	3 -> Outbox
		4 -> Picture messages
	   	5 -> Templates
	  	6 -> Smileys
	    	7 -> Message Settings
	    	a-> Set
	    	i -> Message centre number
	    	ii -> Message sent as
		iii -> Message validity
	    	b -> common 
	    	i -> Deivery reports
		ii -> Reply via same centre
		iii -> Charater support
	        8 -> Info service
	  	9 -> Voice mailbox number
	    	10 -> Service command editor
		11 -> Back to main menu

	""")

	message_menu = input("Press any key from 1 - 10: ")
	match message_menu :
		case "1" : write_messages()
		case "2" : inbox()
		case "3" : outbox()
		case "4" : picture_mesages()
		case "5" : template()
		case "6" :  smileys()
		case "7" :  message_setting()
		case "8" : info()
		case "9" : voice_mail()
		case "10": service_command()
		case "11" : main_menu()
		case _ :
			print("you entered wrong") 
			messages()
		
def write_messages():
	print("Write Mesages")
	write = input("Press 0 to back to message menu: ")
	match write :
		case "0" : messages()	
			

def inbox():
	print("Inbox")
	inbox = input("Press 0 to back to message menu: ")
	match inbox :
		case "0" : messages()

def outbox():
	print("Outbox")
	inbox = input("Press 0 to back to message menu: ")
	match outbox :
		case "0" : messages()


def picture_messages():
	print("Picture Messages")
	picture = input("Press 0 to back to message menu: ")
	match picture :
		case "0" : messages()


		
def template():
	print("Templates")
	template = input("Press 0 to back to message menu: ")
	match template :
		case "0" : messages()


		
def message_setting():
	print("Mesage Setting")
	print( """ 
		 MESSAGES MENU
		1 -> Set 1
		2 -> common
		3 -> Back to messages menu	
		""")

	message_setting = (input("Press any key from 1 - 2: "))
	match message_setting :
		case "1" : set()
		case "2" : common()
		case "3" : messages()
		case _ :
			 print("You entered wrong number")
			 message_setting()

def set():
	print("Set 1")
	print(""" 
	SET MESSAGES MENU
	1 -> Message centre number
	2 -> Mesage sent as
	3 -> Message validity
	""")
	set_messages = input("press any key from 1 - 3: ")
	match set_messages :
		case "1" : print(" Message centre number")

		case "2" : print("Mesage sent as")

		case "3" : print(" Message validity")


def common():
	print("common")
							
	print("""
	COMMON MENU
	1 -> delivery report
	2 -> Reply via same centre
	3 -> character report	
	""")
	common = int(input("press any key from 1 - 3: "))
							
	match common :
		case "1" : print("Delivery report")

		case "2" : print("Reply via same centre")

		case "3" : print("Character report")


				

				


def smileys():
	print("Smileys")
	smileys = input("Press 0 to back to message menu: ")
	match smileys :
		case "0" : messages()


def info():
	print("Info services")
	info = input("Press 0 to back to message menu: ")
	match info :
		case "0" : messages()


def voice_mail():
	print("Voice mailbox number")
	voice_mail = input("Press 0 to back to message menu: ")
	match voice_mail :
		case "0" : messages()


def service_command():
	print("Service command editor")
	service_command = input("Press 0 to back to message menu: ")
	match service_command :
		case "0" : messages()








		








def chat():
	print("Chat")
	chat = input("Press 0 to back to main menu: ")
	match chat :
		case "0" : main_menu()


def call_register():
	print("Call register")
	print(""" 
			CALL REGISTER MENU:
			1 -> missed calls
	   		2 -> received calls
	  		3 -> dialled numbers
			4 -> erassed call lists
			5 -> show call duration
			i -> last call cost
			ii -> All calls duration
			iii -> Received calls duration
			iv -> Dialled calls duration
			v -> clear times
			6 -> Show call cost
	  		i -> Last call cost
			ii -> All calls cost
			iii -> clear counters
			7 -> Call cost settings
			i -> call cost limit
			ii -> Show cost in
			iii -> clear counters
			8 - > Prepaid credit
					""")

	call_register = input("Press any key from 1 - 10: ")
	match call_register :
		case "1" : missed_calls()
		case "2" : received_calls()
		case "3" : dialled_numbers()
		case "4" : erased_calls_list()
		case "5" : show_call()
		case "6" : show_calls_costs()
		case "7" :  call_cost()
		case "8" : prepaid_credit()
		case _ : 
			print("You entered wrong")
			main_menu()

def missed_calls():
	print("Missed calls")
	missed_calls = input("Enter 0 to go back to Call register menu")
	match missed_calls :
		case "0" : call_register()

def received_calls():
	print("Received calls") 
	received_calls = input("Enter 0 to go back to Call register menu")
	match received_calls :
		case "0" : call_register()

def dialled_numbers():
	print("dialled Numbers") 
	dialled_number = input("Enter 0 to go back to Call register menu")
	match dialled_number :
		case "0" : call_register()

def erased_calls_list():
	print("Erased call list") 
	erased_calls = input("Enter 0 to go back to Call register menu")
	match erased_calls :
		case "0" : call_register()
			
def show_call():
	print("Show call duration")
	print(""" 
	CALL DURATION MENU
	1 -> Last call duration
	2 -> All calls duration
	3 -> Received calls duration
	4 -> Dialled calls duration
	5 -> clear timers
	6 -> back to call register
	""")

	call_duration = input("Press any key from 1 - 5: ")
	match call_duration :

		case 1 : last_call()

		case 2 : all_call()

		case 3 : receive_call()

		case 4 : dial_call()
								
		case 5 : clear_timer()

		case 6 : call_register()

		case _ : 
			print("you entered wrong")
			show_call() 

def last_call():
	print("Last call duration")
	last_call = ("Enter 0 to go call duration menu")
	match last_call :
		case "0" : show_call() 
					
def all_call():
	print("All call duration")
	all_call = ("Enter 0 to go call duration menu")
	match all_call :
		case "0" : show_call() 

def receive_call():
	print("received call duration")
	receive_call = ("Enter 0 to go call duration menu")
	match receive_call :
		case "0" : show_call() 

def dial_call():
	print("Dialled call duration")
	dial_call = ("Enter 0 to go call duration menu")
	match dial_call :
		case "0" : show_call() 

def clear_timer():
	print("Clear timer")
	clear = ("Enter 0 to go call duration menu")
	match clear :
		case "0" : show_call() 



					
						
		
def show_calls_costs():
	print("Show call cost") 
	show_cost = input("Enter 0 to go back to Call register menu")
	match show_cost :
		case "0" : call_register()

def call_cost():
	print("Call cost settings") 
	call_cost = input("Enter 0 to go back to Call register menu")
	match call_cost :
		case "0" : call_register()

def prepaid_credit():
	print("prepaid credit") 
	prepaid = input("Enter 0 to go back to Call register menu")
	match prepaid :
		case "0" : call_register()


			
	

	
	
		

def tones():
	print("Tones")
	print(""" 
			TONES MENU:

			1 -> Ringing tone
	   		2 -> Ringing volume
	  		3 -> incoming call alert
			4 -> composer
			5 -> Message alert tone
			6 -> keypad tones
			7 -> Warning and games tones
			8 -> Vibrating alert
			9 -> Screen saver
			10 -> back to main menu
	""")
	tones = int(input("Press any key from 1 - 9: "))				
	match tones :
		case "1" : ringing_tone()

		case "2" :ringing_volume()

		case "3" : call_alert()
						
		case "4" : composer()

		case "5" : message_tone()

		case "6" : keypad_tone()
									
		case "7" :game_tone()

		case "8" : viberating_alert()

		case "9" : Screen_saver()

		case "10" :  main_menu()
			
		case _ : tones()

		
		
def ringing_tone():
	print("Ringing tone")
	ringing_tone = input("Enter 0 to go back to tones menu: ")
	match ringing_tones :
		case "0" : tones()

def ringing_volume():
	print("Ringing volume")
	ringing_volume = input("Enter 0 to go back to tones menu: ")
	match ringing_volume :
		case "0" : tones()

def call_alert():
	print("Incoming call alert")
	call_alert = input("Enter 0 to go back to tones menu: ")
	match call_alert :
		case "0" : tones()

def composer():
	print("Composer")
	composer = input("Enter 0 to go back to tones menu: ")
	match composer :
		case "0" : tones()

def message_tone():
	print("Mesage alert tone")
	message_tone = input("Enter 0 to go back to tones menu: ")
	match message_tones :
		case "0" : tones()

def keypad_tone():
	print("Keypad tone")
	keypad_tone = input("Enter 0 to go back to tones menu: ")
	match keypad_tones :
		case "0" : tones()

def game_tone():
	print("game tone")
	game_tone = input("Enter 0 to go back to tones menu: ")
	match game_tones :
		case "0" : tones()

def viberating_alert():
	print("Viberating alert")
	viberating_alert = input("Enter 0 to go back to tones menu: ")
	match viberating_alert :
		case "0" : tones()

def screen_saver():
	print("Screen saver")
	Screen = input("Enter 0 to go back to tones menu: ")
	match screen :
		case "0" : tones()








			
def setting():
	print("Setting")
	print(""" 
			SETTINGS MENU:
			1 -> call settings
	   		2 -> phone Settings
	  		3 -> Security setting
			4 -> Restore factory settings
			5 -> back to main menu
				
	""")
	settings = input("Press any key from 1 - 5: ")
	match settings :
		case "1" : call_settings()
		case "2" : phone_setting()
		case "3" : security_setting()
		case "4" : factory_setting()
		case "5" : main_menu()
		case _  : 
			print("you entered wrong number")
			setting()
			


def call_settings():
	print("call setting")
	print("""
			CALL SETTING MENU:
			1 -> Automatic redial
			2 -> Speed dialing
			3 -> call waiting options
			4 -> Own number sending
			5 -> phone in line use
			6 -> Automatic answer
			7-> Back to setting menu

							
	""")
					
	call_settings = input("Press any key from 1 - 6: ")

	match call_settings :
		case "1" : automatic()
		case "2" : speed_dialing()
		case "3" :  call_waiting()
		case "4" : own_number()
		case "5" : phone_line()
		case "6" : automatic_answer()
		case "7" : setting()
		case _ : 
			print("You entered wrong number")
			call_settings()


def automatic():
	print("Automatic redial")
	auto = input("Enter 0 to go back to call setting menu: ")
	match auto :
		case "0" : call_settings()


def speed_dialing():
	print("Speed dialing")
	speed = input("Enter 0 to go back to call setting menu: ")
	match speed :
		case "0" : call_settings()


def call_waiting():
	print("Call waiting option")
	call_waiting = input("Enter 0 to go back to call setting menu: ")
	match call_waiting :
		case "0" : call_settings()


def own_number():
	print("Own number sending")
	own = input("Enter 0 to go back to call setting menu: ")
	match own :
		case "0" : call_settings()


def phone_line():
	print("Phone in line use")
	phone_in = input("Enter 0 to go back to call setting menu: ")
	match phone_in :
		case "0" : call_settings()

def automatic_answer():
	print("Automatic answer")
	automatic = input("Enter 0 to go back to call setting menu: ")
	match automatic :
		case "0" : call_settings()


def phone_setting():
	print("Phone settings")
							
	print("""
	PHONE SETTING MENU:
	1 -> Language
	2 -> cell phone display
	3 -> welcome note
	4 -> Network selection
	5 -> Lights
	6 -> Confirm SIM service actions
	7 -> Back to settings

	""")

	phone_setting = input("Press any key from 1 - 6: ")

					
	match phone_setting :
		case "1" : languages()

		case "2" : cell_phone()

		case "3" : welcome_note()
									
		case "4" : network_selection()
						
		case "5" : light()
									
		case "6" : confirm_service()
		
		case "7" : setting()
		
		case _ : 
			print("you entered wrong number :")
			phone_setting()

		
def languages():
	print("Languages")
	language = input("Enter 0 to go back to phone setting menu: ")
	match language :
		case "0" : phone_settings()


def cell_phone():
	print("Cell phone dispay")
	cell = input("Enter 0 to go back to phone setting menu: ")
	match cell :
		case "0" : phone_settings()


def welcome_note():
	print("Welcome note")
	welcome = input("Enter 0 to go back to phone setting menu: ")
	match welcome :
		case "0" : phone_settings()


def network_selection():
	print("Network Selection")
	network = input("Enter 0 to go back to phone setting menu: ")
	match network :
		case "0" : phone_settings()



def light():
	print("light")
	light = input("Enter 0 to go back to phone setting menu: ")
	match light :
		case "0" : phone_settings()


def confirm_service():
	print("Confirm service action")
	confirm = input("Enter 0 to go back to phone setting menu: ")
	match confirm :
		case "0" : phone_settings()






def security_setting():

	print("Security settings")
						   
	print("""
	SECURITY SETTING MENU:
	1 -> PIN code request
	2 -> call barring service
	3 -> Fixed dialing
	4 -> Close user group
	5 -> phone security
	6 -> Change access codes
	7 -> back to setting		
	""")

	security_setting = input("Press any key from 1 - 6: ")
					
	match security_setting :
		case "1" : pin_codes()

		case 2 : call_barring()

		case 3 : fixed_dailing()
									
		case 4 : close_user()
						
		case 5 : phone_security()
									
		case 6 : change_access() 

		case 7 : setting()
		
		case _ : 
			print("you entered wrong ") 
			seurity_setting()


def pin_code():
	print("PIN code request")
	pin = input("Enter 0 to go back to security settings")
	match pin :
		case "0" : security_setting()

def call_barring():
	print("Call barring request")
	call_barring = input("Enter 0 to go back to security settings")
	match call_barring :
		case "0" : security_setting()

def fixed_dialing():
	print("Fixed  dailing")
	fix = input("Enter 0 to go back to security settings")
	match fix :
		case "0" : security_setting()

def close_user():
	print("Close user group")
	close_user = input("Enter 0 to go back to security settings")
	match close_user  :
		case "0" : security_setting()
def phone_security():
	print("Phone seurity")
	phone_security = input("Enter 0 to go back to security settings")
	match phone_security :
		case "0" : security_setting()
def Change_access():
	print("Change access codes")
	change = input("Enter 0 to go back to security settings")
	match change :
		case "0" : security_setting()





def factory_setting():
	print("Restore factory setting")
	factory = input("Enter 0 to go back to setting menu")
	match factory :
		case "0" : setting()



	





		
		






			
def call_divert():
	print("call divert")
	call_divert = input("Enter 0 to go back to main menu:")
	match call_divert :
		case "0" : main_menu()
	
def game():
	print("game")
	game = input("Enter 0 to go back to main menu:")
	match game :
		case "0" : main_menu()

def calculator():
	print("Calulator")
	calculator = input("Enter 0 to go back to main menu:")
	match calculator :
		case "0" : main_menu()

def reminder():
	print("reminder")
	reminder = input("Enter 0 to go back to main menu:")
	match reminder :
		case "0" : main_menu()

def clock():
	print("Clock")
	print(""" 
			CLOCK MENU:
			1 -> Alarm clock
			2 -> clock settings
			3 -> date setting
			4 -> Stopwatch
			5 -> Countdown timer
			6 -> Auto update of date and time
			7 -> Back to main menu
		
	""")

	clock = input("press any key from 1 -6")

	match clock :
		case "1" : alarm()

		case "2": clock_setting

		case "3" : date()
									
		case "4" : stopwatch()
						
		case "5" : counter_timer()
									
		case "6" : auto_update()
		
		case "7" : main_menu()

		case _  : 
			print("You enter the wrong number")
			clock()
			



def alarm():
	print("Alarm clock")
	alarm = input("Enter 0 to go back to clock menu")
	match alarm :
		case "0": clock()

def clock_setting():
	print("Clock setting")
	clock_setting = input("Enter 0 to go back to clock menu")
	match clock_seting :
		case "0": clock()

def date():
	print("Date setting")
	date = input("Enter 0 to go back to clock menu")
	match date :
		case "0": clock()


def stopwatch():
	print("Stopwatch")
	stop = input("Enter 0 to go back to clock menu")
	match date :
		case "0": clock()

def counter_timer():
	print("Counter timer")
	count = input("Enter 0 to go back to clock menu")
	match count :
		case "0": clock()

def auto_update():
	print("auto update of date and time")
	update = input("Enter 0 to go back to clock menu")
	match update :
		case "0": clock()





	






def profiles():
	print("profiles")
	profiles = input("Enter 0 to go back to main menu:")
	match profiles :
		case "0" : main_menu()

	

def sim_services():
	print("SIM services")
	profiles = input("Enter 0 to go back to main menu:")
	match profiles :
		case "0" : main_menu()



	

		
main_menu()		

		
















	

	