## Prerequisites
Firstly, you will need to have installed on your local machine docker, git and some IDE. After that please clone the repository on you local machine.
Having these things, you can go on to next section.

## Main instructions
1. Open bash on your laptop, navigate to cloned project and use this command to build an image out of docker file:
```bash
docker build -t project .
```

2. After the image is built, please use this command to run a container:
```bash
docker run -it -v ${PWD}/src:/app/src -v ${PWD}/data:/app/data -v ${PWD}/data_loader:/app/data_loader --entrypoint bash project
```

That is it, the project is set up.