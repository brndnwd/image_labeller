## What is this?
- This program was built to help a group of three stressed grad students quickly and accurately label a set of images for training and testing CNN image classifiers. Specifically, we were labelling street surface images with the intent of building a classifier that predicts street surface quality. 

## Did it work?
- This little program was quite rewarding to build. It was one of those scenarios where time was limited and we needed to label as many images as possible in a couple days. Having the thought that something like this would make the process much easier but not knowing if building it would actually result in overall time gain, I took a chance and started building. Turned out that I was able to finish this in a few hours. I would estimate it 10x'd our labelling speed. We labelled about 3,000 images in less than a day.

## How does it work?
- With a directory (./images) full of .jpg files, the program will successively load a randomly selected (non-labelled) images and display it within a GUI along with several radio buttons for labelling and buttons to navigate images. Results are written to csv file (results.csv).
- Our use case was to label street surface images. Radio button fields included:
	- Street Condition: Good, Crack, Pothole, etc.
	- Foreign Object: None, Car, Sewer, Person, etc.
	- Shadow: Yes, No
- GUI shows these buttons:
	- Save: write labels to file 
	- Go Back: go back to previous image to change/verify label
	- Skip: don't label this image
	- Done: exit loop, kill process

## Usage
- Just have a local directory (.images/) full of .jpg images and run
- Check requirements.txt for dependencies
- Note we needed to retain geographic location so files were named 'lat,lon.jpg'
