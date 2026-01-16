---
title: "Kafka as a Platform: the Ecosystem from the Ground Up"
slug: "kafka-as-a-platform-the-ecosystem-from-the-ground-up-MaxFXn"
date: 2020-06-08T08:00:00
event: "NDC Oslo"
location: "Virtual"
image: "/images/MaxFXn/slide_000.jpg"
pdf: "/pdfs/MaxFXn.pdf"
notist_id: "MaxFXn"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.ndcoslo-2020-06-11&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors. $50 USD off your bill each calendar month for the first three months, and use code “60DEVADV” for a further $60 money towards your bill (Activate by 11th September 2020. Expires after 90 days of activation. Any unused promo value on the expiration date will be forfeited.)"
  - title: "👾Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/kafka-ecosystem"
    description: "Try out the demo for yourself - all you need is Docker and Docker Compose."
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/ndcoslo2020"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "ℹ️ Confluent Developer"
    url: "http://developer.confluent.io?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.ndcoslo-2020-06-11&utm_term=rmoff-devx"
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
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">An excellent introduction and presentation of Kafka from <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a>.<br><br>I thorouhly enjoyed learning more about Kafka by watching this one.<a href="https://t.co/KutfGGNnnq">https://t.co/KutfGGNnnq</a><a href="https://twitter.com/hashtag/kafka?src=hash&amp;ref_src=twsrc%5Etfw">#kafka</a></p>&mdash; Brian Di Croce (@bdicroce) <a href="https://twitter.com/bdicroce/status/1304096288045178881?ref_src=twsrc%5Etfw">September 10, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Well I&#39;m sold...<br><br>I&#39;m going to start using <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a></p>&mdash; Anthony Dang (@AnthonyDotNet) <a href="https://twitter.com/AnthonyDotNet/status/1271023825887678464?ref_src=twsrc%5Etfw">June 11, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">I&#39;m learning about Kafka with <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> at <a href="https://twitter.com/NDC_Conferences?ref_src=twsrc%5Etfw">@NDC_Conferences</a> Oslow</p>&mdash; Anthony Dang (@AnthonyDotNet) <a href="https://twitter.com/AnthonyDotNet/status/1271016178480275456?ref_src=twsrc%5Etfw">June 11, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/NDCOslo?src=hash&amp;ref_src=twsrc%5Etfw">#NDCOslo</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://t.co/iT3CHLYnqN">pic.twitter.com/iT3CHLYnqN</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1271012851826688000?ref_src=twsrc%5Etfw">June 11, 2020</a></blockquote>
  - type: "notist_video"
    html: |
      <iframe sandbox="allow-scripts allow-same-origin allow-presentation" allowfullscreen class="embedded-deck embedded-video"
                          src="https://notist.ninja/embed/5k8xTs"></iframe>
---

<p>Kafka has become a key data infrastructure technology, and we all have at least a vague sense that it is a messaging system, but what else is it? How can an overgrown message bus be getting this much buzz? Well, because Kafka is merely the center of a rich streaming data platform that invites detailed exploration.</p>
<p>In this talk, we’ll look at the entire streaming platform provided by Apache Kafka and the Confluent community components. Starting with a lonely key-value pair, we’ll build up topics, partitioning, replication, and low-level Producer and Consumer APIs. We’ll group consumers into elastically scalable, fault-tolerant application clusters, then layer on more sophisticated stream processing APIs like Kafka Streams and ksqlDB. We’ll help teams collaborate around data formats with schema management. We’ll integrate with legacy systems without writing custom code. By the time we’re done, the open-source project we thought was Big Data’s answer to message queues will have become an enterprise-grade streaming platform, all in 60 minutes.</p>
