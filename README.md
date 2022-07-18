
# Task 1 - Create a test cases
This was done in two ways:
- The first one, in Gherkin as part of the Task 2 accessible in: `tasks_1_2/features/car_renting.feature`
- The second one, in JIRA as test cases written in common language (see JIRA Xray test cases).

# Task 2 - Automation tests:
## How to set up tests:

1. Install pipenv `pip install pipenv`
2. Go to `tasks_1_2` directory
3. Run `pipenv install`

### To execute tests:
1. Run `behave -D base_url="http://qalab.pl.tivixlabs.com/"`

- Because the environment is not stable, the failed test will add a screenshot to the `tasks_1_2` directory
- 
# Task 3 - Bugs:
Reported in JIRA.


## - JIRA project details
  - **Credentials were sent on email.**
  - Board URL: https://recruitment-task.atlassian.net/jira/software/c/projects/TVXR/boards/2?selectedIssue=TVXR-13
    - Exact URL to the test repository: https://recruitment-task.atlassian.net/projects/TVXR?selectedItem=com.atlassian.plugins.atlassian-connect-plugin:com.xpandit.plugins.xray__testing-board#!page=test-repository&testPlanId=10001
    - Or as in the execution view (**IMO best for review**): https://recruitment-task.atlassian.net/plugins/servlet/ac/com.xpandit.plugins.xray/execution-page?ac.testExecIssueKey=TVXR-17&ac.testIssueKey=TVXR-14 
    - (in the top right corner are arrows to go to the next Test Case)
  - Bugs are reported to the JIRA and displayed on the board.
    - Bugs are prioritized by highest priority (in my opinion) to the lowest one.

## Troubleshooting
  - If the exact link doesn't work, go to the project and select `Testing Board` on the left side menu)
  - Or from the board go into the `Smoke tests - recruitment test cases` ticket (https://recruitment-task.atlassian.net/browse/TVXR-17), scroll down to the list of test cases and click on the arrow on the right in the first test case
