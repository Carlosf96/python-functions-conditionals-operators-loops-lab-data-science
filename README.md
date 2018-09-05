
# Conditionals, Loops, Operators, Functions: Bringing It All Together

We've learned about a lot of statements we have available to us in Python to write more dynamic and concise code. Conditionals let us create *conditions* that inform our code how to operate. Loops help us to dynamically iterate through and operate on a collection (i.e. a list or a dictionary). And Operators, generally, allow us to compare elements to each other, assert the sameness of elements, or return elements based on their truthiness or falsiness. Functions, essentially, help us to create an object that packages up one or more operations and allows us to execute those operations from anywhere else in scope in our code. However, as we can tell by the title of this lesson, we will now be focusing on using all of these smaller parts together. As we get further into our lives as programmers, we will find ourselves facing more and more complex problems and to solve those we will need these types of tools to create solutions while keeping our code concise and efficient. 

## Objectives:
* Identify how and when to use functions, conditionals, loops, and operators
* Use functions, conditionals, loops, and operators efficiently and effectively

## Instructions

In this lab, we will be working with a dataset containing information from some of the largest Python-focused Meetup groups in the US. Our data is in the groups_db.py file, which we are importing below and as the variable `data`. You can also see an example of what the element's datastructure looks like by running the cell with `data[0]`.

To pass the tests in this lab, create functions that perform the operations indicated and have the correct return value.


```python
from groups import data
```


```python
data[0]
```

Let's say we would like to have a way to find all groups in the city we're in or perhaps the city we might want to visit, to make sure we can find a python group to join. 

Below, replace the `pass` statement with your code. The `groups_in_city` function takes in two arguments; the list of meetup dictionary objects, `data`, and a string representing a city's name. It should return only a list of dictionary's whose `city` attribute points to a string with the same name as the city name passed in as the second argument.


```python
def groups_in_city(list_of_groups, city_name):
    pass
```

Similarly, we will probably want to make sure the groups we are looking at joining have a sizeable membership so that we have a bigger network or even a more active schedule of events. 

Below, replace the `pass` statement with your code. The `groups_with_x_members` function takes in two arguments; the list of meetup dictionary objects, `data`, and an integer representing the minimum number of members in a group. It should return a list of dictionaries that have the same or greater number of members.


```python
def groups_with_x_members(list_of_groups, num_members):
    pass
```

Another way we might want to narrow our search down for groups might be to decide how diverse of topics it covers. Maybe we might be interested in groups that have events that talk about more than **just** Python.

Below, replace the `pass` statement with your code. The `groups_with_x_num_topics` function takes in two arguments; the list of meetup dictionary objects, `data`, and an integer representing the minimum number of topics a group lists. It should return a list of dictionaries that have the same or greater number of topics listed.


```python
def groups_with_x_num_topics(list_of_groups, num_topics):
    pass
```

Alright, so trying to brute force diversity of topic might have some value, but when we finally do have a group we want to take a look at, we probably want to have a way to make sure that the topics that the group lists are still *actually* of interest to us. So, let's create a function that will iterate through the a *single* group and return a list of names for each of the topics listed for that group.

Below, replace the `pass` statement with your code. The `list_group_topics` function takes in one argument, a group dictionary. It should return a list of strings that are the `name` of each topic for that group.


```python
def list_group_topics(group):
    pass
```

Great! Now we have an easy way to check if a group has the topics we're interested in. What about just taking stock of all the groups we are currently looking at. We might want to get an idea of what the most popular topics are before we decide whether we're *not interested* in certain topics. 

Below, replace the `pass` statement with your code. The `find_topic_popularity` function takes in one argument, the list of meetup dictionary objects, `data`. It should return a single dictionary that has a key for each **topic** listed for all groups in the list. Each key should point to the number of times that topic appears in the dataset. For example, if `Python` appears in 15 groups, there would be a key `'Python'` that has a value of 15. 


```python
def find_topic_popularity(list_of_groups):
    pass
```

The previous couple functions definitely feel very useful but perhaps we actually want to be able to filter for groups  that contain the topic we would like to look for.

Below, replace the `pass` statement with your code. The `find_groups_containing_topic` function takes in twp arguments; the list of meetup dictionary objects, `data`, and the name of the topic. It should return all groups that contain topics with a matching name.


```python
def find_groups_containing_topic(list_of_groups, topic_name):
    pass
```

Okay, another, perhaps most obvious way of narrowing down our search would be to find groups above a certain `rating`. 

Below, replace the `pass` statement with your code. The `filter_groups_by_rating` function takes in two arguments; first a list of dictionaries for each group, and second a minimum rating. The function should return a list of groups with a rating greater than or equal to the rating passed in.


```python
def filter_groups_by_rating(list_of_groups, min_rating):
    pass
```

## Summary

In this lab, we practiced writing functions that used conditionals, operators, and loops to select, operate on, and return the information we wanted from our dataset.
