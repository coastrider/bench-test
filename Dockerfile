FROM python:3.6
WORKDIR /usr/src/benchtest
RUN git clone https://github.com/coastrider/bench-test.git /usr/src/benchtest \
&& pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./run.py" ]
