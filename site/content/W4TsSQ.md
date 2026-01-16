---
title: "Kafka as a Platform: the Ecosystem from the Ground Up"
slug: "kafka-as-a-platform-the-ecosystem-from-the-ground-up-W4TsSQ"
date: 2020-09-23T08:00:00
event: "Budapest Data Forum"
location: "Budapest, Hungary"
image: "/images/W4TsSQ/slide_000.jpg"
pdf: "/pdfs/W4TsSQ.pdf"
notist_id: "W4TsSQ"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.BudapestDataForum-2020-09-21&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors. $50 USD off your bill each calendar month for the first three months, and use code “60DEVADV” for a further $60 money towards your bill (Activate by 11th September 2020. Expires after 90 days of activation. Any unused promo value on the expiration date will be forfeited.)"
  - title: "👾Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/kafka-ecosystem"
    description: "Try out the demo for yourself - all you need is Docker and Docker Compose."
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/budapestdata"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "ℹ️ Confluent Developer"
    url: "http://developer.confluent.io?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.BudapestDataForum-2020-09-21&utm_term=rmoff-devx"
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
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://twitter.com/hashtag/budapestdata?src=hash&amp;ref_src=twsrc%5Etfw">#budapestdata</a> <a href="https://twitter.com/BudapestData?ref_src=twsrc%5Etfw">@BudapestData</a> <a href="https://t.co/dkVL8vbrSg">pic.twitter.com/dkVL8vbrSg</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1308722648378159104?ref_src=twsrc%5Etfw">September 23, 2020</a></blockquote>
---

<p>Kafka has become a key data infrastructure technology, and we all have at least a vague sense that it is a messaging system, but what else is it? How can an overgrown message bus be getting this much buzz? Well, because Kafka is merely the center of a rich streaming data platform that invites detailed exploration.</p>
<p>In this talk, we’ll look at the entire streaming platform provided by Apache Kafka and the Confluent community components. Starting with a lonely key-value pair, we’ll build up topics, partitioning, replication, and low-level Producer and Consumer APIs. We’ll group consumers into elastically scalable, fault-tolerant application clusters, then layer on more sophisticated stream processing APIs like Kafka Streams and ksqlDB. We’ll help teams collaborate around data formats with schema management. We’ll integrate with legacy systems without writing custom code. By the time we’re done, the open-source project we thought was Big Data’s answer to message queues will have become an enterprise-grade streaming platform, all in 20 minutes.</p>
