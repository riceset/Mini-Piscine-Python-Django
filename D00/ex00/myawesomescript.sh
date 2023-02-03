# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myawesomescript.sh                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkomeno <tkomeno@student.42tokyo.jp>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/30 14:48:22 by tkomeno           #+#    #+#              #
#    Updated: 2023/02/01 17:37:41 by tkomeno          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/sh

if [ $# -ne 1 ]; then
	echo "Error: wrong number of arguments."
	exit 1
else
	curl -v $1 2>&1 | grep Location | cut -d " " -f 3
fi
