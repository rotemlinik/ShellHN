# ShellHN

ShellHN keeps you updated with the most popular HackerNews posts! 
With this command-line tool you can watch comments on leading posts and get some cool insights about it!

## Installation
In order to run ShellHN you'll need some packages installed. We packed it in a requirements file for you, but don't worry- nothing fancy! 
most chances you already got most of them.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage
Simply run
```bash
main.py
```

## Correlation Calculation
A cool feature of ShellHN is calculating the correlation between a posts popularity to it's publish proximity to 8pm.

To make things clear, the algorithm uses the delta between the post time of publish to the closest 8pm. For example, if a post was published at 2am, it's proximity to 8pm will be 6 hours, meaning, to 8 o'clock on the day before.

By creating a table where every row represents a post by proximity to 8pm and amount of comments, I could easily calculate the correlation between the two.

I didn't find a strong correlation between the two variables, but wanted to explain where I was going with it, as I believe that's what matters.