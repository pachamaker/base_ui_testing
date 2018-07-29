# Basic Architecture of UI Autotests
This basic architecture automated tests that can help you to create your own framework.

At the base are:
* [pytest](http://doc.pytest.org/en/latest/)
* [PageObject](https://martinfowler.com/bliki/PageObject.html)
* [Selenium](http://www.seleniumhq.org/)
* [Yandex Allure](http://allure.qatools.ru/)

## Running tests by Category
You can use pytest fixture for add category to your test, for example:
```python
@pytest.mark.categories(component='logo', suite='smoke', country=['ru','uk'])
```
So test, which has component=log and country=ru, will be found via pytest, other tests will be skipped.
This tests can be running via command
```bash
py.test --categories "component=logo,country=ru"
```

## Reporting
We will be use [Allure reporting](http://allure.qatools.ru/), because it is informative report and it is easy to integrate.
Run pytest with additional parameter alluredir. In this folder allure will be generating XML and other files.
```bash
py.test --alluredir ./var
```
For generating allure report locally, you can use [Allure Commandline](http://wiki.qatools.ru/display/AL/Allure+Commandline)
Generate & open report:
```bash
allure generate ./var
allure report open
```



## Requirements
Python 3.5
