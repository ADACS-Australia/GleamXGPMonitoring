FROM nginx:latest

# Copy across the config files for Nginx and link appropriately
COPY nginx.conf /etc/nginx/nginx.conf
COPY gleam_webapp.nginx.conf /etc/nginx/sites-available/gleam_webapp.nginx.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/gleam_webapp.nginx.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]