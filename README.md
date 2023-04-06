## Project of automated API and combined UI with API
### Technologies used
<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Selenium" src="http://www.loadview-testing.com/wp-content/uploads/Selenium_Logo-1.png"></code>
<code><img width="5%" title="Selenoid" src="https://aerokube.com/selenoid/latest/img/og-image.jpg"></code>
<code><img width="5%" title="Requests" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
<code><img width="5%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"></code>
<code><img width="5%" title="Jira" src="https://seeklogo.com/images/J/jira-logo-C71F8C0324-seeklogo.com.png"></code>
</p>
<br> 

### The project contains two groups of tests:
<details><summary><b>'https://reqres.in/' - api tests</b></summary>
<ul>
  <li>Registration with valid email and password</li>
  <li>Registration with one email without a password</li>
  <li>Authorization check</li>
  <li>Login with one email without password</li>
  <li>Create user</li>
  <li>Delete user</li>
</ul>

</details>
<details><summary><b>'https://demowebshop.tricentis.com' - combined UI with API tests</b></summary>
<br> 
<ul>
  <li>Authorized user login</li>
  <li>Adding a Product to the Cart</li>
  <li>Checking that the product has been added to the cart</li>
  <li>Removing a product from the cart</li>
  <li>Exit from personal account</li>
</ul>
</details>
<br>

## How to start
Before execution, it is necessary:
* in .env define configuration options:
```
LOGIN = user email
PASSWORD= user password
LOCAL_DEMOQA = project url to run locally
TEST_DEMOQA = text outline project url
TEST2_DEMOQA= text outline project url
PROD_DEMOQA= url of the demo outline project
LOCAL_REQRESIN = project url to run locally
TEST_REQRESIN = text outline project url
TEST2_REQRESIN= url of text outline project
PROD_REQRESIN= url of Prod's outline project
```

### Locally
```
pytest . --env=prod
```

### Remotely
```
python -m venv .venv
source .venv/bin/activate
pip install poetry 
pytest . --env=prod || true
```


### <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> [Launch of the project в Jenkins](https://jenkins.autotests.cloud/job/qa_diplom_api/)
##### Clicking on "Build Now" will start building tests and running them on the server Jenkins.
![Jenkins_run](/images/screenshots/jenkins_configure.png)

### <img width="3%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"> Allure report
##### Based on the results of passing the tests, an Allure report is generated.
![Overview](/images/screenshots/report.jpg)

##### The Behaviors tab contains collected test cases, which describe the steps. Attachments are implemented for api methods. For combined tests, at the end of the test, a screenshot is taken and a video recording of the test is saved.
![Behaviors](/images/screenshots/behaviors.png)
![Behaviors1](/images/screenshots/behaviors1.png)

##### Video passing the test.
![This is an image](/images/screenshots/video.gif)

Logging implemented in the project:
![This is an image](/images/screenshots/logger.png)
##### Implemented integration with Allure TestOps and Jira.
![Jira](/images/screenshots/jira.png)


### <img width="3%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"> Integration with Telegram
##### At the end of the tests, send a mini report to telegram

![Telegram](/images/screenshots/notifications.png)

