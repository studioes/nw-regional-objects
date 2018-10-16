# nw-regional-objects
Generate network objects by countries for CISCO configuration.

CC:Country Code

object network country-CC-nnnnn

 subnet IP mask

...

object-group network country-group-CC

 network-object object country-CC-nnnnn

When you want to block country code ZZ:

access-list fw-rule extended deny ip object-group country-ZZ

