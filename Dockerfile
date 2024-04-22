FROM python
WORKDIR /Script
COPY . /Script
RUN pip install --no-cache-dir nltk
CMD ["python3","Script.py"]    