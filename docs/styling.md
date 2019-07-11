# Styling

## General
* Indent 4 spaces except for HTML/CSS/Javascript
* Keep horizontal code length relatively short
* Choose self-descriptive variable & function names
* Avoid writing comments within code unless it's absolutely necessary

  Note that this does not refer to docstrings and the like
  
* Most importantly, refer to the [Google Style Guides](https://github.com/google/styleguide)

## Language Specific
### HTML
* Indentation: 2 spaces
### CSS
* Indentation: 2 spaces
### Javascript
* Indentation: 2 spaces
* Run [Prettier](https://prettier.io/) on all .js files that have been edited
### Python
* Run [Pylint](https://www.pylint.org/) on all .py files that have been edited
* Should also install pylint-django using `pip install pylint-django` and 
  run it by using `pylint yourfilehere.py --load-plugins pylint_django`
