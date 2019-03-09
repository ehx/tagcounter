## TagCounter
Its a web page scraper that generates basic metrics like total number of HTML elements,
the top 5 most frequently used tags, and their respective counts about any page.

#### Prerequisites
```
 python 2.7
```

#### Setup
```
clone this repo : https://github.com/ehx/tagcounter.git
```

#### How to use?
```
 python tagcounter.py [target] [number_of_tags]
```
target and number_of_tags are optionals.

by defaults:
* target = http://ordergroove.com/company
* number_of_tags = 5

example:

![script finish](https://raw.githubusercontent.com/ehx/tagcounter/master/screen.png)


#### Running the tests

```
python -m unittest test_tagcounter
`````

