# Robot Framework Selenium 2 Extension Library for Table Utilities

Wait, that's too long! How about:

## RF Table Helpers

Yeah, that's a lot easier to say and remember. We'll go with that.

## About

As this is the first commit, there's not really anything to see here at the moment. However, I will be building out a set of helper functions to extend what [Robot Framework](http://robotframework.org/) can do with the [Selenium 2 Library](http://rtomac.github.io/robotframework-selenium2library/doc/Selenium2Library.html). Specifically, utility functions that allow you to introspect HTML tables to determine a column number by way of its header text, find an instance of a value within a table, etc. 

Even though there's no code at the moment, I will deliver something of substance in the weeks to come. How do I know I can do this? Because I've done this very thing before. However, what I wrote as a company-internal code base, I will be creating something new and fresh - hopefully with some lessons learned along the way. Stay tuned!

## Approach

I'll be using [the approach described in this StackOverflow answer]
(https://stackoverflow.com/questions/23703870/pass-existing-webdriver-object-to-custom-python-library-for-robot-framework/23704655#23704655). This allows you to reference this library only, and not have to reference the Selenium 2 library separately. This also makes it easier to override methods present in the existing Selenium 2 library.

## Documentation

Here's [the main repo web page](http://glmeece.github.io/RF_Table_Helpers/). Not much to look at right now.  Here's more [about Github pages](https://pages.github.com/).

Here's what you really want - [the documentation](http://glmeece.github.io/RF_Table_Helpers/rf_table_helpers.html).

## Author

Greg Meece, who has about 20 years experience in software quality assurance. I'm not the best, I'm not the brightest, but I've weathered the storms and have the scars to prove it. I hope this repo is helpful to a lot of people out there.

## Contact

For now, let's just keep it to comments/requests via GitHub. I'll figure out better ways for you to contact me later.

If you want, you can take a look at my [LinkedIn profile](https://www.linkedin.com/in/gregmeece).
