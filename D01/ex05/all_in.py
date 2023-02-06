# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkomeno <tkomeno@student.42tokyo.jp>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 15:09:12 by tkomeno           #+#    #+#              #
#    Updated: 2023/02/06 16:00:19 by tkomeno          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

def get_inputs(argv):
    inputs = argv[1].split(',')

    res = []

    for item in inputs:
        res.append(item.strip())

    return res

def remove_empty(inputs):
    inputs = list(filter(None, inputs))
    return (inputs)


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

    inputs = remove_empty(get_inputs(argv))

    capitals_as_key = []
    states_as_key = []

    for key in states:
        capitals_as_key.append({capital_cities[states[key]]:key})
        states_as_key.append({key:capital_cities[states[key]]})

    for input in inputs:
        continue_flag = False
        found = True
        for dict in capitals_as_key:
            if input.title() in dict:
                print(f"{input} is the capital of {dict[input.title()]}")
                continue_flag = True
            else:
                found = False
        for dict in states_as_key:
            if input.title() in dict:
                print(f"{dict[input.title()]} is the capital of {input}")
                continue_flag = True
            else:
                found = False
        if continue_flag:
            continue
        if not found:
            print(f"{input} is neither a capital city nor a state")

if __name__ == '__main__':
    main()
