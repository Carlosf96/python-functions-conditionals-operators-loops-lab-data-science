import pytest
from ipynb.fs.full.index import data, groups_in_city, groups_with_x_members, groups_with_x_num_topics, list_group_topics, find_topic_popularity, find_groups_containing_topic, filter_groups_by_rating

def test_groups_in_city():
    assert len(groups_in_city(list_of_groups, "Yonkers")) == 1
    assert len(groups_in_city(data, 'New York')) == 62
    assert len(groups_in_city(data, 'brooklyn')) == 7

def test_groups_with_x_members():
    assert len(groups_with_x_members(data, 10)) == 198
    assert len(groups_with_x_members(data, 100)) == 168
    assert len(groups_with_x_members(data, 1000)) == 78
    assert len(groups_with_x_members(data, 10000)) == 8

def test_groups_with_x_num_topics():
    assert len(groups_with_x_num_topics(data, 10)) == 151
    assert len(groups_with_x_num_topics(data, 15)) == 76
    assert len(groups_with_x_num_topics(data, 4)) == 196

def test_list_group_topics():
    assert list_group_topics(data[4]) == ['Linux', 'Apache', 'PHP', 'Open Source', 'Web Design', 'MySQL', 'Ruby', 'Python', 'Software Development', 'LAMP', 'Web Technology', 'Drupal', 'Django', 'Web Development', 'Ruby On Rails']
    assert list_group_topics(data[100]) == ['Open Source', 'Python', 'JavaScript', 'Web Development', 'Hadoop', 'Mobile Development', 'Computer programming', 'Software Architecture', 'UX Design', 'APIs', 'UI Design', 'Distributed Systems', 'Backend', 'Spotify Apps', 'Frontend Performance']
    assert list_group_topics(data[75]) == ['Mac', 'Open Source', 'Web Design', 'Python', 'Software Development', 'Web Technology', 'Technology', 'Web Development', 'iPhone', 'Business Strategy', 'Ruby On Rails', 'Agile Project Management', 'Selenium', 'Software QA and Testing', 'Test Automation']

def test_find_topic_popularity():
    data_obj = find_topic_popularity(data)
    assert data_obj['python'] == 198
    assert data_obj['web development'] == 73

def test_find_groups_containing_topic():
    assert len(find_groups_containing_topic(data, 'open source')) == 93
    assert len(find_groups_containing_topic(data, 'machine learning')) == 49
    assert len(find_groups_containing_topic(data, 'neural networks')) == 7

def test_filter_groups_by_rating():
    assert len(filter_groups_by_rating(data, 4.9)) == 40
    assert len(filter_groups_by_rating(data, 4.3)) == 152
    assert len(filter_groups_by_rating(data, 4.7)) == 90
