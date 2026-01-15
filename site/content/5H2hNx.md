---
title: "Apache Kafka and ksqlDB in Action : Let’s Build a Streaming Data Pipeline!"
slug: "apache-kafka-and-ksqldb-in-action-lets-build-a-streaming-data-pipeline-5H2hNx"
aliases: ["/5H2hNx/apache-kafka-and-ksqldb-in-action-lets-build-a-streaming-data-pipeline"]
date: 2020-03-04T08:00:00
event: "London Apache Kafka Meetup"
location: "London, UK"
image: "/images/5H2hNx/slide_000.jpg"
pdf: "/pdfs/5H2hNx.pdf"
notist_id: "5H2hNx"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup"
    description: "Fully Managed Apache Kafka, Schema Registry, KSQL, and Connectors"
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/ldn-mar20"
    description: "Free eBooks to download, including “Kafka: The Definitive Guide”, and “I ❤️Logs”"
  - title: "📌From Zero to Hero with Kafka Connect"
    url: "https://rmoff.dev/berlin19-kafka-connect"
    description: "Learn all about Kafka Connect (including the connectors available with ksqlDB)"
  - title: "📌Introduction to ksqlDB"
    url: "https://rmoff.dev/ksqldb-slides"
    description: "Learn more about ksqlDB beyond what was covered in this talk"
  - title: "📌No More Silos: Integrating Databases and Apache Kafka"
    url: "http://rmoff.dev/ksny19-no-more-silos"
    description: "Details on the specifics of streaming changes from a database into Kafka."
  - title: "📌The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://rmoff.dev/oredev19-changing-face-of-etl"
  - title: "✍️Kafka Connect Deep Dive – Converters and Serialization Explained"
    url: "https://www.confluent.io/blog/kafka-connect-deep-dive-converters-serialization-explained/"
  - title: "✍️Kafka Connect Deep Dive – Error Handling and Dead Letter Queues"
    url: "https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/"
  - title: "👾Demo code"
    url: "https://github.com/confluentinc/demo-scene/tree/master/build-a-streaming-pipeline/"
    description: "Code and script to try out the demo from the talk - you just need Docker Compose."
  - title: "👥Kafka Summit London 2020"
    url: "https://kafka-summit.org/events/kafka-summit-london-2020/"
    description: "Two days of talks all about Apache Kafka - register with code MOFFATT30 for a 30% discount."
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">ksqlDB in Action <a href="https://t.co/4hE5pbb0hv">pic.twitter.com/4hE5pbb0hv</a></p>&mdash; Ahmed (@aelbozie) <a href="https://twitter.com/aelbozie/status/1235289684336685056?ref_src=twsrc%5Etfw">March 4, 2020</a></blockquote>
---

<p>Kafka is a whole lot more than just a message bus! It includes stream processing and integration capabilities, and this talk will be mostly live coding to demonstrate what can be built around it, how to do it - and why to do it.</p>
<hr />
<p>Have you ever thought that you needed to be a programmer to do stream processing and build streaming data pipelines? Think again!
Apache Kafka is a distributed, scalable, and fault-tolerant streaming platform, providing low-latency pub-sub messaging coupled with native storage and stream processing capabilities. Integrating Kafka with RDBMS, NoSQL, and object stores is simple with Kafka Connect, which is part of Apache Kafka. ksqlDB is the source-available SQL streaming engine for Apache Kafka, and makes it possible to build stream processing applications at scale, written using a familiar SQL interface.</p>
<p>In this talk, we’ll explain the architectural reasoning for Apache Kafka and the benefits of real-time integration, and we’ll build a streaming data pipeline using nothing but our bare hands, Kafka Connect, and ksqlDB.</p>
<p>Gasp as we filter events in real-time! Be amazed at how we can enrich streams of data with data from RDBMS! Be astonished at the power of streaming aggregates for anomaly detection!</p>
