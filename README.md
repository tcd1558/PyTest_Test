# PyTest_Test
A PyTest project

This is the project I created as a companion to the LinkedIn course "Unit Testing and Test Driver Development in Python"
Please read this document in raw mode

## 1 How to install pytest 

Create a new Project
Open a new file
Add the followin line

import pytest

Hover over the pytest, if it is red underlined. 
Click on install package. 

## 2 Convert a program to a pytest

In the top Menu click on Run, Edit Configurations... 
Add new Configuration, Python Tests, pytest

Name: <MyName> 
(0) Script path: <my file> 
[OK]
  
In the top right margin, to the left of the green Run triangle, click on the pull down menu and set it to <MyName>
  
## 3 Define a test

Tests are defined as function and the function name starts with 'test'
Files with tests inside should start with 'test_' or end in '_test'

If a TDD file contains test classes, the class name needs to start with 'Test'. The class can NOT have a __init__.

## 4 Setup/Teardown

def setup_module(module)    # same as suite in robot. Executed before any function. 
def teardown_module(module) # Executed after last function

def setup_function(function)
def teardown_function(function)

@classmethod
def setup_class(class)
@classmethod
def teardown_class(class)

def setup_method(self, method)
def teardown_method(self, method)

## 5 fixture
### 5.1 Setup

Simuar to Setup/Teardown
Functions get the @pytest.fixture() decorator.

import pytest

@pytest.fixture()
def setup()
  print('\nSetup')
  

def test1(setup) - notice the parameter 'setup'
  print{"test1")
  assert True

@pytest.mark.useFixtures("setup")
def test2()
  print{"test1")
  assert True
  
----
By setting autouse=True as parameter, all tests will run the setup fixture. 
@pytest.fixture(autouse=True)
  
### 5.2 Teardown

@pytest.fixture()
def setup()
  print('\nSetup')
  yield  # everything beyond the 'yield' is considered teardown code
  print('Teardown')
  
  




 

