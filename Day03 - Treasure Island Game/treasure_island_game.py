print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_one = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n").lower()

if choice_one == 'left':
    print('''
        ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
    ''')
    choice_two = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a "
                       "boat. Type 'swim' to swim across.\n").lower()
    if choice_two == 'wait':
        print('''
                     __________      __________      __________
                    |  __  __  |    |  __  __  |    |  __  __  |
                    | |  ||  | |    | |  ||  | |    | |  ||  | |
                    | |  ||  | |    | |  ||  | |    | |  ||  | |
                    | |__||__| |    | |__||__| |    | |__||__| |
                    |  __  __()|    |  __  __()|    |  __  __()|
                    | |  ||  | |    | |  ||  | |    | |  ||  | |
                    | |  ||  | |    | |  ||  | |    | |  ||  | |
                    | |__||__| |    | |__||__| |    | |__||__| |
                    |__________|    |__________|    |__________| 

        ''')
        choice_three = input("You wait for a boat to take you to the island. Once there, you are presented with three "
                             "differently coloured doors. Which do you pick: Red? Blue? or Yellow?\n").lower()
        if choice_three == "red":
            print('''
                            (  .      )
                 )           (              )
                       .  '   .   '  .  '  .
              (    , )       (.   )  (   ',    )
               .' ) ( . )    ,  ( ,     )   ( .
            ). , ( .   (  ) ( , ')  .' (  ,    )
          (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
            print("You're burned by fire. Game Over.")
        if choice_three == "blue":
            print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            ''')
            print("You are eaten by a beast. Game Over.")
        if choice_three == "yellow":
            print('''
                 __________________
               .-'  \ _.-''-._ /  '-.
             .-/\   .'.      .'.   /\-.
            _'/  \.'   '.  .'   './  \'_
            :======:======::======:======:  
            '. '.  \     ''     /  .' .'
              '. .  \   :  :   /  . .'
                '.'  \  '  '  /  '.'
                  ':  \:    :/  :'
                    '. \    / .'
                      '.\  /.'    
                        '\/'
               ''')
            print("You found the treasure, you win!")
    else:
        print('''
        
                 |
                 |
                ,|.
               ,\|/.
             ,' .V. `.
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-' ap

            ''')
        print("You are attacked by a trout! Game Over.")
else:
    print('''
                      ,,ggddY""""Ybbgg,,
                 ,agd""'              `""bg,
              ,gdP"                       "Ybg,
            ,dP"                             "Yb,
          ,dP"         _,,ddP"""Ybb,,_         "Yb,
         ,8"         ,dP"'         `"Yb,         "8,
        ,8'        ,d"                 "b,        `8,
       ,8'        d"                     "b        `8,
       d'        d'        ,gPPRg,        `b        `b
       8         8        dP'   `Yb        8         8
       8         8        8)     (8        8         8
       8         8        Yb     dP        8         8
       8         Y,        "8ggg8"        ,P         8
       Y,         Ya                     aP         ,P
       `8,         "Ya                 aP"         ,8'
        `8,          "Yb,_         _,dP"          ,8'
         `8a           `""YbbgggddP""'           a8'
          `Yba                                 adP'
            "Yba                             adY"
              `"Yba,                     ,adP"'
                 `"Y8ba,             ,ad8P"'
                      ``""YYbaaadPP""''
    ''')
    print("You fall into a hole! Game Over.")
    
    
