# `rolipy` - rolimon's python interaction

`rolipy` is an **open source** python-based **rolimon's api wrapper** 
[rolimon's private api](http://rolimons.com).

## Table of Contents

* [Installation](#installation)
* [Examples](#Examples)
* [Getting started](#getting-started)
* [Documentation](#documentation)

## Examples

### Getting an item's value
```python
value = rolipy.getValue(21070012)
```
### Getting the item attributes to every item on the catalog
```python
itemdata = []

catalog = rolipy.getlimitedsCatalog(format='id')

catalogatrributes = rolipy.getitemAttributes(catalog))
```
### Getting the value, demand, acronym, trend, projected status, and hyped status of an item
```python
details = rolipy.getitemAttributes(21070012)

itemattributes = details['name'], details['acronym'], details['value'], details['demand'], details['trend'], details['projected'], details['hyped'])
```
