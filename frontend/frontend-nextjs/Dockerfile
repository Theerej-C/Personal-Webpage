FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN chown -R 1001:1001 . 

RUN useradd -ms /bin/false app  
USER app

EXPOSE 3000

CMD [ "npm", "run", "dev" ]