FROM nginx:latest

EXPOSE 80
EXPOSE 3000

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/nginx.conf
