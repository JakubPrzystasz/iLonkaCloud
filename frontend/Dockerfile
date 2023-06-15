# Dockerfile
# Use node alpine as it's a small node image
FROM node:alpine

# Create the directory on the node image 
# where our Next.js app will live
RUN mkdir -p /front/ilonkacloud

# Set /app as the working directory
WORKDIR /front/ilonkacloud

COPY ./src/package*.json ./

RUN npm install

CMD ["npm", "run", "dev"]

# Copy package.json and package-lock.json
# to the /app working directory
# COPY package*.json /app

# Install dependencies in /app
# RUN npm install

# EXPOSE 3000

# CMD ["npm", "run", "dev"]
