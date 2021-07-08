def formatDuration(seconds):
    minutes = seconds // 60
    updated_seconds = seconds % 60

    hours = minutes // 60
    updated_minutes = minutes % 60

    days = hours // 24
    updated_hours = hours % 24

    year = days // 365
    updated_days = days % 365

    if year != 0 and updated_days != 0 and updated_hours != 0 and updated_minutes != 0 and updated_seconds != 0:
        print(f"{year} year, {updated_days} days, {updated_hours} hours, {updated_minutes} minutes and {updated_seconds} seconds")

    elif year == 0 and updated_seconds == 0:
        print(f"{days} days, {updated_hours} hours and {updated_minutes} minutes")

    elif year == 0 and days == 0 and hours == 0:
        print(f"{minutes} minutes and {updated_seconds} seconds")

    elif year == 0 and updated_hours == 0:
        print(f"{days} days, {updated_minutes} minutes and {updated_seconds} seconds")

    elif year == 0 and days == 0:
        print(f"{hours} hours, {updated_minutes} minutes and {updated_seconds} seconds")


if __name__ == '__main__':

    formatDuration(62)
    formatDuration(3662)
    formatDuration(1037037)
    formatDuration(3274440)
    formatDuration(34918273)
#
# Your task is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise,
# the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:


#
# formatDuration(62)    // returns "1 minute and 2 seconds"
# formatDuration(3662)  // returns "1 hour, 1 minute and 2 seconds"
# formatDuration(1037037) // returns "12 days, 3 minutes and 57 seconds"
# For the purpose of this challenge, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
#
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc.
# In general, a positive integer and one of the valid units of time, separated by a space.
# The unit of time is used in plural if the integer is greater than 1.
#
# The components are separated by a comma and a space (", "). Except the last component,
# which is separated by " and ", just like it would be written in English.
#
# A more significant units of time will occur before than a least significant one. Therefore,
# 1 second and 1 year is not correct, but 1 year and 1 second is.
#
# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
#
# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds
# is not valid, but it should be just 1 minute.
#
# A unit of time must be used "as much as possible".
# It means that the function should not return 61 seconds, but 1 minute and 1 second instead.
# Formally, the duration specified by a component must not be greater than any valid more significant unit of time.

# // Tests
# const Mocha = require('mocha');
# const mocha = new Mocha();
# const { assert: { equal: assertEquals } } = require('chai');
#
# mocha.suite.emit('pre-require', this, 'solution', mocha);
#
# describe('formatDuration', function() {
#   it('should equal output', function() {
#     assertEquals(formatDuration(0), "now");
#     assertEquals(formatDuration(1), "1 second");
#     assertEquals(formatDuration(62), "1 minute and 2 seconds");
#     assertEquals(formatDuration(120), "2 minutes");
#     assertEquals(formatDuration(3600), "1 hour");
#     assertEquals(formatDuration(3662), "1 hour, 1 minute and 2 seconds");
#     assertEquals(formatDuration(1037037), "12 days, 3 minutes and 57 seconds");
#     assertEquals(formatDuration(3274440), "37 days, 21 hours and 34 minutes");
#     assertEquals(formatDuration(34918273), "1 year, 39 days, 3 hours, 31 minutes and 13 seconds");
#   })
# })
#
# mocha.run()
