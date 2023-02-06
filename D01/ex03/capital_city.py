# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkomeno <tkomeno@student.42tokyo.jp>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 13:30:35 by tkomeno           #+#    #+#              #
#    Updated: 2023/02/06 15:05:42 by tkomeno          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

def main():

    if len(argv) != 2:
        return

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    
    list = []

    for key in states:
        list.append({key:capital_cities[states[key]]})

    input_state = argv[1].title()

    for dict in list:
        if input_state in dict:
            print(dict[input_state])
            return 

    print("Unknown state")

if __name__ == '__main__':
    main()
