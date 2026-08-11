---
layout: post
title: "A Small Piece of the Web of Your Own"
date: 2026-08-11
description: "A personal history of academic website making—from HTML and Drupal to Hugo, GitHub Pages and AI—and why academics should have a space of their own on the web."
permalink: /writing/a-small-piece-of-the-web-of-your-own/
kind: article
---

Somehow, websites have always interested me. Not necessarily because there was a great deal to say on them, but because making them was enjoyable. The difficult part was usually the content. Writing pages about oneself, updating achievements, maintaining publication lists, and periodically deciding what deserved to remain on the site never came naturally. Building the site was much more interesting than feeding it.

That probably explains why several early websites followed the same pattern. Whenever a free hosting service, a new platform, or an interesting web technology appeared, a website would get created. Considerable enthusiasm went into getting the layout right and understanding how things worked. Then the updates became less frequent, the content grew old, and eventually the site met a natural death. This happened more than once.

The interest in the technology, however, stayed.

At IISc Bangalore, that interest became more serious when a fresh website had to be created for my supervisor and the research group. This was the period when making a website meant sitting with HTML and CSS and understanding what each part of the code did. If a menu behaved badly or an image appeared in the wrong place, the solution usually involved finding the relevant line and figuring out why.

The website was built more or less from scratch. The learning was not systematic: a problem would arise, a solution would be sought, something would be changed, another part would break, and the cycle would continue. But that way of learning had an advantage. The relationship between what appeared in the browser and what existed in the source code became very clear.

Later, at IIT Kharagpur, the problem changed. A departmental website is not simply a larger personal webpage. It has to accommodate faculty, students, courses, research areas, facilities, notices and administrative information, preferably in a form that more than one person can maintain.

Drupal became the solution.

Once it was properly configured, building a fairly standard institutional website was not particularly difficult. Getting there required learning enough about servers, databases, themes, modules, permissions and content management to keep everything running. Around the same period, there were other experiments too, including a MediaWiki installation and a small microblogging service. None of this was part of a planned journey into web development. They were simply useful problems that required learning enough technology to solve them.

The next personal website went in almost the opposite direction.

Hugo was attractive because it removed much of the machinery. Content could be written in Markdown; a few desktop commands generated the complete site, and the resulting static pages could be published. No database, no complicated administration interface. For a personal academic website, it felt sufficient.

It also exposed the old problem rather efficiently. Once building the website became easy, the remaining work was writing and maintaining the content.

Toward the end of the IIT Kharagpur period, the website began moving to GitHub Pages. Initially this was not a major change in the workflow. Hugo still generated the pages locally; GitHub simply became the place from which they were served. But there was an important difference. The website no longer had to depend on an institutional server or infrastructure that might disappear when the institution changed.

That point became more significant later.

Moving from one institution to another makes one think a little differently about academic identity. An institutional page is necessarily tied to the institution: the current designation, the department, the responsibilities held there, and whatever fields the university chooses to display. Publications remain elsewhere. Code may be on GitHub. Older projects belong to another institution. Talks, teaching material, datasets, collaborators and students are scattered across many places.

None of this is a problem by itself. Academic life has always been distributed like that. But after a few institutional transitions, it becomes obvious that the institution and the academic are not quite the same entity. The institution is an important part of the identity at a given time, but an academic career develops across institutions, students, research questions, collaborations and projects. A personal website is one of the few places where these pieces can remain connected without having to fit the structure of any particular institution.

At Digital University Kerala, a very different kind of website problem appeared through admissions work. Information changed quickly. Pages had to be created at short notice. Corrections could not wait for a long development cycle. What was needed was something lightweight, easy to modify and easy to deploy.

By then, software development itself had changed.

Vibe coding had matured enough that a website no longer had to be edited primarily by manipulating code. A requirement could be described in ordinary language, the implementation generated, the result inspected, and the next instruction based directly on what appeared on the screen. For the admissions work, this proved surprisingly practical. A frequently changing website could be managed largely through prompts, with essentially no manual coding.

Once the admission cycle was mostly over, it seemed natural to return to the neglected personal website and try the same approach.

