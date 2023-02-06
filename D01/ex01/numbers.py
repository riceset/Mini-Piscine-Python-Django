# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkomeno <tkomeno@student.42tokyo.jp>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:39:09 by tkomeno           #+#    #+#              #
#    Updated: 2023/02/06 13:27:08 by tkomeno          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
    with open("numbers.txt", "r") as object:
        data = object.read()
        lines = data.split(",")
        for line in lines:
            print(line.strip())

if __name__ == '__main__':
    main()
