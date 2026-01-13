---
title: "Introduction to ksqlDB"
slug: "introduction-to-ksqldb-WKykIL"
date: 2020-05-13T08:00:00
event: "LJC Virtual Meetup"
location: "Virtual"
image: "/images/WKykIL/slide_000.jpg"
pdf: "/pdfs/WKykIL.pdf"
notist_id: "WKykIL"
resources:
  - title: "👾Demo code"
    url: "https://rmoff.dev/ksqldb-demo"
    description: "Try out the ksqlDB demo for yourself - all you need is Docker and Docker Compose."
  - title: "👾 Building a Telegram Bot Powered by Apache Kafka and ksqlDB"
    url: "https://cnfl.io/telegram-bot-powered-by-kafka-and-ksqldb"
    description: "A fun blog showing what you can do with ksqlDB and Kafka"
  - title: "ℹ️ Confluent Developer"
    url: "http://developer.confluent.io"
    description: "Tutorials, videos, blogs, podcasts, and more - all for developers working with Apache Kafka and Confluent Platform"
  - title: "Confluent Hub"
    url: "https://www.confluent.io/hub/"
    description: "Huge list of connectors for Kafka Connect"
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup"
    description: "Fully Managed Apache Kafka, Schema Registry, KSQL, and Connectors"
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/ljcjug"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "📌From Zero to Hero with Kafka Connect"
    url: "http://rmoff.dev/ksldn19-kafka-connect"
    description: "Learn all about Kafka Connect (including the connectors available with ksqlDB)"
  - title: "📌The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://rmoff.dev/oredev19-changing-face-of-etl"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">I am now a Kafka convert thanks to <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> - the third in his series of <a href="https://twitter.com/ljcjug?ref_src=twsrc%5Etfw">@ljcjug</a> talks this evening and I&#39;m blown away</p>&mdash; Peter Hicks (@poggs) <a href="https://twitter.com/poggs/status/1260645000531963907?ref_src=twsrc%5Etfw">May 13, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Sadly, I had to miss the last few minutes of <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a>&#39;s talk at <a href="https://twitter.com/ljcjug?ref_src=twsrc%5Etfw">@ljcjug</a>. Had to rush to catch my flight back to St. Louis for another meeting.  But thank Robin for the clear explanation and demo of <a href="https://twitter.com/ksqlDB?ref_src=twsrc%5Etfw">@ksqlDB</a>.</p>&mdash; Dave Klein (@daveklein) <a href="https://twitter.com/daveklein/status/1260646314800328704?ref_src=twsrc%5Etfw">May 13, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Time to pop over to London to catch another great presentation by <a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a>, courtesy of the kind folks at the <a href="https://twitter.com/ljcjug?ref_src=twsrc%5Etfw">@ljcjug</a></p>&mdash; Dave Klein (@daveklein) <a href="https://twitter.com/daveklein/status/1260629994394566657?ref_src=twsrc%5Etfw">May 13, 2020</a></blockquote>
---

<p>You’ve got streams of data that you want to process and store? You’ve got events from which you’d like to derive state or build aggregates? And you want to do all of this in a scalable and fault-tolerant manner? It’s just as well that Kafka and ksqlDB exist!</p>
<p>This talk will be built around a live demonstration of the concepts and capabilities of ksqlDB. We’ll see how you can apply transformations to a stream of events from one Kafka topic to another. We’ll use ksqlDB connectors to bring in data from other systems and use this to join and enrich streams—and we’ll serve the results up directly to an application, without even needing an external data store.</p>
<p>Attendees will learn:</p>
<ul>
<li>How to process streams of events</li>
<li>The semantics of streams and tables, and of push and pull queries</li>
<li>How to use the ksqlDB API to get state directly from the materialised store</li>
<li>What makes ksqlDB elastically scalable and fault-tolerant.</li>
</ul>
