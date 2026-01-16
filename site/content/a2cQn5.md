---
title: "No More Silos: Integrating Databases and Apache Kafka"
slug: "no-more-silos-integrating-databases-and-apache-kafka-a2cQn5"
date: 2019-06-24T08:00:00
event: "KScope 19"
location: "Seattle, WA, USA"
image: "/images/a2cQn5/slide_000.jpg"
pdf: "/pdfs/a2cQn5.pdf"
notist_id: "a2cQn5"
resources:
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "👾 Demo code"
    url: "https://github.com/confluentinc/demo-scene/blob/master/no-more-silos/no-more-silos.adoc"
  - title: "🎥 Recording"
    url: "https://www.confluent.io/kafka-summit-ny19/no-more-silos-integrating-db-into-apache-kafka"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Here’s <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> embedding himself inside of <a href="https://twitter.com/hashtag/Kafka?src=hash&amp;ref_src=twsrc%5Etfw">#Kafka</a> Streams. <a href="https://twitter.com/hashtag/KScope19?src=hash&amp;ref_src=twsrc%5Etfw">#KScope19</a> <a href="https://t.co/MaRlG7fi07">pic.twitter.com/MaRlG7fi07</a></p>&mdash; Michael Rainey ❄️ (@mRainey) <a href="https://twitter.com/mRainey/status/1143562403897991169?ref_src=twsrc%5Etfw">June 25, 2019</a></blockquote>
---

<p>Companies new and old are all recognising the importance of a low-latency, scalable, fault-tolerant data backbone, in the form of the Apache Kafka streaming platform. With Kafka, developers can integrate multiple sources and systems, which enables low latency analytics, event-driven architectures and the population of multiple downstream systems.</p>
<p>In this talk, we’ll look at one of the most common integration requirements - connecting databases to Kafka. We’ll consider the concept that all data is a stream of events, including that residing within a database. We’ll look at why we’d want to stream data from a database, including driving applications in Kafka from events upstream. We’ll discuss the different methods for connecting databases to Kafka, and the pros and cons of each. Techniques including Change-Data-Capture (CDC) and Kafka Connect will be covered, as well as an exploration of the power of KSQL for performing transformations such as joins on the inbound data.</p>
