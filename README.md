# YOLO project

## Requirements

- [poetry](https://python-poetry.org/)

## Installing

1. Clone this repo
2. `cd yolo_project`
3. Install dependencies `poetry install`
4. To work with jupyter notebook, enter the command: 

`poetry run jupyter notebook`



# Training

To get/create a training dataset, there are several ways.
Here two simple ways are introduced:

## Use roboflow platform

1. Create an account in [roboflow](https://roboflow.com/)
2. Find a sample dataset from [here](https://universe.roboflow.com/)
or
2. You can create your own dataset on the platform (but the dataset will be published for all)
3. Train a YOLO model



## Image annotation with Labelme (locally)

Even if you don't have an account, you can use the app...
In the following example I use poetry. (So you need already installed poetry...)

1. Get the codes from the github repo [labelme](https://github.com/wkentaro/labelme/tree/main)

`$ git clone https://github.com/wkentaro/labelme.git`

2. Install dependency with poetry (at first go to the directory)

```
$ cd labelme
$ poetry install
```

3. run the app 

`$ poetry run labelme`







