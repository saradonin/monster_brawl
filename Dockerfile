FROM python:3.10-alpine

ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apk update && apk upgrade && \
    apk add git

RUN mkdir /app && \
    cd /app && \
    git clone https://github.com/saradonin/monster_brawl.git .

RUN apk del git

WORKDIR /app

CMD [ "python", "./main.py" ]

# # to build and run the game
# docker build . -t python-app
# docker run -it --name monster-brawl python-app

# # to start existing container and run the game
# docker start monster-brawl && exec -it monster-brawl python3 main.py

