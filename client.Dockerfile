FROM node:6.14.2-slim
 
WORKDIR /app

COPY client .
RUN npm install && \
    npm install express express-jwt@5.3.3
