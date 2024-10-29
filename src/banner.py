import os
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Function to display the user-defined banner
def display_banner():
    banner = r"""
                       .............
                     ,;............','.
                    :;.....  ......''c'.
                   ,c..... ...... .'.::'
                   :c ...';ccllcc;,'.,c'.
                   :c  oOKKXXXXXXXK0c.;'.
                   :c..xocldOXXkolcxx.:'.
                   ::o;ddl:;:KK;;:lOx:o'.
                   'cc;dOkOkdllxO0KXk::.
                    .:;...       ..,;'.
                     .c.       .cl.',.
                       ;;      .. ''.
                 ';.......:.    ,x'........
                .c'. .. .;looloOKKc. .. ..'
                ;c..   ,looxk0KXXXK0:'''..'.
             ...'.......'o0KKXXXXKo'....;,;;'.
           ,:..............cOKKx:...........':;..
          ;:................,..;...............,'.
          c;............... ....................'.
          c;......................'.............'.
          .''............DARK DEVIL,..............
          ,;...............;;. .......... ........
            .',........... ... ................
                ....,..... ...............
                     .,,.. ...........
                        .','.......
                            .  
    """
    print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)

# Call the display_banner function
