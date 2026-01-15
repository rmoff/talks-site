---
title: "Kafka as a Platform: the Ecosystem from the Ground Up"
slug: "kafka-as-a-platform-the-ecosystem-from-the-ground-up-Q3AoWZ"
aliases: ["/Q3AoWZ/kafka-as-a-platform-the-ecosystem-from-the-ground-up"]
date: 2020-06-09T08:00:00
event: "Confluent VUG"
location: "Virtual"
image: "/images/Q3AoWZ/slide_000.jpg"
pdf: "/pdfs/Q3AoWZ.pdf"
notist_id: "Q3AoWZ"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup?utm_source=meetup&utm_medium=slide&utm_campaign=ty.community.con.confluentvug-2020-06-09&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors."
  - title: "🎥 Recording"
    url: "https://videos.confluent.io/watch/7wjvUPesfRGamMPa2U2BwQ"
  - title: "👾Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/kafka-ecosystem"
    description: "Try out the demo for yourself - all you need is Docker and Docker Compose."
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/6hz"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "ℹ️ Confluent Developer"
    url: "http://developer.confluent.io?utm_source=meetup&utm_medium=slide&utm_campaign=ty.community.con.confluentvug-2020-06-09&utm_term=rmoff-devx"
    description: "Tutorials, videos, blogs, podcasts, and more - all for developers working with Apache Kafka and Confluent Platform"
  - title: "🎥 Kafka Connect tutorials on YouTube"
    url: "http://rmoff.dev/youtube"
  - title: "🧩 Confluent Hub"
    url: "https://www.confluent.io/hub/?utm_source=meetup&utm_medium=slide&utm_campaign=ty.community.con.confluentvug-2020-06-09&utm_term=rmoff-devx"
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
    url: "http://rmoff.dev/ksldn19-kafka-connect"
    description: "Learn all about Kafka Connect (including the connectors available with ksqlDB)"
  - title: "📌The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://rmoff.dev/oredev19-changing-face-of-etl"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">My boy <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> speaking about <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@ApacheKafka</a> as a platform today on <a href="https://twitter.com/hashtag/ConfluentVUG?src=hash&amp;ref_src=twsrc%5Etfw">#ConfluentVUG</a> <a href="https://t.co/hROp2mrIZy">pic.twitter.com/hROp2mrIZy</a></p>&mdash; Ricardo Ferreira (@riferrei) <a href="https://twitter.com/riferrei/status/1270330554999885826?ref_src=twsrc%5Etfw">June 9, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Excellent overview of the <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a> ecosystem, by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a>. So much information packed into 1 hour! Great Q&amp;A coverage by <a href="https://twitter.com/riferrei?ref_src=twsrc%5Etfw">@riferrei</a> &amp; <a href="https://twitter.com/jasonbelldata?ref_src=twsrc%5Etfw">@jasonbelldata</a>.  I can&#39;t wait til the video is up on <a href="https://t.co/lruh5donPF">https://t.co/lruh5donPF</a></p>&mdash; Dave Klein (@daveklein) <a href="https://twitter.com/daveklein/status/1270343768399626241?ref_src=twsrc%5Etfw">June 9, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Participant click . Love the concept of Ksql <a href="https://t.co/Tmu4NVdfyi">pic.twitter.com/Tmu4NVdfyi</a></p>&mdash; Javed Khan (@javs_says) <a href="https://twitter.com/javs_says/status/1270338754331373569?ref_src=twsrc%5Etfw">June 9, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">That beard is looking impressive. Hope the session went well.</p>&mdash; Curtis Thacker (@curtisthacker) <a href="https://twitter.com/curtisthacker/status/1270362489226539008?ref_src=twsrc%5Etfw">June 9, 2020</a></blockquote>
---

<p>Kafka has become a key data infrastructure technology, and we all have at least a vague sense that it is a messaging system, but what else is it? How can an overgrown message bus be getting this much buzz? Well, because Kafka is merely the center of a rich streaming data platform that invites detailed exploration.</p>
<p>In this talk, we’ll look at the entire streaming platform provided by Apache Kafka and the Confluent community components. Starting with a lonely key-value pair, we’ll build up topics, partitioning, replication, and low-level Producer and Consumer APIs. We’ll group consumers into elastically scalable, fault-tolerant application clusters, then layer on more sophisticated stream processing APIs like Kafka Streams and ksqlDB. We’ll help teams collaborate around data formats with schema management. We’ll integrate with legacy systems without writing custom code. By the time we’re done, the open-source project we thought was Big Data’s answer to message queues will have become an enterprise-grade streaming platform, all in 60 minutes.</p>
