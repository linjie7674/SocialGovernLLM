FROM python

WORKDIR /SocialGovernLLM

COPY . /SocialGovernLLM

RUN pip3 install -r requirements.txt