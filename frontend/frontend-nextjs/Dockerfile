# Stage 1: Build and install dependencies
FROM node:20.16 AS builder

WORKDIR /code

COPY ./package*.json .

RUN npm install --production

COPY . .

RUN npm run build

# Remove unnecessary dependencies
RUN npm prune

# Stage 2: Create the final image
FROM node:20.16

WORKDIR /code

# Copy the bundled code from Stage 1
COPY --from=builder /code/.next/ ./.next/
COPY --from=builder /code/public/ ./public/
COPY --from=builder /code/node_modules/ ./node_modules/

COPY next.config.mjs .
COPY package.json .

EXPOSE 3000

CMD [ "npm", "run", "dev" ] 
