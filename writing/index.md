---
layout: page
title: Writing
eyebrow: Notes and essays
description: Writing on computational chemistry, scientific machine learning, research practice, education and academic institutions.
permalink: /writing/
kind: archive
---

{% assign articles = site.pages | where: "kind", "article" | sort: "date" | reverse %}

{% if articles.size > 0 %}

<ol class="writing-list">
  {% for item in articles %}
    <li>
      <time datetime="{{ item.date | date_to_xmlschema }}">{{ item.date | date: "%-d %B %Y" }}</time>
      <div>
        <h2><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h2>
        {% if item.description %}<p>{{ item.description }}</p>{% endif %}
      </div>
    </li>
  {% endfor %}
</ol>
{% else %}
The first essays are being prepared.
{% endif %}
