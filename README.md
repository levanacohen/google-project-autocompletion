# Google Project AutoCompletion (ExcellenTeam Bootcamp)
Introduction:
In order to improve the user experience of the Google search engine, the development team decided to allow the completion of sentences from articles, documentation and information files on various technological topics.
## The Task:
A program that supports two main functions: 1: Initialization function - The purpose of the function is to get a list of text sources on which the search engine will run, each source contains a collection of sentences. 2: Completion function - the function must get a string - which is the text that the user typed - the function must return the five best completions.
## Our solution:
Keep in a tree the full text, where each node represents a letter (and has at most 26 sons), and each sentence is a path in the tree. So we got a very fast run time and we did not have to save all the possibilities that the user will type (include mistakes).
## Libraries/Technologies Used:
* python 3.7
* VS code
* Google colab
