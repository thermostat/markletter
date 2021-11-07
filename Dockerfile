
FROM pandoc/latex:2.16.1

RUN apk add python3 py3-pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD https://mirrors.ctan.org/macros/latex/contrib/footmisc.zip .

RUN unzip footmisc.zip && cd footmisc && latex footmisc.ins && latex footmisc.dtx && cp footmisc.sty /opt/texlive/texmf-local/tex/ && mktexlsr

