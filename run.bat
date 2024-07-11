pip install -r requirements.txt
behave ./features/redBus_help_functionality.feature -f allure_behave.formatter:AllureFormatter -o Report\allure_results
allure serve Report\allure_results
