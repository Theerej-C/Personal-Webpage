FROM node:20.16

WORKDIR /code

COPY ./package*.json .

RUN npm install

COPY . .

# RUN npm run build

EXPOSE 3000

# CMD [ "npm", "run", "dev" ]
