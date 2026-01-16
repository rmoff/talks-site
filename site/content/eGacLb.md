---
title: "No More Silos: Integrating Databases and Apache Kafka"
slug: "no-more-silos-integrating-databases-and-apache-kafka-eGacLb"
date: 2019-04-02T08:00:00
event: "Kafka Summit New York 2019"
location: "New York, NY, USA"
image: "/images/eGacLb/slide_000.jpg"
pdf: "/pdfs/eGacLb.pdf"
notist_id: "eGacLb"
resources:
  - title: "🎥 Recording"
    url: "https://www.confluent.io/kafka-summit-ny19/no-more-silos-integrating-db-into-apache-kafka"
  - title: "✍️Blog - No more silos"
    url: "https://www.confluent.io/blog/no-more-silos-how-to-integrate-your-databases-with-apache-kafka-and-cdc"
  - title: "👾 Demo code"
    url: "https://github.com/confluentinc/demo-scene/blob/master/no-more-silos/demo_no-more-silos.adoc"
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Every time I see the quote &quot;The truth is the log&quot; on a slide, I want to see a picture of log lady from twin peaks.  Great talk by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a>  at <a href="https://twitter.com/hashtag/kafkasummit?src=hash&amp;ref_src=twsrc%5Etfw">#kafkasummit</a> and so central to what we do and my world dominatio..overall architecture <a href="https://t.co/fkOsS51eln">pic.twitter.com/fkOsS51eln</a></p>&mdash; Anna McDonald (@jbfletch_) <a href="https://twitter.com/jbfletch_/status/1113110843200323592?ref_src=twsrc%5Etfw">April 2, 2019</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="in" dir="ltr">Best presentation - Integrating databases into Apache Kafka <a href="https://twitter.com/kafkasummit?ref_src=twsrc%5Etfw">@kafkasummit</a> <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a></p>&mdash; Selva Prabhu (@selvaprabhua) <a href="https://twitter.com/selvaprabhua/status/1113138479897219073?ref_src=twsrc%5Etfw">April 2, 2019</a></blockquote>
---

<p>Companies new and old are all recognising the importance of a low-latency, scalable, fault-tolerant data backbone, in the form of the Apache Kafka streaming platform. With Kafka, developers can integrate multiple sources and systems, which enables low latency analytics, event-driven architectures and the population of multiple downstream systems.</p>
<p>In this talk, we’ll look at one of the most common integration requirements - connecting databases to Kafka. We’ll consider the concept that all data is a stream of events, including that residing within a database. We’ll look at why we’d want to stream data from a database, including driving applications in Kafka from events upstream. We’ll discuss the different methods for connecting databases to Kafka, and the pros and cons of each. Techniques including Change-Data-Capture (CDC) and Kafka Connect will be covered, as well as an exploration of the power of KSQL for performing transformations such as joins on the inbound data.</p>
