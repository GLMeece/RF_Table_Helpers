#!/usr/bin/env python

"""
Various Selenium-related utility functions for Robot Framework, especially 
table-related functions.

- *Module*: robot_utilities
- *Platform*: Unix, Windows
- *Author*: [mailto:glmeece@gmail.com?subject=About rf_Table_Helpers.py|Greg Meece]

"""
__version__ = '0.3.0'

import os
import platform
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

# ------------------- Internal Only Functions -------------------
def _get_sel2lib():
    """== Gets Current Selenium 2 Instance from Robot Framework ==
    
    - Uses the Robot Framework API to get an object of the current Selenium 2 instance.
    - This is an internal helper function only. 
    
    == Calling ==
    
    | *Args* | [none] | |
    | *Returns* | ``object`` | An object instance of the current Selenium 2 library.
    | *Raises* | [none] | |
    """
    return BuiltIn().get_library_instance('Selenium2Library')

# ------------------ General Purpose Functions ------------------

def url_is_reachable(url, expected_response=200):
    """== Verifies URL Passed in Returns a Given Response Code ==

    - Pass in URL, and optionally an expected response code (if something other than ``200`` is expected).
    - Returns either ``True`` or ``False``.
    
    == Calling ==
    
    | *Args* | ``url`` (str) | Fully-qualified URL (including protocol). |
    | *Args* | ``expected_response`` (int) | _Optional_ return code if other than ``200``. |
    | *Returns*  |  ``boolean``  | Either True or False. |
    | *Raises*  |  exception  | Returns ``False`` on exception. |
    """
    import requests
    try:
        req_return = requests.get(url)
        if req_return.status_code == expected_response:
            return True
        else:
            return False
    except:
        return False

def highlight(element, sleep_amount=.33):
    """== Highlights (blinks) a Selenium Webdriver element ==

    - Pass in a Selenium web element, (and optionally a sleep time value).
    - Highlights the web element with the defined style for the time specified.
    
    == Calling ==
    
    | *Args* | ``element`` (object) | Selenium web object. |
    | *Args* | ``sleep_amount`` (float) | _Optional_ Fractional time amount to "hold" the highlight. |
    | *Returns* | [none] |  |
    | *Raises* | [none] |  |

    === Example in Robot ===
    
    | ${the_element} =    Get Webelement   //*[@id="theElementID"]  # Creates the actual Selenium object
    | Highlight           ${the_element}  # does the actual highlighting
    ...alternately, with specified time:
    | Highlight           ${the_element}  sleep_amount=${1.5}  # Must encapsulate float value this way
    """
    import time
    driver = element._parent
    # Make the next two variables, we can tweak the style of highlighting more easily
    back_color = "yellow"
    outline_style = "2px dotted red"
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    hilite_style = ("background: {}; border: {};").format(back_color, outline_style)
    apply_style(hilite_style)
    time.sleep(sleep_amount)
    apply_style(original_style)

# -------------------- HTML Table Functions ---------------------

def get_column_number(table_locator, col_text, loglevel='INFO'):
    """== Returns Number of Specified Column ==
    
    Returns the number of the first column found which contains the ``col_text`` string.

    - Does not require an exact match; if there is a column named ``Foobar`` and you input ``Foo`` then it will match.
    
    === Calling ===
    
    | *Args* | ``table_locator`` (str) | The table locator containing the column whose number you desire. |
    |        | ``col_text`` (str) | The string of the column you want to locate. |
    | *Returns* | ``int`` | Number of column containing string ``col_name``. |
    | *Raises* | AssertionError | If ``col_name`` cannot be found in the table specified. |

    === Example in Robot ===

    | ${column_number} =    Get Column Number    xpath=//*[@id="deviceListHeader"]    Unsafe
    """
    sel2lib = _get_sel2lib()
    locators = sel2lib._table_element_finder._parse_table_locator(table_locator, 'header')
    found_it = False
    for locator in locators:
        elements = sel2lib._element_finder.find(sel2lib._current_browser(), locator)
        counter = 0
        for element in elements:
            counter += 1
            if col_text in element.text:
                output = counter
                found_it = True
                break
    if found_it is False:
        sel2lib.log_source(loglevel)
        raise AssertionError("No column containing '{}' found in the table identified via {}!".format(col_text, table_locator))
    return output

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def does_column_with_string_exist(table_locator, col_text, loglevel='INFO'):
    """== Does Column Exists in Table Header? ==
    
    Returns ``True`` if a column is found which contains the ``col_text`` text.

    - Does not require an exact match; if there is a column named ``Foobar`` and you input ``Foo`` then it will match.
    
    === Calling ===
    
    | *Args* | ``table_locator`` (str) | The table locator containing the column you're testing for. |
    |        | ``col_text`` (str) | The string of the column you want to test for existence. |
    | *Returns* | ``Boolean`` | Returns ``True`` if found; elsewise ``False``. |
    | *Raises* | [none] | |

    === Example in Robot ===

    | ${column_exists} =  Does Column with String Exist    xpath=//*[@id="deviceListHeader"]    Unsafe
    """
    sel2lib = _get_sel2lib()
    locators = sel2lib._table_element_finder._parse_table_locator(table_locator, 'header')
    found_it = False
    for locator in locators:
        elements = sel2lib._element_finder.find(sel2lib._current_browser(), locator)
        for element in elements:
            if col_text in element.text:
                found_it = True
                break
    return found_it

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

def _main():
    """== Runs Some the Embedded Routines as a Crude Test ==
    """
    import os
    print "This module (" + os.path.basename(__file__) + ") has been called directly."

    # Put some test calls here to make sure it's working...OK?
    print "Testing connectivity to Google..."
    reponse_eval = url_is_reachable('http://www.google.com')
    print "The result was {}".format(reponse_eval)

    # More tests to come...

if __name__ == '__main__':
    _main()
