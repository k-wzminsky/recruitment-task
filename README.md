
# Task 1 - Create a test cases
Wasn't sure which form do you expect the test cases, that's why I prepared in two forms:
- The first one, in Gherkin as part of the Task 2 accessible in: `tasks_1_2/features/car_renting.feature`
- The second one, in JIRA Xray test management tool as test cases written in common language.


# Task 2 - Automation tests:
## How to set up tests:

1. Install pipenv `pip install pipenv`
2. Go to `tasks_1_2` directory
3. Run `pipenv install`

### To execute tests:
1. For normal run: `behave -D base_url="http://qalab.pl.tivixlabs.com/"`
2. For headless mode (without displayed browser): `behave -D base_url="http://qalab.pl.tivixlabs.com/" -D headless`

- Because the environment is not stable, the failed test will add a screenshot to the `tasks_1_2` directory

# Task 3 - Bugs:
- Reported in JIRA. Bugs are prioritized by highest priority to the lowest one (in my opinion).


### JIRA project details
  - **Credentials were sent on email.**
  - [Project board](https://recruitment-task.atlassian.net/jira/software/c/projects/TVXR/boards/2?selectedIssue=TVXR-13)
  - [Xray test repository](https://recruitment-task.atlassian.net/projects/TVXR?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.xpandit.plugins.xray__testing-board#!page=test-repository&testPlanId=10001) 
  - [Xray test execution view](https://recruitment-task.atlassian.net/plugins/servlet/ac/com.xpandit.plugins.xray/execution-page?ac.testExecIssueKey=TVXR-17&ac.testIssueKey=TVXR-14) (IMO the best view to review)
    - (in the top right corner are arrows to go to the next Test Case)
  - Bugs are reported to the JIRA and displayed on the board.
    

## Troubleshooting
  - If the link for the Xray repository doesn't work:
    - go to the project and select `Testing Board` on the left side menu)
  - If the link for Xray execution doesn't work:
    - go to the ticket [Smoke tests - recruitment test cases](https://recruitment-task.atlassian.net/browse/TVXR-17), 
    - scroll down to the list of test cases,
    - click on the arrow on the right side for the first test case
