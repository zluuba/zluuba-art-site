# zluuba.ru

[![project-check](https://github.com/zluuba/zluuba-art-site/actions/workflows/project-check.yml/badge.svg)](https://github.com/zluuba/zluuba-art-site/actions/workflows/project-check.yml)

Simple personal website. <br/>
[www.zluuba.ru](https://zluuba.ru)


To Do:
- add personal blog on blog.zluuba.art (include the ability to publish posts remotely);
- add bookshelf (listing books I've read);


## Run Docker
```commandline
# create image
docker build -t 'website' .

# run image
docker run -p 3000:3000 'website'
```


## Plans

I want to make it right and rebuild the current website into a beautiful piece of art.

Functionality:
- admin panel for blog posts (markdown and html support);
- statistic logging;

Design:
- two color schemes: #f2f2f2 and #5c5c5c, aka soft cake cream and graphite;
- line-like glass main menu with the logo on the left and items section on the right (projects, blog, contact);
- add patterns and colors (not too much, not too colorful);

DevOps:
- tools for quick deployment (including fast updates);

Tools:
- try HTMX;
