# Lab: Intro to Django
## Overview
The first words you see on the Django website are

**Django makes it easier to build better Web apps more quickly and with less code.**

The next quote you’ll see is

**The web framework for perfectionists with deadlines.**

In this class we’ll build out a small, but functional, multi page web site using Django.

We’ll get a feel for the “Django Way” and see the dramatic performance gains you can get with a mature, robust framework.

## Feature Tasks and Requirements
- Create web site in Django with 2 pages
    - home page
    - about page
    - create views/urls/templates as needed for home and about pages
    - use ancestor template to contain navigation elements
    - Should be built the “Django way” aka match the structure of in-class demo

## Implementation Notes
- Typical Steps to Start Django Project
    -create project
    - define app
    - add app to project
    - add views
    - add urlpatterns
    - dd templates
    - add tests

## User Acceptance Tests
- Use Django’s built in testing tools
    - Test that **home** and **about** url status codes
    - Test **home** and **about** url template use, including ancestor template.

## Configuration
- create a Github repo named django_intro
- create a new Django driven website
- create folder candy_site
- create django application named candy_project
- create django app named snickers
    - Note: replace candy, snickers etc. with names of your choice but keep django_intro name

Use poetry to initialize project folder.

```
> $ cd `django_intro`
> $ poetry init -n
> $ poetry add django
> $ poetry add --dev black
> $ poetry shell
```
