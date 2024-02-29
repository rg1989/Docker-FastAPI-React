FROM node:20.11.1
WORKDIR /app
COPY package*.json /app

RUN npm i --silent
COPY . ./
EXPOSE 8000

CMD [ "npm", "run", "dev"]