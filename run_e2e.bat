pip install -r requirements.txt
behave .\features\redBus_End_to_End_funtionality.feature -f allure_behave.formatter:AllureFormatter -o Report\allure-results
allure serve Report\allure-results\
