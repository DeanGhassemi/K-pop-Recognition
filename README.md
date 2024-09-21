# K-pop-Recognition

## Inspiration
When I first got into K-pop, it was only for the music. Then I slowly transitioned into getting to know the members of the groups I liked the most. As someone who is new into K-pop, it is hard getting to know who is who when some groups have over 4 members. And even as someone who has been enjoying the music for over 5 years, I struggle to recognize the differences in groups with over 9 members (especially with the style concepts of each release for singles, eps, or albums).\
[WJSN](https://en.wikipedia.org/wiki/WJSN) has 10 members\
[Iz*One](https://en.wikipedia.org/wiki/Iz*One) had 12 members\
[TripleS](https://en.wikipedia.org/wiki/TripleS) has 24 members!

## Starting Point
I have always been interested in facial recognition and had prior knowledge of python. This [video](https://youtu.be/535acCxjHCI?si=ukcc0JfOT3GHT4hr) by Sentdex gave me an amazing starting point and understanding of how to use the face recognition library along with opencv and os.

## Features
So far it is only working with [NewJeans](https://en.wikipedia.org/wiki/NewJeans). Before I add more groups, I want to make it more precise.

## Plans
I want to add more groups, incorporate scikit-learn to make it more precise, turn it into a full developed web app so others can upload their own images and have those analyzed for recognition.

## Technical Challenges
I am attempting to find ways to optimize face-recognition without using extensive amount of training data. Sometimes, a app will recognize everyone as the same person. I made a hotfix where if a member has already been used to label a face, then that member cannot be used once again. The issue with this approach is that all faces do not get labelled. I am currently working on fixing that too. I'm thinking of comparing and switching based on which face encoding is more accurate. 
## Demo Image

![How it looks currently](https://github.com/DeanGhassemi/K-pop-Recognition/blob/main/demo-images/Screenshot%202024-09-19%20at%2010.02.25%E2%80%AFAM.png)
