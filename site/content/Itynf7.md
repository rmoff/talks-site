---
title: "From Zero to Hero with Kafka Connect"
slug: "from-zero-to-hero-with-kafka-connect-Itynf7"
aliases: ["/Itynf7/from-zero-to-hero-with-kafka-connect"]
date: 2020-03-23T08:00:00
event: "Apache Kafka Meetup"
location: "Virtual"
image: "/images/Itynf7/slide_000.png"
pdf: "/pdfs/Itynf7.pdf"
notist_id: "Itynf7"
resources:
  - title: "☁️Confluent Cloud"
    url: "https://confluent.cloud/signup"
    description: "Fully Managed Apache Kafka, Schema Registry, KSQL, and Connectors"
  - title: "📚Free eBooks"
    url: "https://rmoff.dev/cph-0320"
    description: "Free eBooks to download, including Kafka: The Definitive Guide."
  - title: "💬 Confluent Community Slack group"
    url: "http://cnfl.io/slack"
  - title: "👾 Demo code"
    url: "https://rmoff.dev/brujug20-code"
    description: "All you need is Docker &amp; Docker Compose!"
  - title: "🎥 Recording"
    url: "https://videos.confluent.io/watch/wyc1oqmkoQj4k5WM9CuAwg?"
    description: "Same talk, different occassion."
  - title: "📹Streaming data from Kafka to a Database with the JDBC Sink"
    url: "https://dev.to/rmoff/streaming-data-from-kafka-to-a-database-video-walkthrough-4o5p"
  - title: "🖼️No More Silos: Integrating Databases and Apache Kafka"
    url: "http://rmoff.dev/ksny19-no-more-silos"
    description: "The ins and outs of streaming data from RDBMS into Kafka, including how to choose between query-based CDC (JDBC Source connector) and log-based CDC (e.g. Debezium, GoldenGate, etc)"
  - title: "🖼️The Changing Face of ETL: Event-Driven Architectures for Data Engineers"
    url: "https://talks.rmoff.net/Jn6rgo/the-changing-face-of-etl-event-driven-architectures-for-data-engineers"
  - title: "✍️Kafka Connect Deep Dive – Converters and Serialization Explained"
    url: "https://www.confluent.io/blog/kafka-connect-deep-dive-converters-serialization-explained/"
  - title: "✍️Kafka Connect Deep Dive – Error Handling and Dead Letter Queues"
    url: "https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/"
embeds:
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr"><a href="https://twitter.com/rmoff?ref_src=twsrc%5Etfw">@rmoff</a> explaining how to scale out Kafka Connect using the distributed mode. This is the type of knowledge that the <a href="https://twitter.com/confluentinc?ref_src=twsrc%5Etfw">@ConfluentInc</a> DevRel team is bringing to the world with the online meetups! <a href="https://t.co/FWBlqiDlx4">pic.twitter.com/FWBlqiDlx4</a></p>&mdash; Ricardo Ferreira (@riferrei) <a href="https://twitter.com/riferrei/status/1242155214230208513?ref_src=twsrc%5Etfw">March 23, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">I got to the meetup venue early. See you all soon! <a href="https://t.co/TutQF3YeUv">https://t.co/TutQF3YeUv</a> <a href="https://t.co/lL08vJuUKX">pic.twitter.com/lL08vJuUKX</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1242136306009899009?ref_src=twsrc%5Etfw">March 23, 2020</a></blockquote>
  - type: "twitter"
    html: |
      <blockquote class="twitter-tweet" data-dnt="true"><p lang="und" dir="ltr"><a href="https://twitter.com/hashtag/speakerselfie?src=hash&amp;ref_src=twsrc%5Etfw">#speakerselfie</a> <a href="https://twitter.com/hashtag/KafkaMeetup?src=hash&amp;ref_src=twsrc%5Etfw">#KafkaMeetup</a> <a href="https://t.co/JM7yyo42S2">pic.twitter.com/JM7yyo42S2</a></p>&mdash; Robin Moffatt 🍻🏃🥓 (@rmoff) <a href="https://twitter.com/rmoff/status/1242139361816305665?ref_src=twsrc%5Etfw">March 23, 2020</a></blockquote>
---

<p>Integrating Apache Kafka with other systems in a reliable and scalable way is often a key part of a streaming platform. Fortunately, Apache Kafka includes the Connect API that enables streaming integration both in and out of Kafka. Like any technology, understanding its architecture and deployment patterns is key to successful use, as is knowing where to go looking when things aren’t working.</p>
<p>This talk will discuss the key design concepts within Kafka Connect and the pros and cons of standalone vs distributed deployment modes. We’ll do a live demo of building pipelines with Kafka Connect for streaming data in from databases, and out to targets including Elasticsearch. With some gremlins along the way, we’ll go hands-on in methodically diagnosing and resolving common issues encountered with Kafka Connect. The talk will finish off by discussing more advanced topics including Single Message Transforms, and deployment of Kafka Connect in containers.</p>
