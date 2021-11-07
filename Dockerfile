
# Dockerfile for makeletter, built on top of pandoc
FROM pandoc/latex:2.16.1

LABEL author="Dan Williams (dww@pyrento.net)"

# makeletter needs python3, and the pip reqs listed
RUN apk add python3 py3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# pandocs alpine install doesn't include footmisc,
# add it back
ADD https://mirrors.ctan.org/macros/latex/contrib/footmisc.zip .
RUN unzip footmisc.zip && \
    cd footmisc && \
    latex footmisc.ins && \
    latex footmisc.dtx && \
    cp footmisc.sty /opt/texlive/texmf-local/tex/ && \
    mktexlsr

RUN mkdir /makeletter-0.2
COPY build_letter.py /makeletter-0.2

ENTRYPOINT ["python3", "/makeletter-0.2/build_letter.py"]

CMD [""]

