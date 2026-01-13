---
title: "The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
slug: "the-changing-face-of-etl-event-driven-architectures-for-data-engineers-ZPJzzF"
date: 2020-07-01T08:00:00
event: "Confluent VUG"
location: "Virtual"
image: "/images/ZPJzzF/slide_000.jpg"
pdf: "/pdfs/ZPJzzF.pdf"
notist_id: "ZPJzzF"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.confluentvug-2020-07-01&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors."
  - title: "📌Kafka as a Platform: the Ecosystem from the Ground Up"
    url: "https://rmoff.dev/kafka101"
    description: "Kafka 101 - introducing the concepts, the APIs, and the ecosystem"
  - title: "🎥 Recording"
    url: "https://events.confluent.io/meetups"
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/q2m"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "ℹ️ Confluent Developer"
    url: "http://developer.confluent.io?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.confluentvug-2020-07-01&utm_term=rmoff-devx"
    description: "Tutorials, videos, blogs, podcasts, and more - all for developers working with Apache Kafka and Confluent Platform"
  - title: "🎥 Kafka Connect tutorials on YouTube"
    url: "http://rmoff.dev/youtube"
  - title: "🧩 Confluent Hub"
    url: "https://www.confluent.io/hub/?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.DataXDays-2020-06-22&utm_term=rmoff-devx"
    description: "Huge list of connectors for Kafka Connect"
  - title: "👾 Building a Telegram Bot Powered by Apache Kafka and ksqlDB"
    url: "https://cnfl.io/telegram-bot-powered-by-kafka-and-ksqldb"
    description: "A fun blog showing what you can do with ksqlDB and Kafka"
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "📌 Apache Kafka and ksqlDB in Action: Let’s Build a Streaming Data Pipeline!"
    url: "https://rmoff.dev/ljc-kafka-01"
  - title: "📌 Introduction to ksqlDB"
    url: "https://rmoff.dev/ljc-kafka-03"
    description: "Learn all about ksqlDB in this 45 minute talk &amp; live demo"
  - title: "📌From Zero to Hero with Kafka Connect"
    url: "https://rmoff.dev/ljc-kafka-02"
    description: "Learn all about Kafka Connect (including the connectors available with ksqlDB)"
  - title: "📌The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://rmoff.dev/oredev19-changing-face-of-etl"
  - title: "🚂On Track with Apache Kafka: Building a Streaming Platform solution with Rail Data"
    url: "https://rmoff.dev/oredev19-on-track-with-kafka"
    description: "Apache Kafka and Confluent Platform in Action! Using live streams of rail movement data in all sorts of useful ways for analysis and applications."
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/ConfluentVUG?src=hash&amp;ref_src=twsrc%5Etfw">#ConfluentVUG</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://t.co/amQCubeKij">https://t.co/amQCubeKij</a> <a href="https://t.co/IgkTblXUoH">pic.twitter.com/IgkTblXUoH</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1278313389576642560?ref_src=twsrc%5Etfw">July 1, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Not only did <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> show us how <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a> is changing the world, he showed us how it is making it much better!  Thanks Robin!  And thanks <a href="https://twitter.com/ale?ref_src=twsrc%5Etfw">@ale</a> for running another smooth event! Thanks to <a href="https://twitter.com/nbuesing?ref_src=twsrc%5Etfw">@nbuesing</a> and the rest who joined in!</p>&mdash; Dave Klein (@daveklein) <a href="https://twitter.com/daveklein/status/1278329499281756165?ref_src=twsrc%5Etfw">July 1, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr"><a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a>&#39;s blogs on connectors, database configurations, elastic search configurations, ..... are a lifesaver to anyone working in this space.  The more you integrate systems with Kafka, the more you will appreciate all of this.</p>&mdash; Neil Buesing (@nbuesing) <a href="https://twitter.com/nbuesing/status/1278330230827089920?ref_src=twsrc%5Etfw">July 1, 2020</a></blockquote>
---

<p>Data integration in architectures built on static, update-in-place datastores inevitably end up with pathologically high degrees of coupling and poor scalability. This has been the standard practice for decades, as we attempt to build data pipelines on top of databases that do a poor job modelling the fundamental objects that drive our businesses and systems: events.</p>
<p>Events carry both notification and state, and form a powerful primitive on which to build systems for developers and data engineers alike. Developers benefit from the asynchronous communication that events enable between services, and data engineers benefit from the integration capabilities. Everyone gains from using the standards-based, scalable and resilient streaming platform.</p>
<p>In this talk, we’ll discuss the concepts of events, their relevance to both software engineers and data engineers and their ability to unify architectures in a powerful way. We’ll see how stream processing makes sense in both a microservices and ETL environment, and why analytics, data integration and ETL fit naturally into a streaming world. The talk will conclude with a hands-on demonstration of these concepts in practice using Apache Kafka and commentary on the design choices made.</p>
<p>Join this talk to learn:</p>
<ul>
<li>The power of events and unbounded data</li>
<li>Streaming is not just for real-time applications—it’s for everyone</li>
<li>Where a streaming platform fits in an analytic architecture</li>
<li>How event-driven architectures can enable greater scalability and flexibility of systems both now and in the future</li>
</ul>
