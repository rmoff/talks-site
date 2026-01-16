---
title: "Introduction to ksqlDB"
slug: "introduction-to-ksqldb-NrxcrM"
date: 2020-02-26T08:00:00
event: "Krakòw Apache Kafka meetup"
location: "Kraków, Poland"
image: "/images/NrxcrM/slide_000.jpg"
pdf: "/pdfs/NrxcrM.pdf"
notist_id: "NrxcrM"
resources:
  - title: "👾Demo code"
    url: "https://rmoff.dev/ksqldb-demo"
    description: "Try out the ksqlDB demo for yourself - all you need is Docker and Docker Compose."
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup"
    description: "Fully Managed Apache Kafka, Schema Registry, KSQL, and Connectors"
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/books-krk20"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "📌From Zero to Hero with Kafka Connect"
    url: "https://rmoff.dev/berlin19-kafka-connect"
    description: "Learn all about Kafka Connect (including the connectors available with ksqlDB)"
  - title: "📌The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://rmoff.dev/oredev19-changing-face-of-etl"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Krakòw <a href="https://twitter.com/apachekafka?ref_src=twsrc%5Etfw">@apachekafka</a> meetup getting underway in one of the best venues! Thanks to <a href="https://twitter.com/VirtusLab?ref_src=twsrc%5Etfw">@VirtusLab</a> for hosting. <a href="https://t.co/Dr2w2StrD9">pic.twitter.com/Dr2w2StrD9</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1232720953093894145?ref_src=twsrc%5Etfw">February 26, 2020</a></blockquote>
  - type: "notist_video"
    html: |
      <iframe sandbox="allow-scripts allow-same-origin allow-presentation" allowfullscreen class="embedded-deck embedded-video"
                          src="https://notist.ninja/embed/Q2lIog"></iframe>
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
