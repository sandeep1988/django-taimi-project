import appsettings
from django import forms
register = appsettings.register('mymodule')

# settings are organized into groups.
# this will define settings
#   mymodule.story.greeting,
#   mymodule.story.pigs,
#   etc.
@register
class Story:
    # int, string, and float types are auto-discovered.
    greeting = "hello"
    pigs = 3
    wolves = 1