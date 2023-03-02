# Eye-tracking-Data-Analyser
A simple Python program to develop eye-tracking data analyser for people with autism.

Autism Spectrum Disorder (ASD) is a neurodevelopmental disorder characterised by differences in
communication and social interaction, and previous research studies show that people with autism
tend to have different processing strategies (Eraslan et. al. 2019). In this assignment, I developed
an application that analyses the eye-tracking data of people with and without autism recorded while
they are viewing images.

Eye tracking is the process of recording where people look at and how long they look at a particular
spot. When people view images, their eyes become relatively stable at certain points called fixations,
and the series of these fixations show their scan paths. Eye-tracking data recorded on an image is
typically analysed based on the elements of the image, especially for identifying which elements are
frequently used, and in which order. Figure 1 shows a scan path of a person on an image segmented
into its elements where his/her fixations are represented as circles and the elements are represented
by red boxes.

![image](https://user-images.githubusercontent.com/90095338/222381394-217bdd32-7130-42b4-9f18-a574d26c7af5.png)

The application that you will develop in this assignment will process the txt data files in the following
format. There will be two data files for an image – one for people with autism, and another one for
people without autism. The data file includes the fixations of multiple people for a specific image.
Please note that each zero (Idx) shows the first fixation of a different person.

![image](https://user-images.githubusercontent.com/90095338/222381514-b3fc79ed-cd1f-48d4-9afd-4fc4c854cbd7.png)

![image](https://user-images.githubusercontent.com/90095338/222381585-42921d41-679c-4583-8e13-704a826e895e.png)

![image](https://user-images.githubusercontent.com/90095338/222381790-6f0a2607-1f6f-4f37-9e28-1f1a91d4dd1c.png)

![image](https://user-images.githubusercontent.com/90095338/222381895-3bbb42d8-61a4-4be0-bdcf-8660fd6bfc6e.png)


Studier approaches: primitive types, variables, operators, decision making, loops, sequences, dictionaries, functions, modules, regular expressions,
exception handling, command line arguments, and file processing

** İt should be runned in the console as the following command --> main.py asd.txt control.txt 1200x900 3x2

** ASD file belongs to people with Autism and CONTROL file belongs to people without Autism.
