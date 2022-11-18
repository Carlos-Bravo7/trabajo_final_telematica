FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3.10 install flask
RUN pip3.10 install dash
RUN pip3.10 install pandas
COPY pagina_principal.py /home/Escritorio/trabajo_final/pagina_principal.py
WORKDIR /home/Escritorio/trabajo_final/
EXPOSE 80
CMD python3.10 pagina_principal.py
