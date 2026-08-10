---
layout: post
title: "Writing"
description: "Notes on computational chemistry, AI for science, education and academic institutions."
permalink: /writing/
---

{% assign writing_pages = site.pages | where_exp: "item", "item.path contains 'writing/'" | sort: "date" | reverse %}

{% if writing_pages.size > 1 %}
<ul class="writing-list">
  {% for item in writing_pages %}
    {% unless item.path == "writing/index.md" %}
      <li>
        <a href="{{ item.url | relative_url }}"><strong>{{ item.title }}</strong></a>
        {% if item.date %}<br><small>{{ item.date | date: "%-d %B %Y" }}</small>{% endif %}
        {% if item.description %}<br>{{ item.description }}{% endif %}
      </li>
    {% endunless %}
  {% endfor %}
</ul>
{% else %}
The writing archive is being prepared. New essays will appear here.
{% endif %}
