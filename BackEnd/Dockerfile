FROM python

# Exposing Ports
EXPOSE 5002

# Installing python dependencies
RUN pip install Flask
COPY BackEnd.py /
CMD ["python", "./BackEnd.py"]