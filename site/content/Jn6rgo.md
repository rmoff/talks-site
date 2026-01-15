---
title: "The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
slug: "the-changing-face-of-etl-event-driven-architectures-for-data-engineers-Jn6rgo"
aliases: ["/Jn6rgo/the-changing-face-of-etl-event-driven-architectures-for-data-engineers"]
date: 2020-02-03T08:00:00
event: "OOP"
location: "Munich, Germany"
image: "/images/Jn6rgo/slide_000.jpg"
pdf: "/pdfs/Jn6rgo.pdf"
notist_id: "Jn6rgo"
resources:
  - title: "📚Free eBooks (including “Kafka: The Definitive Guide”)"
    url: "https://rmoff.dev/oopmuc"
  - title: "Recording"
    url: "https://rmoff.dev/oredev19-changing-face-of-etl"
    description: "Recording from a previous presentation of this talk."
  - title: "No More Silos: Integrating Databases and Apache Kafka"
    url: "http://rmoff.dev/ksny19-no-more-silos"
  - title: "Kafka & ksqlDB demo"
    url: "https://github.com/confluentinc/demo-scene/blob/master/build-a-streaming-pipeline/"
    description: "Try it yourself!"
  - title: "✍️ Blog: The Changing Face of ETL"
    url: "https://www.confluent.io/blog/changing-face-etl"
  - title: "💬 Join the Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud"
    description: "Provides managed Apache Kafka, Schema Registry, KSQL, etc"
  - title: "📫 Confluent Community mailing list"
    url: "https://groups.google.com/forum/#!forum/confluent-platform"
  - title: "💾 Download Confluent Platform"
    url: "https://www.confluent.io/download/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Great talk! Thanks!</p>&mdash; Christian Wolf (@chaos0815) <a href="https://twitter.com/chaos0815/status/1224692500591521792?ref_src=twsrc%5Etfw">February 4, 2020</a></blockquote>
---

<p>Data integration in architectures built on static, update-in-place datastores inevitably end up with pathologically high degrees of coupling and poor scalability. This has been the standard practice for decades, as we attempt to build data pipelines on top of databases that do a poor job modeling the fundamental objects that drive our businesses and systems: events.</p>
<p>Events carry both notification and state, and form a powerful primitive on which to build systems for developers and data engineers alike. Developers benefit from the asynchronous communication that events enable between services, and data engineers benefit from the integration capabilities. Everyone gains from using the standards-based, scalable and resilient streaming platform.</p>
<p>In this talk, we’ll discuss the concepts of events, their relevance to both software engineers and data engineers and their ability to unify architectures in a powerful way. We’ll see how stream processing makes sense in both a microservices and ETL environment, and why analytics, data integration and ETL fit naturally into a streaming world.</p>
