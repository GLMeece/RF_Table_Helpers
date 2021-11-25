# Robot Framework Selenium Table Utility Extension Library

Wait, that's too long! How about just:

## Table Helpers

Yeah, that's a lot easier to say and remember. We'll go with that.

## About

This a set of helper functions to extend what [Robot Framework](http://robotframework.org/) can do with the [Selenium Library](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html). Specifically:

- `url_is_reachable` - Lets you determine if a URL is routable from the executing machine.
- `highlight` - Given an element, highlights for the specified amount of time (good for visual vetting)
- `get_column_number` - Pass in a string, find the column number that matches
- `does_column_with_string_exist` - Pass in a string, determine if a column text matches

## Approach

I'll be using [the approach described in this StackOverflow answer](https://goo.gl/TFPc2Q). This allows you to reference this library only, and not have to reference the Selenium Library separately. This also makes it easier to override methods present in the existing Selenium Library.

## Documentation

Here's [the main repo web page](http://glmeece.github.io/RF_Table_Helpers/). Not much to look at right now.

Here's what you really want - [the library documentation](http://glmeece.github.io/RF_Table_Helpers/rf_table_helpers.html).

If you want to regenerate the docs locally, just execute: `./create_docs.sh`

## Author

Greg Meece, who has about 24+ years experience in software quality assurance. I'm not the best, I'm not the brightest, but I've weathered the storms and have the scars to prove it. I hope this repo is helpful to a lot of people out there.

## Contact

For now, let's just keep it to comments/requests via GitHub. I'll figure out better ways for you to contact me later.

If you want, you can take a look at my [LinkedIn profile](https://www.linkedin.com/in/gregmeece).
