# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myawesomescript.sh                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkomeno <tkomeno@student.42tokyo.jp>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/30 14:48:22 by tkomeno           #+#    #+#              #
#    Updated: 2023/01/30 14:54:00 by tkomeno          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if [ $# -ne 1 ]; then
	echo "Error: wrong number of arguments."
	exit 1
else
	curl -v $1 2>&1 | grep Location | cut -d " " -f 3
fi
