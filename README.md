# Classifier of male and female names in Spanish
This repository contains the code created to classify names in Spanish for both men and women, singles or doubles, through the **Naive Bayes classifier**, obtaining the most important **characteristics** of each name such as: length of the name, number of vowels or character recognition; as well as the **data augmentation** technique to increase the amount of training data.

### Features

- Use the Naive Bayes classifier found in the NLTK library to train.
- Use the technique of data augmentation to have more training data.
- It incorporates various functions called "atributos" (atributos1 - atributos7) with which the user can obtain various characteristics from the names entered.
- It allows the user to enter as many names as desired until the user indicates the exit of the program.
- When entering a male and female name at the same time, it will only recognize the first name entered from left to right.

## How to use
1. Execute in the terminal the code `python3 main.py` this will train the classification model.
2. Once the model has been trained, the value of the accuracy obtained will be reported as follows: `Model Accuracy: 0.93`.
3. An interactive menu will immediately appear asking the user to enter one or two male or female names:
```python
What do you want to do?

        [P]redict name (male/female)
        [e]xit program
```
	If you want to enter a name, enter the letter `P`; if you want to exit, enter the letter `e`.

#### Example
- Try the names `Carlos` and` Laura`: A male and female names, respectively.
- If you enter the name `Carlos`, the following response will appear:

```python
Enter the name: Carlos

Name: Carlos
Prediction: male
```
