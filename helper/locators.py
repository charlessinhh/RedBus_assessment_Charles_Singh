from selenium.webdriver.common.by import By

class Locators:

    def __init__(self):
        self.account_button = (By.XPATH,"//span[@class='name_rb_secondary_item' and text()='Account']")
        self.login_signup_button = (By.XPATH,"//span[@class='header_dropdown_item_name' and text()='Login/ Sign Up']")
        self.signup_frame = (By.XPATH,"//iframe[@class='modalIframe']")
        self.signup_cancel_button = (By.XPATH,"//i[@class='icon-close']")

        self.help = (By.XPATH,"//span[normalize-space()='Help']")
        self.redBus_Help = (By.XPATH,"//div[contains(text(),'redBus Help')]")
        self.iframe_help = (By.XPATH,"//iframe[@src='//www.redbus.in/help?hideLayout=true']")
        self.technical_issues = (By.XPATH,"//span[normalize-space()='Technical Issues']")
        self.technical_options = (By.XPATH,"//div[@class='chip']")
        self.no_buses_found = (By.XPATH,"//div[@class='chip' and contains(text(),'No buses found')]")
        self.suggestion_block = (By.XPATH,"//div[@class='new-issutype-head']//div//div//span")
        self.no_thanks = (By.XPATH,"//div[@class='chip' and contains(text(),'No, thanks')]")

        self.src_input = (By.XPATH,"//input[@id='src']")
        self.src = (By.XPATH,"//ul[@class='sc-dnqmqq dZhbJF']//text[@class='placeHolderMainText']")
        self.src_bangalore = (By.XPATH,"//text[@class='placeHolderMainText'][normalize-space()='Bangalore']")

        self.dest_input = (By.XPATH,"//input[@id='dest']")
        self.dest = (By.XPATH, "//ul[@class='sc-dnqmqq dZhbJF']//text[@class='placeHolderMainText']")
        self.dest_koyambedu = (By.XPATH,"//text[@class='placeHolderMainText'][normalize-space()='Koyambedu']")

        self.date_text = (By.CSS_SELECTOR,".dateText")  # CSS Selector

        self.search_button = (By.XPATH,"//button[@id='search_button']")
        self.pop_up = (By.XPATH,"//div[@class='clearfix bpdpcoach-block']")
        self.ok_button = (By.XPATH,"//div[@class='w-25 fr']//span[contains(text(), 'Ok, got it')]")
        self.departure_sort = (By.XPATH,"//span[contains(text(),'Departure')]")
        self.sleeper_filter = (By.XPATH,"//ul[@class='list-chkbox']//li[2]//label[1]")

        self.total_bus_count = (By.XPATH,"//span[@class='f-bold busFound']")
        self.buses_count = (By.XPATH,"//div[@class=' new-msg']/child::span[1]")
        self.fare_sort = (By.XPATH,"//span[normalize-space()='Fare']")
        self.bus_rates = (By.XPATH,"//div[@class='fare d-block']")  # Common XPath
        self.dept_time = (By.XPATH,"//div[@class='dp-time f-19 d-color f-bold']")
        self.amenities = (By.XPATH,"//ul[@class='amenity-list clearfix']/li")

    def get_locator(self, text):
        # Create a dictionary mapping variable names to their values
        locators = {
            "account_button":self.account_button,
            "login_signup_button":self.login_signup_button,
            "signup_frame":self.signup_frame,
            "signup_cancel_button":self.signup_cancel_button,

            "help": self.help,
            "redBus_Help": self.redBus_Help,
            "iframe_help": self.iframe_help,
            "technical_issues": self.technical_issues,
            "technical_options": self.technical_options,
            "no_buses_found": self.no_buses_found,
            "suggestion_block": self.suggestion_block,
            "no_thanks": self.no_thanks,

            "src_input": self.src_input,
            "src": self.src,
            "Bangalore": self.src_bangalore,
            "dest_input": self.dest_input,
            "dest":self.dest,
            "Koyambedu": self.dest_koyambedu,
            "calendar": self.date_text,
            # "date_13": self.date_13,
            "search_button": self.search_button,
            "pop_up": self.pop_up,
            "ok_button": self.ok_button,

            "departure_sort": self.departure_sort,
            "sleeper_filter": self.sleeper_filter,

            "total_bus_count": self.total_bus_count,
            "buses_count":self.buses_count,
            "fare_sort":self.fare_sort,
            "bus_rates": self.bus_rates,
            "dept_time": self.dept_time,
            "amenities": self.amenities,
        }
        # Return the value if the text matches a variable name
        # print(f"{text} :>  {locators.get(text)}")
        return locators.get(text, "locator not found")

    def get_date_locator(self, day):
        return (By.XPATH,
                f"//div[@class='DayTiles__CalendarDaysBlock-sc-1xum02u-0 isgDNj']/child::span[contains(text(),'{day}')]")

