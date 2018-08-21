FROM python

# Exposing Ports
EXPOSE 80

# Installing python dependencies
RUN pip install Flask
RUN pip install requests
COPY FrontEnd.py /
CMD ["python", "./FrontEnd.py"]