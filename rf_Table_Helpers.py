#!/usr/bin/env python
"""
Selenium-related utility functions for Robot Framework, especially 
table-related functions.

- *Module*: rf_Table_Helpers
- *Platform*: Unix, Windows
- *Author*: [mailto:glmeece@gmail.com?subject=About rf_Table_Helpers.py|Greg Meece]

"""
__version__ = '0.4.0'

from robot.api.deco import keyword

import os
import requests

# from robot.libraries.BuiltIn import BuiltIn
# from robot.api import logger


class Plugin(LibraryComponent):

    def __init__(self, ctx):
        self.ctx = ctx

    # ------------------- Internal Only Functions -------------------

    # def _get_sel_lib():
    #     """== Gets Current Selenium Library Instance from Robot Framework ==

    #     - Uses the Robot Framework API to get an instance of the current Selenium library.
    #     - This is an internal helper function only.

    #     == Calling ==

    #     | *Args* | [none] | |
    #     | *Returns* | ``object`` | An object instance of the current Selenium 2 library.
    #     | *Raises* | [none] | |
    #     """
    #     return BuiltIn().get_library_instance('SeleniumLibrary')

# ------------------ General Purpose Functions ------------------

    @keyword
    def URL_is_reachable(self, url, expected_response=200):
        """== Verifies URL Passed in Returns a Given Response Code ==
    
        - Pass in URL, and optionally an expected response code (if something other than ``200`` is expected).
        - Returns either ``True`` or ``False``.
        
        == Calling ==
        
        | *Args* | ``url`` (str) | Fully-qualified URL (including protocol). |
        | *Args* | ``expected_response`` (int) | _Optional_ return code if other than ``200``. |
        | *Returns*  |  ``boolean``  | Either True or False. |
        | *Raises*  |  exception  | Returns ``False`` on exception. |
    
        === Example in Robot ===
        
        | ``${is_reachable} =    URL is Reachable   https://www.google.com``
        """
        try:
            req_return = requests.get(url)
            if req_return.status_code == expected_response:
                return True
            else:
                return False
        except:
            return False

    @keyword
    def highlight(self, element, sleep_amount=.33):
        """== Highlights a Selenium Webdriver element ==
    
        - Pass in a Selenium web element (and, optionally, a sleep time value).
        - Highlights the web element with the defined style for the time specified.
        
        == Calling ==
        
        | *Args* | ``element`` (object) | Selenium web object. |
        | *Args* | ``sleep_amount`` (float) | _Optional_ Fractional time amount to "hold" the highlight. |
        | *Returns* | [none] |  |
        | *Raises* | [none] |  |
    
        === Example in Robot ===
        
        | ``${the_element} =    Get Webelement   //*[@id="theElementID"]``  # Creates the actual Selenium object
        | ``Highlight           ${the_element}``  # does the actual highlighting
        ...alternately, with specified time:
        | ``Highlight           ${the_element}  sleep_amount=${1.5}``  # Must encapsulate float value this way
        """
        import time
        driver = self.driver.element._parent
        # Make the next two variables, we can tweak the style of highlighting more easily
        back_color = "yellow"
        outline_style = "2px dotted red"

        def apply_style(s):
            driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);", element,
                s)

        original_style = element.get_attribute('style')
        hilite_style = (f"background: {back_color}; border: {outline_style};")
        apply_style(hilite_style)
        time.sleep(sleep_amount)
        apply_style(original_style)

    # -------------------- HTML Table Functions ---------------------

    @keyword
    def get_column_number(self, table_locator, col_text, loglevel='INFO'):
        """== Returns Number of Specified Column ==
        
        Returns the number of the first column found which contains the
        ``col_text`` string.
        - Returns the first column encountered that matches string.
        - Does not require an exact match; if there is a column named ``Foobar``
          and you input ``Foo`` then it will match.
        - Throws an assertion of the column does not exist. If this is the desired
          behavior, the log will show the error. If you want to 'preflight' before
          calling, it is suggested you call `Does Column Exist` first.
        
        === Calling ===
        
        | *Args* | ``table_locator`` (str) | Table locator containing the column. |
        | | ``col_text`` (str) | The text of the column you want to locate. |
        | | ``loglevel`` (str) | _Optional_ Log level default is ``INFO`` |
        | *Returns* | ``int`` | Number of column containing string ``col_name``. |
        | *Raises* | AssertionError | If ``col_name`` cannot be found in table. |
    
        === Example in Robot ===
        | ``${col_num}    Get Column Number    //*[@id="dataTable"]    Phone``
        """
        found_it = False
        counter = 0  # incrementing through table columns
        output = 0  # if we fail to find it, we return a zero (which doesn't exist)
        sel_lib = self.driver

        locators = sel_lib.find_elements(table_locator + '//table//th')
        for locator in locators:
            counter += 1
            if col_text in locator.text:
                found_it = True
                output = counter
                break
        if found_it is False:
            sel_lib.log_source(loglevel)
            assert_msg = f"≻ No column containing '{col_text}' found in the table located via '{table_locator}'!"
            raise AssertionError(assert_msg)
        return output

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

    @keyword
    def does_column_exist(self, table_locator, col_text):
        """== Does Column Exist in Table Header? ==
        
        Returns ``True`` if a column exists which contains the ``col_text`` string.
        - Does not require an exact match; if there is a column named ``Foobar``
          and you input ``Foo`` then it will match.
        
        === Calling ===
        
        | *Args* | ``table_locator`` (str) | Table locator with the column you're testing for. |
        |        | ``col_text`` (str) | The string of the column you want to test for existence. |
        | *Returns* | ``Boolean`` | Returns ``True`` if found; elsewise ``False``. |
        | *Raises* | [none] | |
    
        === Example in Robot ===
        | ``${col_exists}    Does Column Exist    //*[@id="dataTable"]    Phone``
        """
        sel_lib = self.driver
        locators = sel_lib.find_elements(table_locator + '//table//th')
        found_it = False
        for locator in locators:
            if col_text in locator.text:
                found_it = True
                break
        return found_it


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~


def _main():
    """== Runs Some the Embedded Routines as a Crude Test ==
    """
    print(f"Module '{os.path.basename(__file__)}' was called directly.")

    # Put some test calls here to make sure it's working...OK?
    # print("Testing connectivity to Google...")
    # reponse_eval = URLO_is_reachable('http://www.google.com')
    # print(f"The result was {reponse_eval}")

    # More tests to come...


if __name__ == '__main__':
    _main()
