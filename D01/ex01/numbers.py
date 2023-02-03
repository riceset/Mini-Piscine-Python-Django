# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkomeno <tkomeno@student.42tokyo.jp>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:39:09 by tkomeno           #+#    #+#              #
#    Updated: 2023/02/03 16:46:25 by tkomeno          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

with open("numbers.txt", "r") as object:
    data = object.read()
    lines = data.split(",")
    for line in lines:
        print(line.strip())
