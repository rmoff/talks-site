---
title: "Integrating Oracle and Kafka"
slug: "integrating-oracle-and-kafka-ixPL5r"
date: 2020-06-15T08:00:00
event: "ACEs @ Home"
location: "Virtual"
image: "/images/ixPL5r/slide_000.jpg"
pdf: "/pdfs/ixPL5r.pdf"
notist_id: "ixPL5r"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup?utm_source=meetup&utm_medium=slide&utm_campaign=ty.community.con.ACEsAtHome-2020-06-15&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors."
  - title: "📌Kafka as a Platform: the Ecosystem from the Ground Up"
    url: "https://rmoff.dev/kafka101"
    description: "Kafka 101 - introducing the concepts, the APIs, and the ecosystem"
  - title: "👾Demo code"
    url: "https://github.com/confluentinc/demo-scene/blob/master/oracle-and-kafka/demo_integrating_oracle_kafka.adoc"
    description: "Try out the demo for yourself - all you need is Docker and Docker Compose."
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/aces"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "ℹ️ Confluent Developer"
    url: "http://developer.confluent.io?utm_source=meetup&utm_medium=slide&utm_campaign=ty.community.con.ACEsAtHome-2020-06-15&utm_term=rmoff-devx"
    description: "Tutorials, videos, blogs, podcasts, and more - all for developers working with Apache Kafka and Confluent Platform"
  - title: "🎥 Kafka Connect tutorials on YouTube"
    url: "http://rmoff.dev/youtube"
  - title: "🧩 Confluent Hub"
    url: "https://www.confluent.io/hub/?utm_source=meetup&utm_medium=slide&utm_campaign=ty.community.con.ACEsAtHome-2020-06-15&utm_term=rmoff-devx"
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
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">If you&#39;re watching <a href="https://twitter.com/acesathome?ref_src=twsrc%5Etfw">@acesathome</a> - you just got rick-rolled by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> : <a href="https://t.co/27UxsoXlWh">pic.twitter.com/27UxsoXlWh</a></p>&mdash; Christian Berg (@Nephentur) <a href="https://twitter.com/Nephentur/status/1272526390441771011?ref_src=twsrc%5Etfw">June 15, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/ACEsAtHome?src=hash&amp;ref_src=twsrc%5Etfw">#ACEsAtHome</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://t.co/LRn4eLl2Uy">pic.twitter.com/LRn4eLl2Uy</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1272518838442172416?ref_src=twsrc%5Etfw">June 15, 2020</a></blockquote>
---

<p>For all its quirks and licence fees, we all love Oracle for what it does. But sometimes we want to get the data out to use elsewhere. Maybe we want to build analytics on it; perhaps we want to drive applications with it; sometimes we might even want to move it to another non-Oracle database—can you imagine that! 😱</p>
<p>With Apache Kafka as our scalable, distributed event streaming platform, we can ingest data from Oracle as a stream of events. We can use Kafka to transform and enrich the events if we want to, even joining them to data from other sources. We can stream the resulting events to target systems, as well as use them to create event-driven microservices.</p>
<p>This talk will show some basics of Kafka and then dive into ingesting data from Oracle into Kafka, applying stream processing with ksqlDB, and then pushing that data to systems including PostgreSQL as well as back into Oracle itself.</p>
