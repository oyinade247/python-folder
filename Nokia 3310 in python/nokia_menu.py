print("""		WELCOME TO YOUR NOKIA PHONE

		YOUR NOKIA PHONE MENU:
                  PRESS:
	    1  Phone book
	    2  messages
	    3  Chat
	    4  Call register
	    5  Tones
	    6  Settings
	    7  call divert
	    8  Games
	    9  Calulator
	    10 Reminders
	    11 Clock
	    12 Profiles
	    13 SIM service""")
      
nokia_phone = int(input("Press any key from 1 - 13: "))

match nokia_phone :
	case 1 : 
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
		""")

		phone_book = int(input("Press any key from 1 - 10: "))

		match phone_book :
			case 1 : print("Search")

			case 2 : print("Service Nos")

			case 3 : print("Add name")

			case 4 : print("Erase")

			case 5 : print("edit")
				     
			case 6 : print("Assign tone")

			case 7 : print("Send b'card")

			case 8 : 
				print("Options")

				print(""" 
				OPTION MENU
			1 -> Type of view 
			2 -> Memory Status
					""")

				options = int(input("press any key from 1 - 2: "))

				match options:
					case 1 : print("Type of view ")
					case 2 : print("Memory Status")

			case 9 : print("Speed dials")
			case 10 : print("Voice tags")


	case 2 :
		print("Messages");

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

		""")

		message_menu = int(input("Press any key from 1 - 10: "))
								
		match message_menu :
				case 1 : print("Write messsages")
					  
				case 2 : print("Inbox")

				case 3 : print("Outbox")

				case 4 : print("Picture messages")

				case 5 : print("Templates")
				     
				case 6 : print("Smileys")
				
				case 7 : 
					print("Messages")

					print( """ 
					     MESSAGES MENU
						1 -> Set 1
						2 -> common	
						""")

					messages = int(input("Press any key from 1 - 2: "))

					match messages : 
						case 1 :
							print("Set")

							print(""" 
								SET MESSAGES MENU
								1 -> Message centre number
								2 -> Mesage sent as
								3 -> Message validity
										""")
							set_messages = int(input("press any key from 1 - 3: "))

							match set_messages :
								case 1 : print(" Message centre number")

								case 2 : print("Mesage sent as")

								case 3 : print(" Message validity")

						case 2 : 
							print("common")
							
							print("""
								COMMON MENU
								1 -> delivery report
								2 -> Reply via same centre
								3 -> character report	
										""")
							common = int(input("press any key from 1 - 3: "))
							
							match common :
								case 1 : print("Delivery report")

								case 2 : print("Reply via same centre")

								case 3 : print("Character report")


	case 3 : print("Chat")
	
	case 4 : 
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

		call_register = int(input("Press any key from 1 - 10: "))
			
		match call_register :
			
			case 1 : print("missed calls")
					  
			case 2 : print("receive calls")

			case 3 : print("Dialled number")

			case 4 : print("Erased call lists")

			case 5 : 
				print("Show call duration")

				print(""" 
				CALL DURATION MENU
				1 -> Last call duration
				2 -> All calls duration
				3 -> Received calls duration
				4 -> Dialled calls duration
				5 -> clear timers
					""")

				call_duration = int(input("Press any key from 1 - 5: "))


				match call_duration :

					case 1 : print("Last call duration")

					case 2 : print("All calls duration ")

					case 3 : print("Received calls duration")

					case 4 : print("Dialled calls duration")
								
					case 5 : print("clear timers")


			case 6 : 
				print("Show call cost")

				print("""
				CALL SHOW MENU:
				1 -> last call cost
				2 -> All calls cost
				3 -> clear counters
							
				""")
				call_show = int(input("Press any key from 1 - 3: "))
			
				match call_show :
	
					case 1 : print("Last call cost")

					case 2 : print("All calls cost ")

					case 3 : print("Clear counters")


			case 7 :
				print("call cost setting")
				
				print( """
					CALL COST MENU:
					1 -> call cost limit
					2 -> Show cost in
					3 -> clear counter
							
					""")

				call_cost = int(input("Press any key from 1 - 3: "))


				match call_cost :

					case 1  : print("call cost limit")

					case 2  : print("show cost in")

					case 3  : print("Clear counters")

		
			case  8 : print("Prepaid credit")


	case 5 :
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
					
			""")
		tones = int(input("Press any key from 1 - 9: "))
						
		match tones :
			case 1 : print("Ringing tone")

			case 2 : print("Ringing volume")

			case 3 : print("Incoming call alert")
						
			case 4 : print("Composer")

			case 5 : print("Message alert tone")

			case 6 : print("Keypad tones")
									
			case 7 : print(" Warning and games tones")

			case 8 : print("Viberating alert")

			case 9 : print("Screen saver")


	case 6 : 
		print("Settings")

		print(""" 
			SETTINGS MENU:
			1 -> call settings
	   		2 -> phone Settings
	  		3 -> Security setting
			4 -> Restore factory settings
				
			""")

		settings = int(input("Press any key from 1 - 4: "))
					
		match settings :

			case 1 :
				print("call settings")

				print("""
					CALL SETTING MENU:
					1 -> Automatic redial
					2 -> Speed dialing
					3 -> call waiting options
					4 -> Own number sending
					5 -> phone in line use
					6 -> Automatic answer

							
						""")
					
				call_settings = int(input("Press any key from 1 - 6: "))

				match call_settings :
					case 1 : print("Automatic redial")

					case 2 : print("Speed dialing")

					case 3 : print("call waiting options")
									
					case 4 : print("Own number sending")

					case 5 : print("phone in line use")

					case 6 : print("Automatic answer")

						
			case  2 :
				print("Phone settings")
							
				print("""
					PHONE SETTING MENU:
					1 -> Language
					2 -> cell phone display
					3 -> welcome note
					4 -> Network selection
					5 -> Lights
					6 -> Confirm SIM service actions

						""")

				phone_setting = int(input("Press any key from 1 - 6: "))

					
				match phone_setting :
					case 1 : print("Language")

					case 2 : print("Cell phone display")

					case 3 : print("Welcome note")
									
					case 4 : print("Network selection")
						
					case 5 : print("light")
									
					case 6 : print("Confirm service action")


						                 				
			case 3 :
				print("Security settings")
						   
				print("""
				 SECURITY SETTING MENU:
				 1 -> PIN code request
				 2 -> call barring service
				 3 -> Fixed dialing
				 4 -> Close user group
				 5 -> phone security
				 6 -> Change access codes		
						""")

				security_setting = int(input("Press any key from 1 - 6: "))
					
				match security_setting :
					case 1 : print("PIN code request")

					case 2 : print("Call barring service")

					case 3 : print("Fixed dialing")
									
					case 4 : print("Close user group ")
						
					case 5 : print("phone  security")
									
					case 6 : print("Change access codes"); 

						
			case 4 : print("Restore factory settings")



	case 7 : print("Call divert")

	case 8 : print("Games")

	case 9 : print("Calculator")

	case 10 : print("Reminders")
		
	case 11 : 
		print("Clock")

		print(""" 
			CLOCK MENU:
			1 -> Alarm clock
			2 -> clock settings
			3 -> date setting
			4 -> Stopwatch
			5 -> Countdown timer
			6 -> Auto update of date and time
		
			""")
						
		clock = int(input("Press any key from 1 - 6: "))

		match clock :
			case 1 : print("Alarm clock")

			case 2 : print("Clock settings")

			case 3 : print("Date setting")
									
			case 4 : print("Stopwatch")
						
			case 5 : print("countdown timer")
									
			case 6 : print("Auto Update of date and time")
	
							  

	case 12 : print("Profiles")
	case 13 : print("SIM services")






						
				

			












		
								















		
								   


	



	