The repository was already on GitHub, and the public repository could be used directly with ChatGPT Plus. Instead of opening old templates and starting another round of manual editing, the website was treated almost like a conversation. A change was described, the result was inspected, and the next request came from whatever still looked wrong.

What was intended as a modest update became, over the next day or so, an almost complete reconsideration of the site.

The homepage came first. Some information clearly belonged there; other material had accumulated because the homepage had always been the easiest place to add something. That led naturally to questions about navigation, research, publications, people, alumni, engagements and the principal-investigator page. Once these were reorganised, other inconsistencies became easier to see. Photographs did not follow the same proportions. Some pages carried too much information. Others lacked context. Names, affiliations and descriptions were not always presented in quite the same way.

Each correction exposed another layer.

Visual consistency led to image standardisation. Content organisation led to dedicated pages. Dedicated pages led to page titles, descriptions, headings, navigation and metadata. That led to search visibility, structured data, sitemaps and indexing. From there came another question: search is no longer limited to a list of Google results. Increasingly, information is also encountered through AI-assisted search and answer systems.

So the exercise expanded again. Could a search engine, a prospective student, a collaborator, or an AI system understand what the research group actually works on? Could important software or datasets be identified as things in their own right rather than buried inside publication lists? Was the same person clearly represented across the university page, publications, ORCID, GitHub and the personal website?

By then, the coding itself had become almost incidental.

This, more than automatic HTML or CSS generation, seems to be the important change brought by current AI tools. The implementation step has become small enough that much more attention can be given to judgment. What belongs on the homepage? What deserves its own page? What should simply be deleted? Can someone unfamiliar with the work understand it? Are important outputs buried? Does the structure reflect the way the research has actually developed?

There is also an obvious danger. When changing a website becomes extremely easy, an unnecessary change becomes equally easy. An AI system will happily redesign a section that was already adequate, rewrite text that did not need rewriting, or add elements simply because it can. Deciding when to leave something alone becomes part of the work.

In that sense, the basic method has not changed much from the early HTML days. Something is built, looked at, criticised, corrected and looked at again. What has changed dramatically is the cost of each iteration.

That matters for someone starting today.

Twenty years ago, learning at least some HTML and CSS was practically unavoidable. Later, systems such as Drupal made publishing easier but brought their own learning curve. Static-site generators such as Hugo simplified things again, although they still assumed some comfort with command lines, templates and version control.

A beginner today can start much further up the ladder.

A useful academic website can now be created with GitHub Pages and current AI tools without paying for hosting and without first becoming a web programmer. Some understanding of HTML, CSS, Git, domains and how websites work is still very useful, but these can be learned while building something. Syntax no longer has to be the starting point.

This is particularly useful for academics because most institutions already provide an official faculty page. Those pages are important. They establish the institutional affiliation and provide an authoritative record of designation, department, contact information and other standard details.

But they are necessarily templated. The university page presents academics in the way the institution needs to organise information.

A personal website can organise things in the way the academic finds useful.

Research themes can be explained in the form that makes sense for the work. Software, datasets, teaching material, talks, older projects, collaborators, student work and occasional writing can be given appropriate space. Some things may deserve a full page; others may need only a line. The structure can change as the work changes.

It also gives search engines, students, collaborators and increasingly AI-based discovery systems one place where these different parts of an academic career can be understood together.

There is another practical advantage. Institutions change. Designations change. University websites are redesigned. Servers are retired. URLs disappear. A personal academic website can remain a relatively stable point connecting all of these changes.

Until recently, maintaining one involved enough technical overhead that many academics understandably did not bother. That argument has become much weaker.

GitHub Pages can host a static website free of charge. A custom domain is optional. AI tools can handle much of the initial coding and a large part of routine modification. The real work is increasingly deciding what should be there, how it should be organised, and keeping it reasonably current.

That last part cannot be completely outsourced.

Perhaps it should not be.

An academic website is not merely another profile on the internet. It is a small piece of academic space over which one has unusual freedom. The official page records where we are and what the institution needs to present. A personal website can keep together the work, interests and history that do not fit neatly into those boxes.

And now, for the first time, creating that space requires almost no money and remarkably little technical preparation.

Every academic should probably have one, especially younger ones.
