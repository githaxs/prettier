FROM public.ecr.aws/lambda/python:3.8 as deps

RUN yum install -y git

RUN curl --silent --location https://rpm.nodesource.com/setup_14.x | bash -

RUN yum install -y nodejs

RUN npm install -g prettier

RUN echo 123456789123
COPY requirements.txt .
RUN python3.8 -m pip install -r requirements.txt

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]