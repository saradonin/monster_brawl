FROM python:3.10-alpine

ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /app
WORKDIR /app
COPY . /app/

CMD [ "python", "./main.py" ]

# # to build and run the game
# docker build . -t monster-app
# docker run -it --name monster-brawl monster-app

# # to start existing container and run the game
# docker start monster-brawl
# docker exec -it monster-brawl python3 main.py

