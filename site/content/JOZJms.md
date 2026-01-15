---
title: "No More Silos: Integrating Databases and Apache Kafka"
slug: "no-more-silos-integrating-databases-and-apache-kafka-JOZJms"
aliases: ["/JOZJms/no-more-silos-integrating-databases-and-apache-kafka"]
date: 2021-06-14T08:00:00
event: "Berlin Buzzwords"
location: "Virtual"
image: "/images/JOZJms/slide_000.jpg"
pdf: "/pdfs/JOZJms.pdf"
notist_id: "JOZJms"
resources:
  - title: "🎥 YouTube - Kafka Connect and ksqlDB videos"
    url: "http://youtube.com/rmoff"
  - title: "💾 Confluent Hub"
    url: "https://www.confluent.io/hub/"
  - title: "☁️ Confluent Cloud"
    url: "https://confluent.cloud/signup?utm_source=conference&utm_medium=slide&utm_campaign=ty.community.con.bbuzz-2021-06-16&utm_term=rmoff-devx"
    description: "Fully Managed Apache Kafka, Schema Registry, ksqlDB, and Connectors. Use promo code RMOFF200 to get an additional $200 of free Confluent Cloud usage ( T&amp;C )"
  - title: "💬 Confluent Community Forum"
    url: "https://forum.confluent.io/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Listening to my friend <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> making a great <a href="https://twitter.com/hashtag/bbuzz?src=hash&amp;ref_src=twsrc%5Etfw">#bbuzz</a> about integrating databases and <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@ApacheKafka</a>. <a href="https://t.co/UhqtOC94oN">pic.twitter.com/UhqtOC94oN</a></p>&mdash; Ricardo Ferreira (@riferrei) <a href="https://twitter.com/riferrei/status/1405207823907180548?ref_src=twsrc%5Etfw">June 16, 2021</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/bbuzz?src=hash&amp;ref_src=twsrc%5Etfw">#bbuzz</a> <a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://t.co/Ko7VQHOFm7">pic.twitter.com/Ko7VQHOFm7</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1405205754253131785?ref_src=twsrc%5Etfw">June 16, 2021</a></blockquote>
---

<p>Companies new and old are all recognising the importance of a low-latency, scalable, fault-tolerant data backbone, in the form of the Apache Kafka streaming platform. With Kafka, developers can integrate multiple sources and systems, which enables low latency analytics, event-driven architectures and the population of multiple downstream systems.</p>
<p>In this talk, we’ll look at one of the most common integration requirements - connecting databases to Kafka. We’ll consider the concept that all data is a stream of events, including that residing within a database. We’ll look at why we’d want to stream data from a database, including driving applications in Kafka from events upstream. We’ll discuss the different methods for connecting databases to Kafka, and the pros and cons of each. Techniques including Change-Data-Capture (CDC) and Kafka Connect will be covered, as well as an exploration of the power of ksqlDB for performing transformations such as joins on the inbound data.</p>
<p>Attendees of this talk will learn:</p>
<ul>
<li>why events, not just state, matter</li>
<li>the difference between log-based CDC and query-based CDC</li>
<li>how to chose which CDC approach to use</li>
</ul>
